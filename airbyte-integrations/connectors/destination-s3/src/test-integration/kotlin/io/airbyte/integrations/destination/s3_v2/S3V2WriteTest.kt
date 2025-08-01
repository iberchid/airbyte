/*
 * Copyright (c) 2024 Airbyte, Inc., all rights reserved.
 */

package io.airbyte.integrations.destination.s3_v2

import io.airbyte.cdk.load.command.Append
import io.airbyte.cdk.load.command.DestinationStream
import io.airbyte.cdk.load.command.aws.asMicronautProperties
import io.airbyte.cdk.load.config.DataChannelFormat
import io.airbyte.cdk.load.config.DataChannelMedium
import io.airbyte.cdk.load.data.*
import io.airbyte.cdk.load.data.avro.AvroExpectedRecordMapper
import io.airbyte.cdk.load.message.InputRecord
import io.airbyte.cdk.load.test.util.ExpectedRecordMapper
import io.airbyte.cdk.load.test.util.NoopDestinationCleaner
import io.airbyte.cdk.load.test.util.OutputRecord
import io.airbyte.cdk.load.test.util.UncoercedExpectedRecordMapper
import io.airbyte.cdk.load.test.util.destination_process.DestinationUncleanExitException
import io.airbyte.cdk.load.write.AllTypesBehavior
import io.airbyte.cdk.load.write.BasicFunctionalityIntegrationTest
import io.airbyte.cdk.load.write.SchematizedNestedValueBehavior
import io.airbyte.cdk.load.write.StronglyTyped
import io.airbyte.cdk.load.write.UnionBehavior
import io.airbyte.cdk.load.write.UnknownTypesBehavior
import io.airbyte.cdk.load.write.Untyped
import java.util.concurrent.TimeUnit
import org.junit.jupiter.api.Assumptions
import org.junit.jupiter.api.Disabled
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.Timeout
import org.junit.jupiter.api.assertThrows

