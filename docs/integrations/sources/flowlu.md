# Flowlu
Flowlu connector enables seamless data integration between Flowlu, a project management and CRM platform, and various destinations supported by Airbyte. With this connector, users can automate the flow of project, finance, and CRM data into their preferred analytics or storage solutions for enhanced data analysis and reporting. This integration streamlines data syncing, reducing manual data transfer efforts and enhancing productivity.

## Configuration

| Input | Type | Description | Default Value |
|-------|------|-------------|---------------|
| `api_key` | `string` | API Key. The API key to use for authentication |  |
| `company` | `string` | Sub Domain information for the Company.  |  |

## Streams
| Stream Name | Primary Key | Pagination | Supports Full Sync | Supports Incremental |
|-------------|-------------|------------|---------------------|----------------------|
| tasks | id | DefaultPaginator | ✅ |  ❌  |
| custom_fields | id | DefaultPaginator | ✅ |  ❌  |
| agile_workflows | id | DefaultPaginator | ✅ |  ❌  |
| st_projects_users |  | DefaultPaginator | ✅ |  ❌  |
| projects | id | DefaultPaginator | ✅ |  ❌  |
| account | id | DefaultPaginator | ✅ |  ❌  |
| agile_epics | id | DefaultPaginator | ✅ |  ❌  |
| loss_reason | id | DefaultPaginator | ✅ |  ❌  |
| pipeline |  | DefaultPaginator | ✅ |  ❌  |
| lead | id | DefaultPaginator | ✅ |  ❌  |
| emails | id | DefaultPaginator | ✅ |  ❌  |
| invoice | id | DefaultPaginator | ✅ |  ❌  |
| customer_payment | id | DefaultPaginator | ✅ |  ❌  |
| bank_account | id | DefaultPaginator | ✅ |  ❌  |
| agile_stages | id | DefaultPaginator | ✅ |  ❌  |
| agile_sprints | id | DefaultPaginator | ✅ |  ❌  |
| agile_issues | id | DefaultPaginator | ✅ |  ❌  |
| task_lists | id | DefaultPaginator | ✅ |  ❌  |
| lists | id | DefaultPaginator | ✅ |  ❌  |
| calendar | id | DefaultPaginator | ✅ |  ❌  |
| agile_issue_relation_types | id | DefaultPaginator | ✅ |  ❌  |
| agile_issue_relation_names | id | DefaultPaginator | ✅ |  ❌  |
| agile_issue_type | id | DefaultPaginator | ✅ |  ❌  |
| agile_categories | id | DefaultPaginator | ✅ |  ❌  |
| custom_fields_field_sets | id | DefaultPaginator | ✅ |  ❌  |
| product_list | id | DefaultPaginator | ✅ |  ❌  |
| product_categories | id | DefaultPaginator | ✅ |  ❌  |
| product_price_list | id | DefaultPaginator | ✅ |  ❌  |
| product_manufacturer | id | DefaultPaginator | ✅ |  ❌  |
| timesheet | id | DefaultPaginator | ✅ |  ❌  |
| estimates | id | DefaultPaginator | ✅ |  ❌  |
| transactions | id | DefaultPaginator | ✅ |  ❌  |
| invoice_items | id | DefaultPaginator | ✅ |  ❌  |
| invoice_contacts | id | DefaultPaginator | ✅ |  ❌  |
| project_observers | id | DefaultPaginator | ✅ |  ❌  |
| task_workflows | id | DefaultPaginator | ✅ |  ❌  |

## Changelog

<details>
  <summary>Expand to review</summary>

| Version          | Date              | Pull Request | Subject        |
|------------------|-------------------|--------------|----------------|
| 0.0.29 | 2025-07-26 | [64026](https://github.com/airbytehq/airbyte/pull/64026) | Update dependencies |
| 0.0.28 | 2025-07-19 | [63568](https://github.com/airbytehq/airbyte/pull/63568) | Update dependencies |
| 0.0.27 | 2025-07-12 | [62989](https://github.com/airbytehq/airbyte/pull/62989) | Update dependencies |
| 0.0.26 | 2025-07-05 | [62810](https://github.com/airbytehq/airbyte/pull/62810) | Update dependencies |
| 0.0.25 | 2025-06-28 | [62303](https://github.com/airbytehq/airbyte/pull/62303) | Update dependencies |
| 0.0.24 | 2025-06-22 | [61998](https://github.com/airbytehq/airbyte/pull/61998) | Update dependencies |
| 0.0.23 | 2025-06-14 | [61177](https://github.com/airbytehq/airbyte/pull/61177) | Update dependencies |
| 0.0.22 | 2025-05-24 | [60428](https://github.com/airbytehq/airbyte/pull/60428) | Update dependencies |
| 0.0.21 | 2025-05-10 | [59946](https://github.com/airbytehq/airbyte/pull/59946) | Update dependencies |
| 0.0.20 | 2025-05-03 | [59451](https://github.com/airbytehq/airbyte/pull/59451) | Update dependencies |
| 0.0.19 | 2025-04-26 | [58912](https://github.com/airbytehq/airbyte/pull/58912) | Update dependencies |
| 0.0.18 | 2025-04-19 | [58338](https://github.com/airbytehq/airbyte/pull/58338) | Update dependencies |
| 0.0.17 | 2025-04-12 | [57779](https://github.com/airbytehq/airbyte/pull/57779) | Update dependencies |
| 0.0.16 | 2025-04-05 | [57252](https://github.com/airbytehq/airbyte/pull/57252) | Update dependencies |
| 0.0.15 | 2025-03-29 | [56493](https://github.com/airbytehq/airbyte/pull/56493) | Update dependencies |
| 0.0.14 | 2025-03-22 | [55962](https://github.com/airbytehq/airbyte/pull/55962) | Update dependencies |
| 0.0.13 | 2025-03-08 | [55276](https://github.com/airbytehq/airbyte/pull/55276) | Update dependencies |
| 0.0.12 | 2025-03-01 | [54941](https://github.com/airbytehq/airbyte/pull/54941) | Update dependencies |
| 0.0.11 | 2025-02-22 | [54406](https://github.com/airbytehq/airbyte/pull/54406) | Update dependencies |
| 0.0.10 | 2025-02-15 | [53353](https://github.com/airbytehq/airbyte/pull/53353) | Update dependencies |
| 0.0.9 | 2025-02-01 | [52811](https://github.com/airbytehq/airbyte/pull/52811) | Update dependencies |
| 0.0.8 | 2025-01-25 | [52361](https://github.com/airbytehq/airbyte/pull/52361) | Update dependencies |
| 0.0.7 | 2025-01-18 | [51623](https://github.com/airbytehq/airbyte/pull/51623) | Update dependencies |
| 0.0.6 | 2025-01-11 | [51066](https://github.com/airbytehq/airbyte/pull/51066) | Update dependencies |
| 0.0.5 | 2024-12-28 | [50538](https://github.com/airbytehq/airbyte/pull/50538) | Update dependencies |
| 0.0.4 | 2024-12-21 | [50034](https://github.com/airbytehq/airbyte/pull/50034) | Update dependencies |
| 0.0.3 | 2024-12-14 | [49518](https://github.com/airbytehq/airbyte/pull/49518) | Update dependencies |
| 0.0.2 | 2024-12-12 | [48921](https://github.com/airbytehq/airbyte/pull/48921) | Update dependencies |
| 0.0.1 | 2024-11-11 | | Initial release by [@bishalbera](https://github.com/bishalbera) via Connector Builder |

</details>
