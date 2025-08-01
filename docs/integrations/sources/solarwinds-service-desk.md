# Solarwinds Service Desk
## Overview

The Solarwinds Service Desk connector support both Full sync and Incremental.

Documentation: https://apidoc.samanage.com/#section/General-Concepts

## Configuration

| Input | Type | Description | Default Value |
|-------|------|-------------|---------------|
| `api_key_2` | `string` | API Key. Refer to `https://documentation.solarwinds.com/en/success_center/swsd/content/completeguidetoswsd/token-authentication-for-api-integration.htm#link4` |  |
| `start_date` | `string` | Start date.  |  |

## Streams
| Stream Name | Primary Key | Pagination | Supports Full Sync | Supports Incremental |
|-------------|-------------|------------|---------------------|----------------------|
| hardwares | id | DefaultPaginator | ✅ |  ✅  |
| risks | id | DefaultPaginator | ✅ |  ✅  |
| audits | uuid | DefaultPaginator | ✅ |  ✅  |
| vendors | id | DefaultPaginator | ✅ |  ❌  |
| purchase_orders | id | DefaultPaginator | ✅ |  ✅  |
| contracts | id | DefaultPaginator | ✅ |  ✅  |
| assets | id | DefaultPaginator | ✅ |  ✅  |
| mobiles | id | DefaultPaginator | ✅ |  ❌  |
| categories | id | DefaultPaginator | ✅ |  ❌  |
| groups | id | DefaultPaginator | ✅ |  ❌  |
| roles | id | DefaultPaginator | ✅ |  ❌  |
| departments | id | DefaultPaginator | ✅ |  ❌  |
| sites | id | DefaultPaginator | ✅ |  ❌  |
| users | id | DefaultPaginator | ✅ |  ✅  |
| configuration_items | id | DefaultPaginator | ✅ |  ✅  |
| solutions | id | DefaultPaginator | ✅ |  ✅  |
| releases | id | DefaultPaginator | ✅ |  ✅  |
| change_catalogs | id | DefaultPaginator | ✅ |  ✅  |
| changes | id | DefaultPaginator | ✅ |  ✅  |
| incidents | id | DefaultPaginator | ✅ |  ✅  |
| catalog_items | id | DefaultPaginator | ✅ |  ✅  |
| problems | id | DefaultPaginator | ✅ |  ✅  |

## Changelog

<details>
  <summary>Expand to review</summary>

| Version          | Date              | Pull Request | Subject        |
|------------------|-------------------|--------------|----------------|
| 0.0.31 | 2025-07-26 | [63966](https://github.com/airbytehq/airbyte/pull/63966) | Update dependencies |
| 0.0.30 | 2025-07-19 | [63632](https://github.com/airbytehq/airbyte/pull/63632) | Update dependencies |
| 0.0.29 | 2025-07-12 | [63076](https://github.com/airbytehq/airbyte/pull/63076) | Update dependencies |
| 0.0.28 | 2025-07-05 | [62719](https://github.com/airbytehq/airbyte/pull/62719) | Update dependencies |
| 0.0.27 | 2025-06-28 | [62266](https://github.com/airbytehq/airbyte/pull/62266) | Update dependencies |
| 0.0.26 | 2025-06-14 | [61311](https://github.com/airbytehq/airbyte/pull/61311) | Update dependencies |
| 0.0.25 | 2025-05-25 | [60569](https://github.com/airbytehq/airbyte/pull/60569) | Update dependencies |
| 0.0.24 | 2025-05-10 | [60067](https://github.com/airbytehq/airbyte/pull/60067) | Update dependencies |
| 0.0.23 | 2025-05-04 | [59638](https://github.com/airbytehq/airbyte/pull/59638) | Update dependencies |
| 0.0.22 | 2025-04-27 | [59022](https://github.com/airbytehq/airbyte/pull/59022) | Update dependencies |
| 0.0.21 | 2025-04-19 | [58404](https://github.com/airbytehq/airbyte/pull/58404) | Update dependencies |
| 0.0.20 | 2025-04-12 | [57981](https://github.com/airbytehq/airbyte/pull/57981) | Update dependencies |
| 0.0.19 | 2025-04-05 | [57437](https://github.com/airbytehq/airbyte/pull/57437) | Update dependencies |
| 0.0.18 | 2025-03-29 | [56889](https://github.com/airbytehq/airbyte/pull/56889) | Update dependencies |
| 0.0.17 | 2025-03-22 | [56286](https://github.com/airbytehq/airbyte/pull/56286) | Update dependencies |
| 0.0.16 | 2025-03-08 | [55643](https://github.com/airbytehq/airbyte/pull/55643) | Update dependencies |
| 0.0.15 | 2025-03-01 | [55102](https://github.com/airbytehq/airbyte/pull/55102) | Update dependencies |
| 0.0.14 | 2025-02-22 | [54520](https://github.com/airbytehq/airbyte/pull/54520) | Update dependencies |
| 0.0.13 | 2025-02-15 | [54063](https://github.com/airbytehq/airbyte/pull/54063) | Update dependencies |
| 0.0.12 | 2025-02-08 | [53519](https://github.com/airbytehq/airbyte/pull/53519) | Update dependencies |
| 0.0.11 | 2025-02-01 | [53096](https://github.com/airbytehq/airbyte/pull/53096) | Update dependencies |
| 0.0.10 | 2025-01-25 | [52410](https://github.com/airbytehq/airbyte/pull/52410) | Update dependencies |
| 0.0.9 | 2025-01-18 | [51977](https://github.com/airbytehq/airbyte/pull/51977) | Update dependencies |
| 0.0.8 | 2025-01-11 | [51409](https://github.com/airbytehq/airbyte/pull/51409) | Update dependencies |
| 0.0.7 | 2025-01-04 | [50748](https://github.com/airbytehq/airbyte/pull/50748) | Update dependencies |
| 0.0.6 | 2024-12-21 | [50360](https://github.com/airbytehq/airbyte/pull/50360) | Update dependencies |
| 0.0.5 | 2024-12-14 | [49771](https://github.com/airbytehq/airbyte/pull/49771) | Update dependencies |
| 0.0.4 | 2024-12-12 | [49418](https://github.com/airbytehq/airbyte/pull/49418) | Update dependencies |
| 0.0.3 | 2024-12-11 | [49111](https://github.com/airbytehq/airbyte/pull/49111) | Starting with this version, the Docker image is now rootless. Please note that this and future versions will not be compatible with Airbyte versions earlier than 0.64 |
| 0.0.2 | 2024-10-29 | [47855](https://github.com/airbytehq/airbyte/pull/47855) | Update dependencies |
| 0.0.1 | 2024-10-10 | [46707](https://github.com/airbytehq/airbyte/pull/46707) | Initial release by [@gemsteam](https://github.com/gemsteam) via Connector Builder |

</details>