@Timeout(60, unit = TimeUnit.MINUTES)
abstract class S3V2WriteTest(
    path: String,
    expectedRecordMapper: ExpectedRecordMapper,
    stringifySchemalessObjects: Boolean,
    schematizedObjectBehavior: SchematizedNestedValueBehavior,
    schematizedArrayBehavior: SchematizedNestedValueBehavior,
    unionBehavior: UnionBehavior,
    commitDataIncrementally: Boolean = true,
    allTypesBehavior: AllTypesBehavior,
    nullEqualsUnset: Boolean = false,
    unknownTypesBehavior: UnknownTypesBehavior = UnknownTypesBehavior.PASS_THROUGH,
    private val mergesUnions: Boolean = false,
    mismatchedTypesUnrepresentable: Boolean = false,
    dataChannelMedium: DataChannelMedium = DataChannelMedium.STDIO,
    dataChannelFormat: DataChannelFormat = DataChannelFormat.JSONL,
) :
    BasicFunctionalityIntegrationTest(
        S3V2TestUtils.getConfig(path),
        S3V2Specification::class.java,
        S3V2DataDumper,
        NoopDestinationCleaner,
        expectedRecordMapper,
        additionalMicronautEnvs = S3V2Destination.additionalMicronautEnvs,
        micronautProperties = S3V2TestUtils.assumeRoleCredentials.asMicronautProperties(),
        isStreamSchemaRetroactive = false,
        dedupBehavior = null,
        stringifySchemalessObjects = stringifySchemalessObjects,
        schematizedObjectBehavior = schematizedObjectBehavior,
        schematizedArrayBehavior = schematizedArrayBehavior,
        unionBehavior = unionBehavior,
        commitDataIncrementally = commitDataIncrementally,
        allTypesBehavior = allTypesBehavior,
        nullEqualsUnset = nullEqualsUnset,
        supportFileTransfer = true,
        unknownTypesBehavior = unknownTypesBehavior,
        mismatchedTypesUnrepresentable = mismatchedTypesUnrepresentable,
        dataChannelMedium = dataChannelMedium,
        dataChannelFormat = dataChannelFormat,
    ) {
    @Disabled("Irrelevant for file destinations")
    @Test
    override fun testAppendSchemaEvolution() {
        super.testAppendSchemaEvolution()
    }

    @Disabled("For most test the file test is not needed since it doesn't apply compression")
    @Test
    override fun testBasicWriteFile() {
        super.testBasicWriteFile()
    }

    @Test
    fun testMergeUnions() {
        Assumptions.assumeTrue(mergesUnions)
        // Avro and parquet merges unions, merging schemas. Validate the behavior by ensuring
        // that fields not matching the schema are dropped.
        val streamName = "stream"
        val stream =
            DestinationStream(
                unmappedNamespace = randomizedNamespace,
                unmappedName = streamName,
                namespaceMapper = namespaceMapperForMedium(),
                importType = Append,
                generationId = 1L,
                minimumGenerationId = 0L,
                syncId = 101L,
                schema =
                    ObjectType(
                        linkedMapOf(
                            "id" to FieldType(IntegerType, nullable = true),
                            "union_of_objects" to
                                FieldType(
                                    type =
                                        UnionType.of(
                                            ObjectType(
                                                linkedMapOf(
                                                    "field1" to FieldType(StringType, true),
                                                    "field2" to FieldType(IntegerType, true),
                                                    "field4" to FieldType(StringType, true)
                                                )
                                            ),
                                            ObjectType(
                                                linkedMapOf(
                                                    "field1" to
                                                        FieldType(
                                                            StringType,
                                                            true
                                                        ), // merges to String
                                                    "field3" to FieldType(NumberType, true),
                                                    "field4" to
                                                        FieldType(
                                                            BooleanType,
                                                            true
                                                        ) // merges to String|Boolean
                                                )
                                            )
                                        ),
                                    nullable = true
                                )
                        )
                    )
            )
        runSync(
            updatedConfig,
            stream,
            listOf(
                    """{"id": 1, "union_of_objects": {"field1": "a", "field2": 1, "field3": 3.14, "field4": "boo", "field5": "extra"}}""",
                    """{"id": 2, "union_of_objects": {"field1": "b", "field2": 2, "field3": 2.71, "field4": true, "field5": "extra"}}"""
                )
                .map { InputRecord(stream, it, 1L) }
        )
        val field4a: Any =
            if (unionBehavior == UnionBehavior.PROMOTE_TO_OBJECT) {
                mapOf("type" to "string", "string" to "boo")
            } else {
                "boo"
            }
        val field4b: Any =
            if (unionBehavior == UnionBehavior.PROMOTE_TO_OBJECT) {
                mapOf("type" to "boolean", "boolean" to true)
            } else {
                true
            }
        dumpAndDiffRecords(
            config = parsedConfig,
            canonicalExpectedRecords =
                listOf(
                        mapOf(
                            "id" to 1,
                            "union_of_objects" to
                                mutableMapOf(
                                    "field1" to "a",
                                    "field2" to 1,
                                    "field3" to 3.14,
                                    "field4" to field4a
                                )
                        ),
                        mapOf(
                            "id" to 2,
                            "union_of_objects" to
                                mapOf(
                                    "field1" to "b",
                                    "field2" to 2,
                                    "field3" to 2.71,
                                    "field4" to field4b
                                )
                        )
                    )
                    .map {
                        OutputRecord(
                            extractedAt = 1L,
                            generationId = 1L,
                            data = it,
                            airbyteMeta = OutputRecord.Meta(syncId = 101L)
                        )
                    },
            stream,
            primaryKey = listOf(listOf("id")),
            cursor = listOf("id")
        )
    }

    @Test
    fun conflictingTypesInMappedUnions() {
        Assumptions.assumeTrue(unionBehavior == UnionBehavior.PROMOTE_TO_OBJECT)
        val stream =
            DestinationStream(
                unmappedNamespace = randomizedNamespace,
                unmappedName = "stream",
                importType = Append,
                generationId = 1L,
                minimumGenerationId = 0L,
                syncId = 101L,
                schema =
                    ObjectType(
                        linkedMapOf(
                            "id" to FieldType(IntegerType, nullable = true),
                            "union_of_objects" to
                                FieldType(
                                    type =
                                        UnionType.of(
                                            ObjectType(
                                                linkedMapOf(
                                                    "field1" to FieldType(StringType, true),
                                                )
                                            ),
                                            ObjectTypeWithoutSchema
                                        ),
                                    nullable = true
                                )
                        )
                    ),
                namespaceMapper = namespaceMapperForMedium()
            )

        assertThrows<DestinationUncleanExitException> {
            runSync(
                updatedConfig,
                stream,
                listOf(
                        """{"id": 1, "union_of_objects": {"field1": "a"}}""",
                        """{"id": 2, "union_of_objects": {"undeclared": "field"}}"""
                    )
                    .map { InputRecord(stream, it, 1L) }
            )
        }
    }

    @Test
    fun testMappableTypesNestedInUnions() {
        // Avro and parquet both merge unions and map complex types to other types. Validate
        // that the behavior still works as expected when nested within a union.
        Assumptions.assumeTrue(mergesUnions)
        val stream =
            DestinationStream(
                unmappedNamespace = randomizedNamespace,
                unmappedName = "stream",
                importType = Append,
                generationId = 1L,
                minimumGenerationId = 0L,
                syncId = 101L,
                schema =
                    ObjectType(
                        linkedMapOf(
                            "id" to FieldType(IntegerType, nullable = true),
                            "union_of_objects" to
                                FieldType(
                                    type =
                                        UnionType.of(
                                            ObjectType(
                                                linkedMapOf(
                                                    "field1" to FieldType(StringType, true),
                                                    "field2" to
                                                        FieldType(
                                                            ObjectType(
                                                                linkedMapOf(
                                                                    "nested_schemaless" to
                                                                        FieldType(
                                                                            ObjectTypeWithoutSchema,
                                                                            true
                                                                        ),
                                                                    "nested_union" to
                                                                        FieldType(
                                                                            UnionType.of(
                                                                                StringType,
                                                                                BooleanType
                                                                            ),
                                                                            true
                                                                        )
                                                                )
                                                            ),
                                                            true
                                                        )
                                                )
                                            ),
                                            StringType
                                        ),
                                    nullable = true
                                ),
                        )
                    ),
                namespaceMapper = namespaceMapperForMedium()
            )

        val expectedRecords =
            if (unionBehavior == UnionBehavior.PROMOTE_TO_OBJECT) {
                listOf(
                    """{"id": 1, "union_of_objects": {"field1": "a", "field2": {"nested_schemaless": "{\"field\": \"value\"}", "nested_union": {"type": "string", "string": "string"}}}}""",
                    """{"id": 2, "union_of_objects": {"field1": "b", "field2": {"nested_schemaless": "{\"field\": \"value\"}", "nested_union": {"type": "boolean", "boolean": true}}}}"""
                )
            } else {
                listOf(
                    """{"id": 1, "union_of_objects": {"field1": "a", "field2": {"nested_schemaless": "{\"field\": \"value\"}", "nested_union": "string"}}}""",
                    """{"id": 2, "union_of_objects": {"field1": "b", "field2": {"nested_schemaless": "{\"field\": \"value\"}", "nested_union": true}}}"""
                )
            }

        runSync(updatedConfig, stream, expectedRecords.map { InputRecord(stream, it, 1L) })
    }
}

