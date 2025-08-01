# Survicate
This page contains the setup guide and reference information for the [Survicate](https://survicate.com/) source connector.

## Prerequisites
To set up the Survicate source connector with Airbyte, you'll need to create your API keys from theie settings page. Please refer `https://developers.survicate.com/data-export/setup/` for getting your api_key.

## Documentation reference:
Visit `https://developers.survicate.com/data-export/setup/` for API documentation

## Authentication setup
Refer `https://developers.survicate.com/data-export/setup/#authentication` for more details.

## Configuration

| Input | Type | Description | Default Value |
|-------|------|-------------|---------------|
| `api_key` | `string` | API Key.  |  |
| `start_date` | `string` | Start date.  |  |

## Streams
| Stream Name | Primary Key | Pagination | Supports Full Sync | Supports Incremental |
|-------------|-------------|------------|---------------------|----------------------|
| surveys | id | DefaultPaginator | ✅ |  ✅  |
| surveys_questions | id | DefaultPaginator | ✅ |  ❌  |
| surveys_responses | uuid | DefaultPaginator | ✅ |  ✅  |
| respondents_attributes |  | DefaultPaginator | ✅ |  ❌  |
| respondents_responses |  | DefaultPaginator | ✅ |  ❌  |

## Changelog

<details>
  <summary>Expand to review</summary>

| Version | Date | Pull Request | Subject |
| ------------------ | ------------ | -- | ---------------- |
| 0.0.30 | 2025-07-19 | [63621](https://github.com/airbytehq/airbyte/pull/63621) | Update dependencies |
| 0.0.29 | 2025-07-12 | [63090](https://github.com/airbytehq/airbyte/pull/63090) | Update dependencies |
| 0.0.28 | 2025-07-05 | [62681](https://github.com/airbytehq/airbyte/pull/62681) | Update dependencies |
| 0.0.27 | 2025-06-28 | [61459](https://github.com/airbytehq/airbyte/pull/61459) | Update dependencies |
| 0.0.26 | 2025-05-24 | [60508](https://github.com/airbytehq/airbyte/pull/60508) | Update dependencies |
| 0.0.25 | 2025-05-10 | [60178](https://github.com/airbytehq/airbyte/pull/60178) | Update dependencies |
| 0.0.24 | 2025-05-04 | [59577](https://github.com/airbytehq/airbyte/pull/59577) | Update dependencies |
| 0.0.23 | 2025-04-24 | [58084](https://github.com/airbytehq/airbyte/pull/58084) | Fix `respondents_attributes` stream |
| 0.0.22 | 2025-04-27 | [58981](https://github.com/airbytehq/airbyte/pull/58981) | Update dependencies |
| 0.0.21 | 2025-04-19 | [58424](https://github.com/airbytehq/airbyte/pull/58424) | Update dependencies |
| 0.0.20 | 2025-04-12 | [57949](https://github.com/airbytehq/airbyte/pull/57949) | Update dependencies |
| 0.0.19 | 2025-04-05 | [57436](https://github.com/airbytehq/airbyte/pull/57436) | Update dependencies |
| 0.0.18 | 2025-03-29 | [56865](https://github.com/airbytehq/airbyte/pull/56865) | Update dependencies |
| 0.0.17 | 2025-03-22 | [56307](https://github.com/airbytehq/airbyte/pull/56307) | Update dependencies |
| 0.0.16 | 2025-03-08 | [55581](https://github.com/airbytehq/airbyte/pull/55581) | Update dependencies |
| 0.0.15 | 2025-03-01 | [54545](https://github.com/airbytehq/airbyte/pull/54545) | Update dependencies |
| 0.0.14 | 2025-02-15 | [54052](https://github.com/airbytehq/airbyte/pull/54052) | Update dependencies |
| 0.0.13 | 2025-02-08 | [53565](https://github.com/airbytehq/airbyte/pull/53565) | Update dependencies |
| 0.0.12 | 2025-02-01 | [53101](https://github.com/airbytehq/airbyte/pull/53101) | Update dependencies |
| 0.0.11 | 2025-01-25 | [52397](https://github.com/airbytehq/airbyte/pull/52397) | Update dependencies |
| 0.0.10 | 2025-01-18 | [51954](https://github.com/airbytehq/airbyte/pull/51954) | Update dependencies |
| 0.0.9 | 2025-01-11 | [51457](https://github.com/airbytehq/airbyte/pull/51457) | Update dependencies |
| 0.0.8 | 2024-12-28 | [50801](https://github.com/airbytehq/airbyte/pull/50801) | Update dependencies |
| 0.0.7 | 2024-12-21 | [50313](https://github.com/airbytehq/airbyte/pull/50313) | Update dependencies |
| 0.0.6 | 2024-12-14 | [49747](https://github.com/airbytehq/airbyte/pull/49747) | Update dependencies |
| 0.0.5 | 2024-12-12 | [49420](https://github.com/airbytehq/airbyte/pull/49420) | Update dependencies |
| 0.0.4 | 2024-11-04 | [48278](https://github.com/airbytehq/airbyte/pull/48278) | Update dependencies |
| 0.0.3 | 2024-10-29 | [47884](https://github.com/airbytehq/airbyte/pull/47884) | Update dependencies |
| 0.0.2 | 2024-10-28 | [47494](https://github.com/airbytehq/airbyte/pull/47494) | Update dependencies |
| 0.0.1 | 2024-09-05 | [45163](https://github.com/airbytehq/airbyte/pull/45163) | Initial release by [@btkcodedev](https://github.com/btkcodedev) via Connector Builder |

</details>
