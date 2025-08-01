# Shippo
This is the Shippo source for ingesting data using the Shippo API.

Shippo is your one-stop solution for shipping labels. Whether you use our app to ship or API to power your logistics workflow, Shippo gives you scalable shipping tools, the best rates, and world-class support https://goshippo.com/

In order to use this source, you must first create a Shippo account. Once logged in, head over to Settings -&gt; Advanced -&gt; API and click on generate new token. You can learn more about the API here https://docs.goshippo.com/shippoapi/public-api/#tag/Overview 

## Configuration

| Input | Type | Description | Default Value |
|-------|------|-------------|---------------|
| `shippo_token` | `string` | Shippo Token. The bearer token used for making requests |  |
| `start_date` | `string` | Start date.  |  |

## Streams
| Stream Name | Primary Key | Pagination | Supports Full Sync | Supports Incremental |
|-------------|-------------|------------|---------------------|----------------------|
| addresses | id | DefaultPaginator | ✅ |  ❌  |
| parcels | object_id | DefaultPaginator | ✅ |  ❌  |
| custom_items | object_id | DefaultPaginator | ✅ |  ❌  |
| accounts | object_id | DefaultPaginator | ✅ |  ❌  |
| carrier_acounts | object_id | DefaultPaginator | ✅ |  ❌  |
| shipments | object_id | DefaultPaginator | ✅ |  ✅  |

## Changelog

<details>
  <summary>Expand to review</summary>

| Version          | Date              | Pull Request | Subject        |
|------------------|-------------------|--------------|----------------|
| 0.0.25 | 2025-07-26 | [64004](https://github.com/airbytehq/airbyte/pull/64004) | Update dependencies |
| 0.0.24 | 2025-07-20 | [63675](https://github.com/airbytehq/airbyte/pull/63675) | Update dependencies |
| 0.0.23 | 2025-06-28 | [62245](https://github.com/airbytehq/airbyte/pull/62245) | Update dependencies |
| 0.0.22 | 2025-06-21 | [61456](https://github.com/airbytehq/airbyte/pull/61456) | Update dependencies |
| 0.0.21 | 2025-05-24 | [60475](https://github.com/airbytehq/airbyte/pull/60475) | Update dependencies |
| 0.0.20 | 2025-05-10 | [59616](https://github.com/airbytehq/airbyte/pull/59616) | Update dependencies |
| 0.0.19 | 2025-04-27 | [58387](https://github.com/airbytehq/airbyte/pull/58387) | Update dependencies |
| 0.0.18 | 2025-04-12 | [57417](https://github.com/airbytehq/airbyte/pull/57417) | Update dependencies |
| 0.0.17 | 2025-03-29 | [56857](https://github.com/airbytehq/airbyte/pull/56857) | Update dependencies |
| 0.0.16 | 2025-03-22 | [56299](https://github.com/airbytehq/airbyte/pull/56299) | Update dependencies |
| 0.0.15 | 2025-03-08 | [55594](https://github.com/airbytehq/airbyte/pull/55594) | Update dependencies |
| 0.0.14 | 2025-03-01 | [55153](https://github.com/airbytehq/airbyte/pull/55153) | Update dependencies |
| 0.0.13 | 2025-02-22 | [54487](https://github.com/airbytehq/airbyte/pull/54487) | Update dependencies |
| 0.0.12 | 2025-02-15 | [54069](https://github.com/airbytehq/airbyte/pull/54069) | Update dependencies |
| 0.0.11 | 2025-02-08 | [53535](https://github.com/airbytehq/airbyte/pull/53535) | Update dependencies |
| 0.0.10 | 2025-02-01 | [52997](https://github.com/airbytehq/airbyte/pull/52997) | Update dependencies |
| 0.0.9 | 2025-01-25 | [52451](https://github.com/airbytehq/airbyte/pull/52451) | Update dependencies |
| 0.0.8 | 2025-01-18 | [51924](https://github.com/airbytehq/airbyte/pull/51924) | Update dependencies |
| 0.0.7 | 2025-01-11 | [51315](https://github.com/airbytehq/airbyte/pull/51315) | Update dependencies |
| 0.0.6 | 2024-12-28 | [50702](https://github.com/airbytehq/airbyte/pull/50702) | Update dependencies |
| 0.0.5 | 2024-12-21 | [50292](https://github.com/airbytehq/airbyte/pull/50292) | Update dependencies |
| 0.0.4 | 2024-12-14 | [49727](https://github.com/airbytehq/airbyte/pull/49727) | Update dependencies |
| 0.0.3 | 2024-12-12 | [49352](https://github.com/airbytehq/airbyte/pull/49352) | Update dependencies |
| 0.0.2 | 2024-12-11 | [49101](https://github.com/airbytehq/airbyte/pull/49101) | Starting with this version, the Docker image is now rootless. Please note that this and future versions will not be compatible with Airbyte versions earlier than 0.64 |
| 0.0.1 | 2024-10-28 | | Initial release by [@aazam-gh](https://github.com/aazam-gh) via Connector Builder |

</details>