class S3V2WriteTestJsonUncompressed :
    S3V2WriteTest(
        S3V2TestUtils.JSON_UNCOMPRESSED_CONFIG_PATH,
        UncoercedExpectedRecordMapper,
        stringifySchemalessObjects = false,
        schematizedObjectBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        schematizedArrayBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        unionBehavior = UnionBehavior.PASS_THROUGH,
        allTypesBehavior = Untyped,
    )

class S3V2WriteTestJsonRootLevelFlattening :
    S3V2WriteTest(
        S3V2TestUtils.JSON_ROOT_LEVEL_FLATTENING_CONFIG_PATH,
        UncoercedExpectedRecordMapper,
        stringifySchemalessObjects = false,
        schematizedObjectBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        schematizedArrayBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        unionBehavior = UnionBehavior.PASS_THROUGH,
        allTypesBehavior = Untyped,
    )

class S3V2WriteTestJsonGzip :
    S3V2WriteTest(
        S3V2TestUtils.JSON_GZIP_CONFIG_PATH,
        UncoercedExpectedRecordMapper,
        stringifySchemalessObjects = false,
        schematizedObjectBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        schematizedArrayBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        unionBehavior = UnionBehavior.PASS_THROUGH,
        allTypesBehavior = Untyped,
    )

class S3V2WriteTestCsvUncompressed :
    S3V2WriteTest(
        S3V2TestUtils.CSV_UNCOMPRESSED_CONFIG_PATH,
        UncoercedExpectedRecordMapper,
        stringifySchemalessObjects = false,
        schematizedObjectBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        schematizedArrayBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        unionBehavior = UnionBehavior.PASS_THROUGH,
        allTypesBehavior = Untyped,
    )

