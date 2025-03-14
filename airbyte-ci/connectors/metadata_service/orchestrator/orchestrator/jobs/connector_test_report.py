#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#

from dagster import AssetSelection, define_asset_job


nightly_reports_inclusive = AssetSelection.keys("generate_nightly_report").upstream()
generate_nightly_reports = define_asset_job(name="generate_nightly_reports", selection=nightly_reports_inclusive)

connector_test_reports_inclusive = AssetSelection.keys("persist_connectors_test_summary_files").upstream()
generate_connector_test_summary_reports = define_asset_job(
    name="generate_connector_test_summary_reports", selection=connector_test_reports_inclusive
)