class S3V2WriteTestCsvRootLevelFlattening :
    S3V2WriteTest(
        S3V2TestUtils.CSV_ROOT_LEVEL_FLATTENING_CONFIG_PATH,
        UncoercedExpectedRecordMapper,
        stringifySchemalessObjects = false,
        unionBehavior = UnionBehavior.PASS_THROUGH,
        schematizedObjectBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        schematizedArrayBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        allTypesBehavior = Untyped,
        nullEqualsUnset =
            true, // Technically true of unflattened as well, but no top-level fields are nullable
    )

class S3V2WriteTestCsvGzip :
    S3V2WriteTest(
        S3V2TestUtils.CSV_GZIP_CONFIG_PATH,
        UncoercedExpectedRecordMapper,
        stringifySchemalessObjects = false,
        schematizedObjectBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        schematizedArrayBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        unionBehavior = UnionBehavior.PASS_THROUGH,
        allTypesBehavior = Untyped,
    )

class S3V2WriteTestAvroUncompressedProto :
    S3V2WriteTest(
        S3V2TestUtils.AVRO_UNCOMPRESSED_CONFIG_PATH,
        AvroExpectedRecordMapper,
        stringifySchemalessObjects = true,
        unionBehavior = UnionBehavior.PASS_THROUGH,
        schematizedObjectBehavior = SchematizedNestedValueBehavior.STRONGLY_TYPE,
        schematizedArrayBehavior = SchematizedNestedValueBehavior.STRONGLY_TYPE,
        // this is technically false. Avro + parquet do have limits on numbers.
        // But float64 is weird, in that the actual _limits_ are unreasonably large -
        // but at that size, you have very little precision.
        // This is actually covered by the nested/topLevelFloatLosesPrecision test cases.
        allTypesBehavior = StronglyTyped(integerCanBeLarge = false),
        nullEqualsUnset = true,
        unknownTypesBehavior = UnknownTypesBehavior.FAIL,
        mergesUnions = true,
        dataChannelMedium = DataChannelMedium.SOCKET,
        dataChannelFormat = DataChannelFormat.PROTOBUF,
    ) {

    @Test
    @Disabled("Clear will never run in socket mode")
    override fun testClear() {
        super.testClear()
    }
}

class S3V2WriteTestAvroBzip2Proto :
    S3V2WriteTest(
        S3V2TestUtils.AVRO_BZIP2_CONFIG_PATH,
        AvroExpectedRecordMapper,
        stringifySchemalessObjects = true,
        unionBehavior = UnionBehavior.PASS_THROUGH,
        schematizedObjectBehavior = SchematizedNestedValueBehavior.STRONGLY_TYPE,
        schematizedArrayBehavior = SchematizedNestedValueBehavior.STRONGLY_TYPE,
        allTypesBehavior = StronglyTyped(integerCanBeLarge = false),
        nullEqualsUnset = true,
        unknownTypesBehavior = UnknownTypesBehavior.FAIL,
        mergesUnions = true,
        dataChannelMedium = DataChannelMedium.SOCKET,
        dataChannelFormat = DataChannelFormat.PROTOBUF,
    ) {
    @Test
    @Disabled("Clear will never run in socket mode")
    override fun testClear() {
        super.testClear()
    }
}

class S3V2WriteTestCsvUncompressedProtoSocket :
    S3V2WriteTest(
        S3V2TestUtils.CSV_UNCOMPRESSED_CONFIG_PATH,
        UncoercedExpectedRecordMapper,
        stringifySchemalessObjects = false,
        unionBehavior = UnionBehavior.PASS_THROUGH,
        schematizedObjectBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        schematizedArrayBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        allTypesBehavior = Untyped,
        nullEqualsUnset = true,
        unknownTypesBehavior = UnknownTypesBehavior.NULL,
        mismatchedTypesUnrepresentable = true,
        dataChannelMedium = DataChannelMedium.SOCKET,
        dataChannelFormat = DataChannelFormat.PROTOBUF,
    ) {

    @Test
    @Disabled("Clear will never run in socket mode")
    override fun testClear() {
        super.testClear()
    }
}

class S3V2WriteTestCsvFlattenedProtoSocket :
    S3V2WriteTest(
        S3V2TestUtils.CSV_ROOT_LEVEL_FLATTENING_CONFIG_PATH,
        UncoercedExpectedRecordMapper,
        stringifySchemalessObjects = false,
        unionBehavior = UnionBehavior.PASS_THROUGH,
        schematizedObjectBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        schematizedArrayBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        allTypesBehavior = Untyped,
        nullEqualsUnset = true,
        unknownTypesBehavior = UnknownTypesBehavior.NULL,
        mismatchedTypesUnrepresentable = true,
        dataChannelMedium = DataChannelMedium.SOCKET,
        dataChannelFormat = DataChannelFormat.PROTOBUF,
    ) {

    @Test
    @Disabled("Clear will never run in socket mode")
    override fun testClear() {
        super.testClear()
    }
}

class S3V2WriteTestAvroUncompressed :
    S3V2WriteTest(
        S3V2TestUtils.AVRO_UNCOMPRESSED_CONFIG_PATH,
        AvroExpectedRecordMapper,
        stringifySchemalessObjects = true,
        unionBehavior = UnionBehavior.PASS_THROUGH,
        schematizedObjectBehavior = SchematizedNestedValueBehavior.STRONGLY_TYPE,
        schematizedArrayBehavior = SchematizedNestedValueBehavior.STRONGLY_TYPE,
        // this is technically false. Avro + parquet do have limits on numbers.
        // But float64 is weird, in that the actual _limits_ are unreasonably large -
        // but at that size, you have very little precision.
        // This is actually covered by the nested/topLevelFloatLosesPrecision test cases.
        allTypesBehavior = StronglyTyped(integerCanBeLarge = false),
        nullEqualsUnset = true,
        unknownTypesBehavior = UnknownTypesBehavior.FAIL,
        mergesUnions = true,
    )

class S3V2WriteTestAvroBzip2 :
    S3V2WriteTest(
        S3V2TestUtils.AVRO_BZIP2_CONFIG_PATH,
        AvroExpectedRecordMapper,
        stringifySchemalessObjects = true,
        schematizedObjectBehavior = SchematizedNestedValueBehavior.STRONGLY_TYPE,
        schematizedArrayBehavior = SchematizedNestedValueBehavior.STRONGLY_TYPE,
        unionBehavior = UnionBehavior.PASS_THROUGH,
        allTypesBehavior = StronglyTyped(integerCanBeLarge = false),
        nullEqualsUnset = true,
        unknownTypesBehavior = UnknownTypesBehavior.FAIL,
        mergesUnions = true,
    )

class S3V2WriteTestParquetUncompressed :
    S3V2WriteTest(
        S3V2TestUtils.PARQUET_UNCOMPRESSED_CONFIG_PATH,
        AvroExpectedRecordMapper,
        stringifySchemalessObjects = true,
        schematizedObjectBehavior = SchematizedNestedValueBehavior.STRONGLY_TYPE,
        schematizedArrayBehavior = SchematizedNestedValueBehavior.STRONGLY_TYPE,
        unionBehavior = UnionBehavior.PROMOTE_TO_OBJECT,
        allTypesBehavior = StronglyTyped(integerCanBeLarge = false),
        nullEqualsUnset = true,
        unknownTypesBehavior = UnknownTypesBehavior.FAIL,
        mergesUnions = true,
    )

class S3V2WriteTestParquetUncompressedProto :
    S3V2WriteTest(
        S3V2TestUtils.PARQUET_UNCOMPRESSED_CONFIG_PATH,
        AvroExpectedRecordMapper,
        stringifySchemalessObjects = true,
        schematizedObjectBehavior = SchematizedNestedValueBehavior.STRONGLY_TYPE,
        schematizedArrayBehavior = SchematizedNestedValueBehavior.STRONGLY_TYPE,
        unionBehavior = UnionBehavior.PROMOTE_TO_OBJECT,
        allTypesBehavior = StronglyTyped(integerCanBeLarge = false),
        nullEqualsUnset = true,
        unknownTypesBehavior = UnknownTypesBehavior.FAIL,
        mergesUnions = true,
        dataChannelFormat = DataChannelFormat.PROTOBUF,
        dataChannelMedium = DataChannelMedium.SOCKET
    )

class S3V2WriteTestParquetSnappy :
    S3V2WriteTest(
        S3V2TestUtils.PARQUET_SNAPPY_CONFIG_PATH,
        AvroExpectedRecordMapper,
        stringifySchemalessObjects = true,
        schematizedObjectBehavior = SchematizedNestedValueBehavior.STRONGLY_TYPE,
        schematizedArrayBehavior = SchematizedNestedValueBehavior.STRONGLY_TYPE,
        unionBehavior = UnionBehavior.PROMOTE_TO_OBJECT,
        allTypesBehavior = StronglyTyped(integerCanBeLarge = false),
        nullEqualsUnset = true,
        unknownTypesBehavior = UnknownTypesBehavior.FAIL,
        mergesUnions = true,
    )

class S3V2WriteTestParquetSnappyProto :
    S3V2WriteTest(
        S3V2TestUtils.PARQUET_SNAPPY_CONFIG_PATH,
        AvroExpectedRecordMapper,
        stringifySchemalessObjects = true,
        schematizedObjectBehavior = SchematizedNestedValueBehavior.STRONGLY_TYPE,
        schematizedArrayBehavior = SchematizedNestedValueBehavior.STRONGLY_TYPE,
        unionBehavior = UnionBehavior.PROMOTE_TO_OBJECT,
        allTypesBehavior = StronglyTyped(integerCanBeLarge = false),
        nullEqualsUnset = true,
        unknownTypesBehavior = UnknownTypesBehavior.FAIL,
        mergesUnions = true,
        dataChannelFormat = DataChannelFormat.PROTOBUF,
        dataChannelMedium = DataChannelMedium.SOCKET
    )

class S3V2WriteTestEndpointURL :
    S3V2WriteTest(
        S3V2TestUtils.ENDPOINT_URL_CONFIG_PATH,
        // this test is writing to CSV
        UncoercedExpectedRecordMapper,
        stringifySchemalessObjects = false,
        unionBehavior = UnionBehavior.PASS_THROUGH,
        schematizedObjectBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        schematizedArrayBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        allTypesBehavior = Untyped,
        nullEqualsUnset = true,
    )

class S3V2AmbiguousFilepath :
    S3V2WriteTest(
        S3V2TestUtils.AMBIGUOUS_FILEPATH_CONFIG_PATH,
        // this test is writing to CSV
        UncoercedExpectedRecordMapper,
        stringifySchemalessObjects = false,
        unionBehavior = UnionBehavior.PASS_THROUGH,
        schematizedObjectBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        schematizedArrayBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        allTypesBehavior = Untyped,
    )

class S3V2CsvAssumeRole :
    S3V2WriteTest(
        S3V2TestUtils.CSV_ASSUME_ROLE_CONFIG_PATH,
        UncoercedExpectedRecordMapper,
        stringifySchemalessObjects = false,
        schematizedObjectBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        schematizedArrayBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        unionBehavior = UnionBehavior.PASS_THROUGH,
        allTypesBehavior = Untyped,
    )

class S3V2WriteTestJsonUncompressedSockets :
    S3V2WriteTest(
        S3V2TestUtils.JSON_UNCOMPRESSED_CONFIG_PATH,
        UncoercedExpectedRecordMapper,
        stringifySchemalessObjects = false,
        schematizedObjectBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        schematizedArrayBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        unionBehavior = UnionBehavior.PASS_THROUGH,
        allTypesBehavior = Untyped,
        dataChannelMedium = DataChannelMedium.SOCKET
    ) {
    @Test
    @Disabled("Clear will never run in socket mode")
    override fun testClear() {
        super.testClear()
    }
}

class S3V2WriteTestJsonUncompressedSocketsProtobuf :
    S3V2WriteTest(
        S3V2TestUtils.JSON_UNCOMPRESSED_CONFIG_PATH,
        UncoercedExpectedRecordMapper,
        stringifySchemalessObjects = false,
        unionBehavior = UnionBehavior.PASS_THROUGH,
        schematizedObjectBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        schematizedArrayBehavior = SchematizedNestedValueBehavior.PASS_THROUGH,
        allTypesBehavior = Untyped,
        // Because proto uses a fixed-sized array of typed unions, nulls are always present
        nullEqualsUnset = true,
        unknownTypesBehavior = UnknownTypesBehavior.NULL,
        mismatchedTypesUnrepresentable = true,
        dataChannelMedium = DataChannelMedium.SOCKET,
        dataChannelFormat = DataChannelFormat.PROTOBUF,
    ) {
    @Test
    @Disabled("Clear will never run in socket mode")
    override fun testClear() {
        super.testClear()
    }
}
