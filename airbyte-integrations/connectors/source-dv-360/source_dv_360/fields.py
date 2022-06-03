#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


import re


def sanitize(s):
  s = re.sub('[&]', 'and', s)
  s = re.sub('[%]', 'pct', s)
  s = re.sub('[\s/-]+', '_', s.strip())
  # Remove punctuation, which is anything that is not either a word or a whitespace character
  s = re.sub('[^\w\s]+', '', s)
  return s.lower()

# Mapping betwee naming in the connector and naming in the report builder
API_REPORT_BUILDER_MAPPING = {
  "audience_list":"FILTER_AUDIENCE_LIST",
  "date":"FILTER_DATE",
  "eligible_cookies_on_first_party_audience_list":"FILTER_ELIGIBLE_COOKIES_ON_FIRST_PARTY_AUDIENCE_LIST",
  "eligible_cookies_on_third_party_audience_list_and_interest":"FILTER_ELIGIBLE_COOKIES_ON_THIRD_PARTY_AUDIENCE_LIST_AND_INTEREST",
  "first_party_audience_list":"FILTER_USER_LIST_FIRST_PARTY_NAME",
  "first_party_audience_list_cost":"FILTER_FIRST_PARTY_AUDIENCE_LIST_COST",
  "first_party_audience_list_id":"FILTER_USER_LIST_FIRST_PARTY",
  "first_party_audience_list_type":"FILTER_FIRST_PARTY_AUDIENCE_LIST_TYPE",
  "match_ratio":"FILTER_MATCH_RATIO",
  "third_party_audience_list":"FILTER_USER_LIST_THIRD_PARTY_NAME",
  "third_party_audience_list_cost":"FILTER_THIRD_PARTY_AUDIENCE_LIST_COST",
  "third_party_audience_list_id":"FILTER_USER_LIST_THIRD_PARTY",
  "third_party_audience_list_type":"FILTER_THIRD_PARTY_AUDIENCE_LIST_TYPE",
  "advertiser":"FILTER_ADVERTISER_NAME",
  "advertiser_currency":"FILTER_ADVERTISER_CURRENCY",
  "advertiser_id":"FILTER_ADVERTISER",
  "advertiser_integration_code":"FILTER_ADVERTISER_INTEGRATION_CODE",
  "advertiser_status":"FILTER_ADVERTISER_INTEGRATION_STATUS",
  "advertiser_time_zone":"FILTER_ADVERTISER_TIMEZONE",
  "app_url":"FILTER_APP_URL",
  "app_url_excluded":"FILTER_APP_URL_EXCLUDED",
  "app_url_id":"FILTER_SITE_ID",
  "campaign":"FILTER_MEDIA_PLAN_NAME",
  "campaign_id":"FILTER_MEDIA_PLAN",
  "category":"FILTER_PAGE_CATEGORY",
  "cm_placement_id":"FILTER_CM_PLACEMENT_ID",
  "creative":"FILTER_CREATIVE",
  "creative_asset":"FILTER_CREATIVE_ASSET",
  "creative_attributes":"FILTER_CREATIVE_ATTRIBUTE",
  "creative_height":"FILTER_CREATIVE_HEIGHT",
  "creative_id":"FILTER_CREATIVE_ID",
  "creative_integration_code":"FILTER_CREATIVE_INTEGRATION_CODE",
  "creative_rendered_in_amp":"FILTER_CREATIVE_RENDERED_IN_AMP",
  "creative_size":"FILTER_CREATIVE_SIZE",
  "creative_source":"FILTER_CREATIVE_SOURCE",
  "creative_status":"FILTER_CREATIVE_STATUS",
  "creative_type":"FILTER_CREATIVE_TYPE",
  "creative_width":"FILTER_CREATIVE_WIDTH",
  "day_of_week":"FILTER_DAY_OF_WEEK",
  "exchange":"FILTER_EXCHANGE",
  "exchange_code":"FILTER_EXCHANGE_CODE",
  "exchange_id":"FILTER_EXCHANGE_ID",
  "floodlight_activity":"FILTER_FLOODLIGHT_ACTIVITY",
  "floodlight_activity_id":"FILTER_FLOODLIGHT_ACTIVITY_ID",
  "insertion_order":"FILTER_INSERTION_ORDER_NAME",
  "insertion_order_integration_code":"FILTER_INSERTION_ORDER_INTEGRATION_CODE",
  "insertion_order_status":"FILTER_INSERTION_ORDER_STATUS",
  "line_item":"FILTER_LINE_ITEM_NAME",
  "line_item_id":"FILTER_LINE_ITEM",
  "line_item_integration_code":"FILTER_LINE_ITEM_INTEGRATION_CODE",
  "line_item_status":"FILTER_LINE_ITEM_STATUS",
  "line_item_type":"FILTER_LINE_ITEM_TYPE",
  "month":"FILTER_MONTH",
  "order_id":"FILTER_ORDER_ID",
  "partner":"FILTER_PARTNER_NAME",
  "partner_currency":"FILTER_PARTNER_CURRENCY",
  "partner_id":"FILTER_PARTNER",
  "partner_status":"FILTER_PARTNER_STATUS",
  "targeted_data_providers":"FILTER_TARGETED_DATA_PROVIDERS",
  "year":"FILTER_YEAR",
  "country":"FILTER_COUNTRY",
  "country_id":"FILTER_COUNTRY_ID",
  "insertion_order_id":"FILTER_INSERTION_ORDER",
  "inventory_source":"FILTER_INVENTORY_SOURCE_NAME",
  "active_view_custom_metric_id":"FILTER_ACTIVE_VIEW_CUSTOM_METRIC_ID",
  "active_view_custom_metric_name":"FILTER_ACTIVE_VIEW_CUSTOM_METRIC_NAME",
  "ad_position":"FILTER_AD_POSITION",
  "ad_type":"FILTER_AD_TYPE",
  "algorithm":"FILTER_ALGORITHM",
  "algorithm_id":"FILTER_ALGORITHM_ID",
  "amp_page_request":"FILTER_AMP_PAGE_REQUEST",
  "attributed_userlist":"FILTER_ATTRIBUTED_USERLIST",
  "attributed_userlist_cost":"FILTER_ATTRIBUTED_USERLIST_COST",
  "attributed_userlist_id":"FILTER_TARGETED_USER_LIST",
  "attributed_userlist_type":"FILTER_ATTRIBUTED_USERLIST_TYPE",
  "attribution_model":"FILTER_ATTRIBUTION_MODEL",
  "audience_list_cost":"FILTER_AUDIENCE_LIST_COST",
  "audience_list_id":"FILTER_USER_LIST",
  "audience_list_type":"FILTER_AUDIENCE_LIST_TYPE",
  "audience_name":"FILTER_AUDIENCE_NAME",
  "audience_type":"FILTER_AUDIENCE_TYPE",
  "authorized_seller_state":"FILTER_AUTHORIZED_SELLER_STATE",
  "billable_outcome":"FILTER_BILLABLE_OUTCOME",
  "brand_lift_type":"FILTER_BRAND_LIFT_TYPE",
  "browser_id":"FILTER_BROWSER",
  "budget_segment_description":"FILTER_BUDGET_SEGMENT_DESCRIPTION",
  "channel":"FILTER_CHANNEL_NAME",
  "channel_id":"FILTER_CHANNEL_ID",
  "channel_type":"FILTER_CHANNEL_TYPE",
  "city":"FILTER_CITY_NAME",
  "city_id":"FILTER_CITY",
  "companion_creative":"FILTER_COMPANION_CREATIVE_NAME",
  "companion_creative_id":"FILTER_COMPANION_CREATIVE_ID",
  "companion_creative_size":"FILTER_COMPANION_CREATIVE_SIZE",
  "data_provider":"FILTER_DATA_PROVIDER_NAME",
  "data_provider_id":"FILTER_DATA_PROVIDER",
  "detailed_demographics":"FILTER_DETAILED_DEMOGRAPHICS",
  "detailed_demographics_id":"FILTER_DETAILED_DEMOGRAPHICS_ID",
  "device":"FILTER_DEVICE",
  "device_make":"FILTER_DEVICE_MAKE",
  "device_model":"FILTER_DEVICE_MODEL",
  "device_type":"FILTER_DEVICE_TYPE",
  "digital_content_label":"FILTER_DIGITAL_CONTENT_LABEL",
  "dma":"FILTER_DMA_NAME",
  "dma_code":"FILTER_DMA",
  "extension":"FILTER_EXTENSION",
  "extension_status":"FILTER_EXTENSION_STATUS",
  "extension_type":"FILTER_EXTENSION_TYPE",
  "format":"FILTER_FORMAT",
  "gmail_age":"FILTER_GMAIL_AGE",
  "gmail_city":"FILTER_GMAIL_CITY",
  "gmail_country":"FILTER_GMAIL_COUNTRY",
  "gmail_device_type":"FILTER_GMAIL_DEVICE_TYPE",
  "gmail_gender":"FILTER_GMAIL_GENDER",
  "gmail_region":"FILTER_GMAIL_REGION",
  "gmail_remarketing_list":"FILTER_GMAIL_REMARKETING_LIST",
  "household_income":"FILTER_HOUSEHOLD_INCOME",
  "impression_counting_method":"FILTER_IMPRESSION_COUNTING_METHOD",
  "insertion_order_daily_frequency":"FILTER_CAMPAIGN_DAILY_FREQUENCY",
  "interest":"FILTER_INTEREST",
  "inventory_commitment_type":"FILTER_INVENTORY_COMMITMENT_TYPE",
  "inventory_delivery_method":"FILTER_INVENTORY_DELIVERY_METHOD",
  "inventory_rate_type":"FILTER_INVENTORY_RATE_TYPE",
  "inventory_source_group":"FILTER_INVENTORY_SOURCE_GROUP",
  "inventory_source_group_id":"FILTER_INVENTORY_SOURCE_GROUP_ID",
  "inventory_source_id":"FILTER_INVENTORY_SOURCE_ID",
  "inventory_source_id_external":"FILTER_INVENTORY_SOURCE_EXTERNAL_ID",
  "inventory_source_type":"FILTER_INVENTORY_SOURCE_TYPE",
  "isp_or_carrier":"FILTER_CARRIER_NAME",
  "isp_or_carrier_id":"FILTER_CARRIER",
  "keyword":"FILTER_KEYWORD",
  "life_event":"FILTER_LIFE_EVENT",
  "life_events":"FILTER_LIFE_EVENTS",
  "line_item_daily_frequency":"FILTER_LINE_ITEM_DAILY_FREQUENCY",
  "line_item_lifetime_frequency":"FILTER_LINE_ITEM_LIFETIME_FREQUENCY",
  "max_video_duration":"FILTER_VIDEO_DURATION_SECONDS",
  "measurement_source":"FILTER_MEASUREMENT_SOURCE",
  "operating_system":"FILTER_OS",
  "platform":"FILTER_PLATFORM",
  "playback_method":"FILTER_PLAYBACK_METHOD",
  "position_in_content":"FILTER_POSITION_IN_CONTENT",
  "public_inventory":"FILTER_PUBLIC_INVENTORY",
  "publisher_property":"FILTER_PUBLISHER_PROPERTY",
  "publisher_property_id":"FILTER_PUBLISHER_PROPERTY_ID",
  "publisher_property_section":"FILTER_PUBLISHER_PROPERTY_SECTION",
  "publisher_property_section_id":"FILTER_PUBLISHER_PROPERTY_SECTION_ID",
  "refund_reason":"FILTER_REFUND_REASON",
  "region":"FILTER_REGION_NAME",
  "region_id":"FILTER_REGION",
  "rewarded":"FILTER_REWARDED",
  "sensitive_category":"FILTER_SENSITIVE_CATEGORY",
  "served_pixel_density":"FILTER_SERVED_PIXEL_DENSITY",
  "time_of_day":"FILTER_TIME_OF_DAY",
  "time_to_conversion":"FILTER_CONVERSION_DELAY",
  "variant_id":"FILTER_VARIANT_ID",
  "variant_name":"FILTER_VARIANT_NAME",
  "variant_version":"FILTER_VARIANT_VERSION",
  "verification_video_player_size":"FILTER_VERIFICATION_VIDEO_PLAYER_SIZE",
  "verification_video_position":"FILTER_VERIFICATION_VIDEO_POSITION",
  "video_continuous_play":"FILTER_VIDEO_CONTINUOUS_PLAY",
  "video_player_size":"FILTER_VIDEO_PLAYER_SIZE",
  "video_skippable_support":"FILTER_SKIPPABLE_SUPPORT",
  "week":"FILTER_WEEK",
  "zip_code":"FILTER_ZIP_POSTAL_CODE",
  "zip_code_id":"FILTER_ZIP_CODE",
  "age":"FILTER_AGE",
  "gender":"FILTER_GENDER",
  "potential_impressions":"METRIC_POTENTIAL_IMPRESSIONS",
  "unique_cookies_with_impressions":"METRIC_UNIQUE_COOKIES_WITH_IMPRESSIONS",
  "cm_post_click_revenue":"METRIC_CM_POST_CLICK_REVENUE",
  "cm_post_view_revenue":"METRIC_CM_POST_VIEW_REVENUE",
  "cookie_consented_floodlight_impressions":"METRIC_COOKIE_CONSENTED_FLOODLIGHT_IMPRESSIONS",
  "cookie_unconsented_floodlight_impressions":"METRIC_COOKIE_UNCONSENTED_FLOODLIGHT_IMPRESSIONS",
  "duplicate_floodlight_impressions":"METRIC_DUPLICATE_FLOODLIGHT_IMPRESSIONS",
  "floodlight_impressions":"METRIC_FLOODLIGHT_IMPRESSIONS",
  "post_click_conversions":"METRIC_LAST_CLICKS",
  "post_view_conversions":"METRIC_LAST_IMPRESSIONS",
  "total_conversions":"METRIC_TOTAL_CONVERSIONS",
  "cookie_reach_average_impression_frequency":"METRIC_COOKIE_REACH_AVERAGE_IMPRESSION_FREQUENCY",
  "cookie_reach_impression_reach":"METRIC_COOKIE_REACH_IMPRESSION_REACH",
  "unique_reach_average_impression_frequency":"METRIC_UNIQUE_REACH_AVERAGE_IMPRESSION_FREQUENCY",
  "unique_reach_click_reach":"METRIC_UNIQUE_REACH_CLICK_REACH",
  "unique_reach_impression_reach":"METRIC_UNIQUE_REACH_IMPRESSION_REACH",
  "unique_reach_total_reach":"METRIC_UNIQUE_REACH_TOTAL_REACH",
  "pct_clicks_leading_to_conversions":"METRIC_CLICK_TO_POST_CLICK_CONVERSION_RATE",
  "pct_impressions_leading_to_conversions":"METRIC_IMPRESSIONS_TO_CONVERSION_RATE",
  "pct_impressions_with_positive_custom_value":"METRIC_PERCENT_IMPRESSIONS_WITH_POSITIVE_CUSTOM_VALUE",
  "active_view_pct_audible_and_visible_at_completion":"METRIC_ACTIVE_VIEW_PERCENT_AUDIBLE_VISIBLE_ON_COMPLETE",
  "active_view_pct_audible_and_visible_at_first_quartile":"METRIC_ACTIVE_VIEW_PERCENT_AUDIBLE_VISIBLE_FIRST_QUAR",
  "active_view_pct_audible_and_visible_at_midpoint":"METRIC_ACTIVE_VIEW_PERCENT_AUDIBLE_VISIBLE_SECOND_QUAR",
  "active_view_pct_audible_and_visible_at_start":"METRIC_ACTIVE_VIEW_PERCENT_AUDIBLE_VISIBLE_AT_START",
  "active_view_pct_audible_and_visible_at_third_quartile":"METRIC_ACTIVE_VIEW_PERCENT_AUDIBLE_VISIBLE_THIRD_QUAR",
  "active_view_pct_audible_impressions":"METRIC_ACTIVE_VIEW_PERCENT_AUDIBLE_IMPRESSIONS",
  "active_view_pct_full_screen":"METRIC_ACTIVE_VIEW_PERCENT_FULL_SCREEN",
  "active_view_pct_fully_on_screen_2_sec":"METRIC_ACTIVE_VIEW_PERCENT_FULLY_ON_SCREEN_2_SEC",
  "active_view_pct_in_background":"METRIC_ACTIVE_VIEW_PERCENT_IN_BACKGROUND",
  "active_view_pct_measurable_impressions":"METRIC_ACTIVE_VIEW_PCT_MEASURABLE_IMPRESSIONS",
  "active_view_pct_of_ad_played":"METRIC_ACTIVE_VIEW_PERCENT_OF_AD_PLAYED",
  "active_view_pct_of_completed_impressions_audible_and_visible":"METRIC_ACTIVE_VIEW_PERCENT_OF_COMPLETED_IMPRESSIONS_AUDIBLE_AND_VISIBLE",
  "active_view_pct_of_completed_impressions_visible":"METRIC_ACTIVE_VIEW_PERCENT_OF_COMPLETED_IMPRESSIONS_VISIBLE",
  "active_view_pct_of_first_quartile_impressions_audible_and_visible":"METRIC_ACTIVE_VIEW_PERCENT_OF_FIRST_QUARTILE_IMPRESSIONS_AUDIBLE_AND_VISIBLE",
  "active_view_pct_of_first_quartile_impressions_visible":"METRIC_ACTIVE_VIEW_PERCENT_OF_FIRST_QUARTILE_IMPRESSIONS_VISIBLE",
  "active_view_pct_of_midpoint_impressions_audible_and_visible":"METRIC_ACTIVE_VIEW_PERCENT_OF_MIDPOINT_IMPRESSIONS_AUDIBLE_AND_VISIBLE",
  "active_view_pct_of_midpoint_impressions_visible":"METRIC_ACTIVE_VIEW_PERCENT_OF_MIDPOINT_IMPRESSIONS_VISIBLE",
  "active_view_pct_of_third_quartile_impressions_audible_and_visible":"METRIC_ACTIVE_VIEW_PERCENT_OF_THIRD_QUARTILE_IMPRESSIONS_AUDIBLE_AND_VISIBLE",
  "active_view_pct_of_third_quartile_impressions_visible":"METRIC_ACTIVE_VIEW_PERCENT_OF_THIRD_QUARTILE_IMPRESSIONS_VISIBLE",
  "active_view_pct_play_time_audible":"METRIC_ACTIVE_VIEW_PERCENT_PLAY_TIME_AUDIBLE",
  "active_view_pct_play_time_audible_and_visible":"METRIC_ACTIVE_VIEW_PERCENT_PLAY_TIME_AUDIBLE_AND_VISIBLE",
  "active_view_pct_play_time_visible":"METRIC_ACTIVE_VIEW_PERCENT_PLAY_TIME_VISIBLE",
  "active_view_pct_viewable_impressions":"METRIC_ACTIVE_VIEW_PCT_VIEWABLE_IMPRESSIONS",
  "active_view_pct_visible_10_seconds":"METRIC_ACTIVE_VIEW_PERCENT_VIEWABLE_FOR_TIME_THRESHOLD",
  "active_view_pct_visible_at_completion":"METRIC_ACTIVE_VIEW_PERCENT_VISIBLE_ON_COMPLETE",
  "active_view_pct_visible_at_first_quartile":"METRIC_ACTIVE_VIEW_PERCENT_VISIBLE_FIRST_QUAR",
  "active_view_pct_visible_at_midpoint":"METRIC_ACTIVE_VIEW_PERCENT_VISIBLE_SECOND_QUAR",
  "active_view_pct_visible_at_start":"METRIC_ACTIVE_VIEW_PERCENT_VISIBLE_AT_START",
  "active_view_pct_visible_at_third_quartile":"METRIC_ACTIVE_VIEW_PERCENT_VISIBLE_THIRD_QUAR",
  "active_view_audible_and_fully_on_screen_for_half_of_duration_15_sec_cap_impressions":"METRIC_ACTIVE_VIEW_AUDIBLE_FULLY_ON_SCREEN_HALF_OF_DURATION_IMPRESSIONS",
  "active_view_audible_and_fully_on_screen_for_half_of_duration_15_sec_cap_measurable_impressions":"METRIC_ACTIVE_VIEW_AUDIBLE_FULLY_ON_SCREEN_HALF_OF_DURATION_MEASURABLE_IMPRESSIONS",
  "active_view_audible_and_fully_on_screen_for_half_of_duration_15_sec_cap_rate":"METRIC_ACTIVE_VIEW_AUDIBLE_FULLY_ON_SCREEN_HALF_OF_DURATION_RATE",
  "active_view_audible_and_fully_on_screen_for_half_of_duration_trueview_impressions":"METRIC_ACTIVE_VIEW_AUDIBLE_FULLY_ON_SCREEN_HALF_OF_DURATION_TRUEVIEW_IMPRESSIONS",
  "active_view_audible_and_fully_on_screen_for_half_of_duration_trueview_measurable_impressions":"METRIC_ACTIVE_VIEW_AUDIBLE_FULLY_ON_SCREEN_HALF_OF_DURATION_TRUEVIEW_MEASURABLE_IMPRESSIONS",
  "active_view_audible_and_fully_on_screen_for_half_of_duration_trueview_rate":"METRIC_ACTIVE_VIEW_AUDIBLE_FULLY_ON_SCREEN_HALF_OF_DURATION_TRUEVIEW_RATE",
  "active_view_average_viewable_time_seconds":"METRIC_ACTIVE_VIEW_AVERAGE_VIEWABLE_TIME",
  "active_view_custom_metric_measurable_impressions":"METRIC_ACTIVE_VIEW_CUSTOM_METRIC_MEASURABLE_IMPRESSIONS",
  "active_view_custom_metric_viewable_impressions":"METRIC_ACTIVE_VIEW_CUSTOM_METRIC_VIEWABLE_IMPRESSIONS",
  "active_view_custom_metric_viewable_rate":"METRIC_ACTIVE_VIEW_CUSTOM_METRIC_VIEWABLE_RATE",
  "active_view_eligible_impressions":"METRIC_ACTIVE_VIEW_ELIGIBLE_IMPRESSIONS",
  "active_view_impression_distribution_not_measurable":"METRIC_ACTIVE_VIEW_DISTRIBUTION_UNMEASURABLE",
  "active_view_impression_distribution_not_viewable":"METRIC_ACTIVE_VIEW_DISTRIBUTION_UNVIEWABLE",
  "active_view_impression_distribution_viewable":"METRIC_ACTIVE_VIEW_DISTRIBUTION_VIEWABLE",
  "active_view_impressions_audible_and_visible_at_completion":"METRIC_ACTIVE_VIEW_AUDIBLE_VISIBLE_ON_COMPLETE_IMPRESSIONS",
  "active_view_impressions_visible_10_seconds":"METRIC_ACTIVE_VIEW_VIEWABLE_FOR_TIME_THRESHOLD",
  "active_view_measurable_impressions":"METRIC_ACTIVE_VIEW_MEASURABLE_IMPRESSIONS",
  "active_view_not_measurable_impressions":"METRIC_ACTIVE_VIEW_UNMEASURABLE_IMPRESSIONS",
  "active_view_not_viewable_impressions":"METRIC_ACTIVE_VIEW_UNVIEWABLE_IMPRESSIONS",
  "active_view_viewable_impressions":"METRIC_ACTIVE_VIEW_VIEWABLE_IMPRESSIONS",
  "adlingo_fee_advertiser_currency":"METRIC_ADLINGO_FEE_ADVERTISER_CURRENCY",
  "adloox_fee_advertiser_currency":"METRIC_FEE21_ADVERTISER",
  "adloox_fee_partner_currency":"METRIC_FEE21_PARTNER",
  "adloox_fee_usd":"METRIC_FEE21_USD",
  "adloox_pre_bid_fee_advertiser_currency":"METRIC_FEE22_ADVERTISER",
  "adloox_pre_bid_fee_partner_currency":"METRIC_FEE22_PARTNER",
  "adloox_pre_bid_fee_usd":"METRIC_FEE22_USD",
  "adsafe_fee_advertiser_currency":"METRIC_FEE4_ADVERTISER",
  "adsafe_fee_partner_currency":"METRIC_FEE4_PARTNER",
  "adsafe_fee_usd":"METRIC_FEE4_USD",
  "adxpose_fee_advertiser_currency":"METRIC_FEE5_ADVERTISER",
  "adxpose_fee_partner_currency":"METRIC_FEE5_PARTNER",
  "adxpose_fee_usd":"METRIC_FEE5_USD",
  "agency_trading_desk_fee_advertiser_currency":"METRIC_FEE10_ADVERTISER",
  "agency_trading_desk_fee_partner_currency":"METRIC_FEE10_PARTNER",
  "agency_trading_desk_fee_usd":"METRIC_FEE10_USD",
  "aggregate_knowledge_fee_advertiser_currency":"METRIC_FEE7_ADVERTISER",
  "aggregate_knowledge_fee_partner_currency":"METRIC_FEE7_PARTNER",
  "aggregate_knowledge_fee_usd":"METRIC_FEE7_USD",
  "audio_client_cost_ecpcl_advertiser_currency":"METRIC_AUDIO_CLIENT_COST_ECPCL_ADVERTISER_CURRENCY",
  "audio_media_cost_ecpcl_advertiser_currency":"METRIC_AUDIO_MEDIA_COST_ECPCL_ADVERTISER_CURRENCY",
  "audio_mutes_audio":"METRIC_AUDIO_MUTES_AUDIO",
  "audio_mutes_video":"METRIC_RICH_MEDIA_VIDEO_MUTES",
  "audio_revenue_ecpcl_advertiser_currency":"METRIC_AUDIO_REVENUE_ECPCL_ADVERTISER_CURRENCY",
  "audio_unmutes_audio":"METRIC_AUDIO_UNMUTES_AUDIO",
  "audio_unmutes_video":"METRIC_AUDIO_UNMUTES_VIDEO",
  "average_display_time":"METRIC_AVERAGE_DISPLAY_TIME",
  "average_interaction_time":"METRIC_AVERAGE_INTERACTION_TIME",
  "begin_to_render_eligible_impressions":"METRIC_BEGIN_TO_RENDER_ELIGIBLE_IMPRESSIONS",
  "begin_to_render_impressions":"METRIC_BEGIN_TO_RENDER_IMPRESSIONS",
  "billable_cost_advertiser_currency":"METRIC_BILLABLE_COST_ADVERTISER",
  "billable_cost_partner_currency":"METRIC_BILLABLE_COST_PARTNER",
  "billable_cost_usd":"METRIC_BILLABLE_COST_USD",
  "billable_impressions":"METRIC_BILLABLE_IMPRESSIONS",
  "click_rate_ctr":"METRIC_CTR",
  "clicks":"METRIC_CLICKS",
  "client_cost_advertiser_currency":"METRIC_CLIENT_COST_ADVERTISER_CURRENCY",
  "client_cost_ecpa_advertiser_currency":"METRIC_CLIENT_COST_ECPA_ADVERTISER_CURRENCY",
  "client_cost_ecpa_pc_advertiser_currency":"METRIC_CLIENT_COST_ECPA_PC_ADVERTISER_CURRENCY",
  "client_cost_ecpa_pv_advertiser_currency":"METRIC_CLIENT_COST_ECPA_PV_ADVERTISER_CURRENCY",
  "client_cost_ecpc_advertiser_currency":"METRIC_CLIENT_COST_ECPC_ADVERTISER_CURRENCY",
  "client_cost_ecpm_advertiser_currency":"METRIC_CLIENT_COST_ECPM_ADVERTISER_CURRENCY",
  "client_cost_viewable_ecpm_advertiser_currency":"METRIC_CLIENT_COST_VIEWABLE_ECPM_ADVERTISER_CURRENCY",
  "cm_post_click_revenue__cross_environment":"METRIC_CM_POST_CLICK_REVENUE_CROSS_ENVIRONMENT",
  "cm_post_view_revenue__cross_environment":"METRIC_CM_POST_VIEW_REVENUE_CROSS_ENVIRONMENT",
  "companion_clicks_audio":"METRIC_COMPANION_CLICKS_AUDIO",
  "companion_clicks_video":"METRIC_VIDEO_COMPANION_CLICKS",
  "companion_impressions_audio":"METRIC_COMPANION_IMPRESSIONS_AUDIO",
  "companion_impressions_video":"METRIC_VIDEO_COMPANION_IMPRESSIONS",
  "complete_listens_audio":"METRIC_COMPLETE_LISTENS_AUDIO",
  "complete_views_video":"METRIC_RICH_MEDIA_VIDEO_COMPLETIONS",
  "completion_rate_audio":"METRIC_COMPLETION_RATE_AUDIO",
  "completion_rate_video":"METRIC_VIDEO_COMPLETION_RATE",
  "comscore_vce_in_doubleclick_fee_advertiser_currency":"METRIC_FEE20_ADVERTISER",
  "comscore_vce_in_doubleclick_fee_partner_currency":"METRIC_FEE20_PARTNER",
  "comscore_vce_in_doubleclick_fee_usd":"METRIC_FEE20_USD",
  "conversions_per_1000_impressions":"METRIC_CONVERSIONS_PER_MILLE",
  "cookie_unconsented_clicks":"METRIC_TRACKING_UNCONSENTED_CLICKS",
  "counters":"METRIC_COUNTERS",
  "cpm_fee_1_advertiser_currency":"METRIC_CPM_FEE1_ADVERTISER",
  "cpm_fee_1_partner_currency":"METRIC_CPM_FEE1_PARTNER",
  "cpm_fee_1_usd":"METRIC_CPM_FEE1_USD",
  "cpm_fee_2_advertiser_currency":"METRIC_CPM_FEE2_ADVERTISER",
  "cpm_fee_2_partner_currency":"METRIC_CPM_FEE2_PARTNER",
  "cpm_fee_2_usd":"METRIC_CPM_FEE2_USD",
  "cpm_fee_3_advertiser_currency":"METRIC_CPM_FEE3_ADVERTISER",
  "cpm_fee_3_partner_currency":"METRIC_CPM_FEE3_PARTNER",
  "cpm_fee_3_usd":"METRIC_CPM_FEE3_USD",
  "cpm_fee_4_advertiser_currency":"METRIC_CPM_FEE4_ADVERTISER",
  "cpm_fee_4_partner_currency":"METRIC_CPM_FEE4_PARTNER",
  "cpm_fee_4_usd":"METRIC_CPM_FEE4_USD",
  "cpm_fee_5_advertiser_currency":"METRIC_CPM_FEE5_ADVERTISER",
  "cpm_fee_5_partner_currency":"METRIC_CPM_FEE5_PARTNER",
  "cpm_fee_5_usd":"METRIC_CPM_FEE5_USD",
  "custom_fee_1_advertiser_currency":"METRIC_CUSTOM_FEE_1_ADVERTISER_CURRENCY",
  "custom_fee_2_advertiser_currency":"METRIC_CUSTOM_FEE_2_ADVERTISER_CURRENCY",
  "custom_fee_3_advertiser_currency":"METRIC_CUSTOM_FEE_3_ADVERTISER_CURRENCY",
  "custom_fee_4_advertiser_currency":"METRIC_CUSTOM_FEE_4_ADVERTISER_CURRENCY",
  "custom_fee_5_advertiser_currency":"METRIC_CUSTOM_FEE_5_ADVERTISER_CURRENCY",
  "data_fees_advertiser_currency":"METRIC_DATA_COST_ADVERTISER",
  "data_fees_partner_currency":"METRIC_DATA_COST_PARTNER",
  "data_fees_usd":"METRIC_DATA_COST_USD",
  "data_management_platform_fee_advertiser_currency":"METRIC_FEE11_ADVERTISER",
  "data_management_platform_fee_partner_currency":"METRIC_FEE11_PARTNER",
  "data_management_platform_fee_usd":"METRIC_FEE11_USD",
  "doubleverify_fee_advertiser_currency":"METRIC_FEE3_ADVERTISER",
  "doubleverify_fee_partner_currency":"METRIC_FEE3_PARTNER",
  "doubleverify_fee_usd":"METRIC_FEE3_USD",
  "doubleverify_pre_bid_fee_advertiser_currency":"METRIC_FEE13_ADVERTISER",
  "doubleverify_pre_bid_fee_partner_currency":"METRIC_FEE13_PARTNER",
  "doubleverify_pre_bid_fee_usd":"METRIC_FEE13_USD",
  "engagement_rate":"METRIC_DBM_ENGAGEMENT_RATE",
  "engagements":"METRIC_ENGAGEMENTS",
  "estimated_cpm_for_impressions_with_custom_value_advertiser_currency":"METRIC_ESTIMATED_CPM_FOR_IMPRESSIONS_WITH_CUSTOM_VALUE_ADVERTISER_CURRENCY",
  "estimated_total_cost_for_impressions_with_custom_value_advertiser_currency":"METRIC_ESTIMATED_TOTAL_COST_FOR_IMPRESSIONS_WITH_CUSTOM_VALUE_ADVERTISER_CURRENCY",
  "evidon_fee_advertiser_currency":"METRIC_FEE9_ADVERTISER",
  "evidon_fee_partner_currency":"METRIC_FEE9_PARTNER",
  "evidon_fee_usd":"METRIC_FEE9_USD",
  "exits":"METRIC_EXITS",
  "expansions":"METRIC_EXPANSIONS",
  "first_quartile_audio":"METRIC_FIRST_QUARTILE_AUDIO",
  "first_quartile_views_video":"METRIC_RICH_MEDIA_VIDEO_FIRST_QUARTILE_COMPLETES",
  "fullscreens_video":"METRIC_RICH_MEDIA_VIDEO_FULL_SCREENS",
  "general_invalid_traffic_givt_active_view_eligible_impressions":"METRIC_GIVT_ACTIVE_VIEW_ELIGIBLE_IMPRESSIONS",
  "general_invalid_traffic_givt_active_view_measurable_impressions":"METRIC_GIVT_ACTIVE_VIEW_MEASURABLE_IMPRESSIONS",
  "general_invalid_traffic_givt_active_view_viewable_impressions":"METRIC_GIVT_ACTIVE_VIEW_VIEWABLE_IMPRESSIONS",
  "general_invalid_traffic_givt_begin_to_render_impressions":"METRIC_GIVT_BEGIN_TO_RENDER_IMPRESSIONS",
  "general_invalid_traffic_givt_clicks":"METRIC_GIVT_CLICKS",
  "general_invalid_traffic_givt_impressions":"METRIC_GENERAL_INVALID_TRAFFIC_GIVT_IMPRESSIONS",
  "general_invalid_traffic_givt_tracked_ads":"METRIC_GENERAL_INVALID_TRAFFIC_GIVT_TRACKED_ADS",
  "gmail_conversions":"METRIC_GMAIL_CONVERSIONS",
  "gmail_post_click_conversions":"METRIC_GMAIL_POST_CLICK_CONVERSIONS",
  "gmail_post_view_conversions":"METRIC_GMAIL_POST_VIEW_CONVERSIONS",
  "impression_custom_value_cost":"METRIC_IMPRESSION_CUSTOM_VALUE_COST",
  "impressions":"METRIC_IMPRESSIONS",
  "impressions_with_custom_value":"METRIC_IMPRESSIONS_WITH_CUSTOM_VALUE",
  "impressions_with_positive_custom_value":"METRIC_IMPRESSIONS_WITH_POSITIVE_CUSTOM_VALUE",
  "integral_ad_science_pre_bid_fee_advertiser_currency":"METRIC_FEE12_ADVERTISER",
  "integral_ad_science_pre_bid_fee_partner_currency":"METRIC_FEE12_PARTNER",
  "integral_ad_science_pre_bid_fee_usd":"METRIC_FEE12_USD",
  "integral_ad_science_video_fee_advertiser_currency":"METRIC_FEE17_ADVERTISER",
  "integral_ad_science_video_fee_partner_currency":"METRIC_FEE17_PARTNER",
  "integral_ad_science_video_fee_usd":"METRIC_FEE17_USD",
  "interactive_impressions":"METRIC_INTERACTIVE_IMPRESSIONS",
  "invalid_active_view_eligible_impressions":"METRIC_INVALID_ACTIVE_VIEW_ELIGIBLE_IMPRESSIONS",
  "invalid_active_view_measurable_impressions":"METRIC_INVALID_ACTIVE_VIEW_MEASURABLE_IMPRESSIONS",
  "invalid_active_view_viewable_impressions":"METRIC_INVALID_ACTIVE_VIEW_VIEWABLE_IMPRESSIONS",
  "invalid_begin_to_render_impressions":"METRIC_INVALID_BEGIN_TO_RENDER_IMPRESSIONS",
  "invalid_clicks":"METRIC_INVALID_CLICKS",
  "invalid_impressions":"METRIC_INVALID_IMPRESSIONS",
  "invalid_tracked_ads":"METRIC_INVALID_TRACKED_ADS",
  "media_cost_advertiser_currency":"METRIC_MEDIA_COST_ADVERTISER",
  "media_cost_partner_currency":"METRIC_MEDIA_COST_PARTNER",
  "media_cost_usd":"METRIC_MEDIA_COST_USD",
  "media_cost_ecpa_advertiser_currency":"METRIC_MEDIA_COST_ECPA_ADVERTISER",
  "media_cost_ecpa_partner_currency":"METRIC_MEDIA_COST_ECPA_PARTNER",
  "media_cost_ecpa_pc_advertiser_currency":"METRIC_MEDIA_COST_ECPAPC_ADVERTISER",
  "media_cost_ecpa_pv_advertiser_currency":"METRIC_MEDIA_COST_ECPAPV_ADVERTISER",
  "media_cost_ecpa_usd":"METRIC_MEDIA_COST_ECPA_USD",
  "media_cost_ecpc_advertiser_currency":"METRIC_MEDIA_COST_ECPC_ADVERTISER",
  "media_cost_ecpc_partner_currency":"METRIC_MEDIA_COST_ECPC_PARTNER",
  "media_cost_ecpc_pc_partner_currency":"METRIC_MEDIA_COST_ECPAPC_PARTNER",
  "media_cost_ecpc_pc_usd":"METRIC_MEDIA_COST_ECPAPC_USD",
  "media_cost_ecpc_pv_partner_currency":"METRIC_MEDIA_COST_ECPAPV_PARTNER",
  "media_cost_ecpc_pv_usd":"METRIC_MEDIA_COST_ECPAPV_USD",
  "media_cost_ecpc_usd":"METRIC_MEDIA_COST_ECPC_USD",
  "media_cost_ecpm_advertiser_currency":"METRIC_MEDIA_COST_ECPM_ADVERTISER",
  "media_cost_ecpm_partner_currency":"METRIC_MEDIA_COST_ECPM_PARTNER",
  "media_cost_ecpm_usd":"METRIC_MEDIA_COST_ECPM_USD",
  "media_cost_viewable_ecpm_advertiser_currency":"METRIC_MEDIA_COST_VIEWABLE_ECPM_ADVERTISER",
  "media_cost_viewable_ecpm_partner_currency":"METRIC_MEDIA_COST_VIEWABLE_ECPM_PARTNER",
  "media_cost_viewable_ecpm_usd":"METRIC_MEDIA_COST_VIEWABLE_ECPM_USD",
  "media_fee_1_advertiser_currency":"METRIC_MEDIA_FEE1_ADVERTISER",
  "media_fee_1_partner_currency":"METRIC_MEDIA_FEE1_PARTNER",
  "media_fee_1_usd":"METRIC_MEDIA_FEE1_USD",
  "media_fee_2_advertiser_currency":"METRIC_MEDIA_FEE2_ADVERTISER",
  "media_fee_2_partner_currency":"METRIC_MEDIA_FEE2_PARTNER",
  "media_fee_2_usd":"METRIC_MEDIA_FEE2_USD",
  "media_fee_3_advertiser_currency":"METRIC_MEDIA_FEE3_ADVERTISER",
  "media_fee_3_partner_currency":"METRIC_MEDIA_FEE3_PARTNER",
  "media_fee_3_usd":"METRIC_MEDIA_FEE3_USD",
  "media_fee_4_advertiser_currency":"METRIC_MEDIA_FEE4_ADVERTISER",
  "media_fee_4_partner_currency":"METRIC_MEDIA_FEE4_PARTNER",
  "media_fee_4_usd":"METRIC_MEDIA_FEE4_USD",
  "media_fee_5_advertiser_currency":"METRIC_MEDIA_FEE5_ADVERTISER",
  "media_fee_5_partner_currency":"METRIC_MEDIA_FEE5_PARTNER",
  "media_fee_5_usd":"METRIC_MEDIA_FEE5_USD",
  "mediacost_data_fee_advertiser_currency":"METRIC_FEE16_ADVERTISER",
  "mediacost_data_fee_partner_currency":"METRIC_FEE16_PARTNER",
  "mediacost_data_fee_usd":"METRIC_FEE16_USD",
  "midpoint_audio":"METRIC_MIDPOINT_AUDIO",
  "midpoint_views_video":"METRIC_RICH_MEDIA_VIDEO_MIDPOINTS",
  "moat_video_fee_advertiser_currency":"METRIC_FEE18_ADVERTISER",
  "moat_video_fee_partner_currency":"METRIC_FEE18_PARTNER",
  "moat_video_fee_usd":"METRIC_FEE18_USD",
  "nielsen_digital_ad_ratings_fee_advertiser_currency":"METRIC_FEE19_ADVERTISER",
  "nielsen_digital_ad_ratings_fee_partner_currency":"METRIC_FEE19_PARTNER",
  "nielsen_digital_ad_ratings_fee_usd":"METRIC_FEE19_USD",
  "pauses_audio":"METRIC_PAUSES_AUDIO",
  "pauses_video":"METRIC_RICH_MEDIA_VIDEO_PAUSES",
  "platform_fee_advertiser_currency":"METRIC_PLATFORM_FEE_ADVERTISER",
  "platform_fee_partner_currency":"METRIC_PLATFORM_FEE_PARTNER",
  "platform_fee_usd":"METRIC_PLATFORM_FEE_USD",
  "platform_fee_rate":"METRIC_PLATFORM_FEE_RATE",
  "post_view_conversions__cross_environment":"METRIC_POST_VIEW_CONVERSIONS_CROSS_ENVIRONMENT",
  "premium_fee_advertiser_currency":"METRIC_PREMIUM_FEE_ADVERTISER_CURRENCY",
  "profit_advertiser_currency":"METRIC_PROFIT_ADVERTISER",
  "profit_partner_currency":"METRIC_PROFIT_PARTNER",
  "profit_usd":"METRIC_PROFIT_USD",
  "profit_ecpm_advertiser_currency":"METRIC_PROFIT_ECPM_ADVERTISER",
  "profit_ecpm_partner_currency":"METRIC_PROFIT_ECPM_PARTNER",
  "profit_ecpm_usd":"METRIC_PROFIT_ECPM_USD",
  "profit_margin":"METRIC_PROFIT_MARGIN",
  "profit_viewable_ecpm_advertiser_currency":"METRIC_PROFIT_VIEWABLE_ECPM_ADVERTISER",
  "profit_viewable_ecpm_partner_currency":"METRIC_PROFIT_VIEWABLE_ECPM_PARTNER",
  "profit_viewable_ecpm_usd":"METRIC_PROFIT_VIEWABLE_ECPM_USD",
  "programmatic_guaranteed_impressions_passed_due_to_frequency":"METRIC_PROGRAMMATIC_GUARANTEED_IMPRESSIONS_PASSED_DUE_TO_FREQUENCY",
  "programmatic_guaranteed_savings_re_invested_due_to_frequency_advertiser_currency":"METRIC_PROGRAMMATIC_GUARANTEED_SAVINGS_RE_INVESTED_DUE_TO_FREQUENCY_ADVERTISER_CURRENCY",
  "refund_billable_cost_advertiser_currency":"METRIC_REFUND_BILLABLE_COST_ADVERTISER_CURRENCY",
  "refund_media_cost_advertiser_currency":"METRIC_REFUND_MEDIA_COST_ADVERTISER_CURRENCY",
  "refund_platform_fee_advertiser_currency":"METRIC_REFUND_PLATFORM_FEE_ADVERTISER_CURRENCY",
  "revenue_advertiser_currency":"METRIC_REVENUE_ADVERTISER",
  "revenue_partner_currency":"METRIC_REVENUE_PARTNER",
  "revenue_usd":"METRIC_REVENUE_USD",
  "revenue_ecpa_advertiser_currency":"METRIC_REVENUE_ECPA_ADVERTISER",
  "revenue_ecpa_partner_currency":"METRIC_REVENUE_ECPA_PARTNER",
  "revenue_ecpa_pc_advertiser_currency":"METRIC_REVENUE_ECPAPC_ADVERTISER",
  "revenue_ecpa_pc_partner_currency":"METRIC_REVENUE_ECPAPC_PARTNER",
  "revenue_ecpa_pc_usd":"METRIC_REVENUE_ECPAPC_USD",
  "revenue_ecpa_pv_advertiser_currency":"METRIC_REVENUE_ECPAPV_ADVERTISER",
  "revenue_ecpa_pv_partner_currency":"METRIC_REVENUE_ECPAPV_PARTNER",
  "revenue_ecpa_pv_usd":"METRIC_REVENUE_ECPAPV_USD",
  "revenue_ecpa_usd":"METRIC_REVENUE_ECPA_USD",
  "revenue_ecpc_advertiser_currency":"METRIC_REVENUE_ECPC_ADVERTISER",
  "revenue_ecpc_partner_currency":"METRIC_REVENUE_ECPC_PARTNER",
  "revenue_ecpc_usd":"METRIC_REVENUE_ECPC_USD",
  "revenue_ecpe_advertiser_currency":"METRIC_TRUEVIEW_AVERAGE_CPE_ADVERTISER",
  "revenue_ecpe_partner_currency":"METRIC_TRUEVIEW_AVERAGE_CPE_PARTNER",
  "revenue_ecpe_usd":"METRIC_TRUEVIEW_AVERAGE_CPE_USD",
  "revenue_ecpm_advertiser_currency":"METRIC_REVENUE_ECPM_ADVERTISER",
  "revenue_ecpm_partner_currency":"METRIC_REVENUE_ECPM_PARTNER",
  "revenue_ecpm_usd":"METRIC_REVENUE_ECPM_USD",
  "revenue_ecpv_advertiser_currency":"METRIC_TRUEVIEW_CPV_ADVERTISER",
  "revenue_ecpv_partner_currency":"METRIC_TRUEVIEW_CPV_PARTNER",
  "revenue_ecpv_usd":"METRIC_TRUEVIEW_CPV_USD",
  "revenue_viewable_ecpm_advertiser_currency":"METRIC_REVENUE_VIEWABLE_ECPM_ADVERTISER",
  "revenue_viewable_ecpm_partner_currency":"METRIC_REVENUE_VIEWABLE_ECPM_PARTNER",
  "revenue_viewable_ecpm_usd":"METRIC_REVENUE_VIEWABLE_ECPM_USD",
  "rich_media_engagements":"METRIC_RICH_MEDIA_ENGAGEMENTS",
  "scrolls":"METRIC_RICH_MEDIA_SCROLLS",
  "shoplocal_fee_advertiser_currency":"METRIC_FEE14_ADVERTISER",
  "shoplocal_fee_partner_currency":"METRIC_FEE14_PARTNER",
  "shoplocal_fee_usd":"METRIC_FEE14_USD",
  "skips_video":"METRIC_RICH_MEDIA_VIDEO_SKIPS",
  "starts_audio":"METRIC_STARTS_AUDIO",
  "starts_video":"METRIC_RICH_MEDIA_VIDEO_PLAYS",
  "stops_audio":"METRIC_STOPS_AUDIO",
  "teracent_fee_advertiser_currency":"METRIC_FEE8_ADVERTISER",
  "teracent_fee_partner_currency":"METRIC_FEE8_PARTNER",
  "teracent_fee_usd":"METRIC_FEE8_USD",
  "third_party_ad_server_fee_advertiser_currency":"METRIC_FEE2_ADVERTISER",
  "third_party_ad_server_fee_partner_currency":"METRIC_FEE2_PARTNER",
  "third_party_ad_server_fee_usd":"METRIC_FEE2_USD",
  "third_quartile_audio":"METRIC_THIRD_QUARTILE_AUDIO",
  "third_quartile_views_video":"METRIC_RICH_MEDIA_VIDEO_THIRD_QUARTILE_COMPLETES",
  "timers":"METRIC_TIMERS",
  "total_conversions__cross_environment":"METRIC_TOTAL_CONVERSIONS_CROSS_ENVIRONMENT",
  "total_display_time":"METRIC_TOTAL_DISPLAY_TIME",
  "total_impression_custom_value":"METRIC_TOTAL_IMPRESSION_CUSTOM_VALUE",
  "total_interaction_time":"METRIC_TOTAL_INTERACTION_TIME",
  "total_media_cost_advertiser_currency":"METRIC_TOTAL_MEDIA_COST_ADVERTISER",
  "total_media_cost_partner_currency":"METRIC_TOTAL_MEDIA_COST_PARTNER",
  "total_media_cost_usd":"METRIC_TOTAL_MEDIA_COST_USD",
  "total_media_cost_ecpa_advertiser_currency":"METRIC_TOTAL_MEDIA_COST_ECPA_ADVERTISER",
  "total_media_cost_ecpa_partner_currency":"METRIC_TOTAL_MEDIA_COST_ECPA_PARTNER",
  "total_media_cost_ecpa_pc_advertiser_currency":"METRIC_TOTAL_MEDIA_COST_ECPAPC_ADVERTISER",
  "total_media_cost_ecpa_pc_partner_currency":"METRIC_TOTAL_MEDIA_COST_ECPAPC_PARTNER",
  "total_media_cost_ecpa_pc_usd":"METRIC_TOTAL_MEDIA_COST_ECPAPC_USD",
  "total_media_cost_ecpa_pv_advertiser_currency":"METRIC_TOTAL_MEDIA_COST_ECPAPV_ADVERTISER",
  "total_media_cost_ecpa_pv_partner_currency":"METRIC_TOTAL_MEDIA_COST_ECPAPV_PARTNER",
  "total_media_cost_ecpa_pv_usd":"METRIC_TOTAL_MEDIA_COST_ECPAPV_USD",
  "total_media_cost_ecpa_usd":"METRIC_TOTAL_MEDIA_COST_ECPA_USD",
  "total_media_cost_ecpc_advertiser_currency":"METRIC_TOTAL_MEDIA_COST_ECPC_ADVERTISER",
  "total_media_cost_ecpc_partner_currency":"METRIC_TOTAL_MEDIA_COST_ECPC_PARTNER",
  "total_media_cost_ecpc_usd":"METRIC_TOTAL_MEDIA_COST_ECPC_USD",
  "total_media_cost_ecpm_advertiser_currency":"METRIC_TOTAL_MEDIA_COST_ECPM_ADVERTISER",
  "total_media_cost_ecpm_partner_currency":"METRIC_TOTAL_MEDIA_COST_ECPM_PARTNER",
  "total_media_cost_ecpm_usd":"METRIC_TOTAL_MEDIA_COST_ECPM_USD",
  "total_media_cost_viewable_ecpm_advertiser_currency":"METRIC_TOTAL_MEDIA_COST_VIEWABLE_ECPM_ADVERTISER",
  "total_media_cost_viewable_ecpm_partner_currency":"METRIC_TOTAL_MEDIA_COST_VIEWABLE_ECPM_PARTNER",
  "total_media_cost_viewable_ecpm_usd":"METRIC_TOTAL_MEDIA_COST_VIEWABLE_ECPM_USD",
  "total_video_media_cost_ecpcv_advertiser_currency":"METRIC_TOTAL_MEDIA_COST_ECPCV_ADVERTISER",
  "total_video_media_cost_ecpcv_partner_currency":"METRIC_TOTAL_MEDIA_COST_ECPCV_PARTNER",
  "total_video_media_cost_ecpcv_usd":"METRIC_TOTAL_MEDIA_COST_ECPCV_USD",
  "tracked_ads":"METRIC_TRACKED_ADS",
  "trueview_general_invalid_traffic_givt_views":"METRIC_TRUEVIEW_GENERAL_INVALID_TRAFFIC_GIVT_VIEWS",
  "trueview_invalid_views":"METRIC_TRUEVIEW_INVALID_VIEWS",
  "trustmetrics_fee_advertiser_currency":"METRIC_FEE15_ADVERTISER",
  "trustmetrics_fee_partner_currency":"METRIC_FEE15_PARTNER",
  "trustmetrics_fee_usd":"METRIC_FEE15_USD",
  "verifiable_impressions":"METRIC_VERIFIABLE_IMPRESSIONS",
  "video_client_cost_ecpcv_advertiser_currency":"METRIC_VIDEO_CLIENT_COST_ECPCV_ADVERTISER_CURRENCY",
  "video_media_cost_ecpcv_advertiser_currency":"METRIC_MEDIA_COST_ECPCV_ADVERTISER",
  "video_media_cost_ecpcv_partner_currency":"METRIC_MEDIA_COST_ECPCV_PARTNER",
  "video_media_cost_ecpcv_usd":"METRIC_MEDIA_COST_ECPCV_USD",
  "vizu_fee_advertiser_currency":"METRIC_FEE6_ADVERTISER",
  "vizu_fee_partner_currency":"METRIC_FEE6_PARTNER",
  "vizu_fee_usd":"METRIC_FEE6_USD",
  "youtube_view_rate":"METRIC_TRUEVIEW_VIEW_RATE",
  "youtube_views":"METRIC_TRUEVIEW_VIEWS",
  "pct_composition_impressions":"METRIC_DEMO_COMPOSITION_IMPRESSION",
  "pct_composition_reach":"METRIC_VIRTUAL_PEOPLE_IMPRESSION_REACH_SHARE_PERCENT",
  "pct_population_reach":"METRIC_VIRTUAL_PEOPLE_IMPRESSION_REACH_PERCENT",
  "population":"METRIC_DEMO_POPULATION",
  "target_rating_points":"METRIC_TARGET_RATING_POINTS",
  "unique_reach_viewable_impression_reach":"METRIC_VIRTUAL_PEOPLE_VIEWABLE_IMPRESSION_REACH_BY_DEMO",
  "viewable_target_rating_points":"METRIC_VIEWABLE_GROSS_RATING_POINTS",
  "viewable_impressions":"METRIC_GRP_CORRECTED_VIEWABLE_IMPRESSIONS",
  "pct_viewable_composition_impressions":"METRIC_GRP_CORRECTED_VIEWABLE_IMPRESSIONS_SHARE_PERCENT",
  "pct_viewable_composition_reach":"METRIC_VIRTUAL_PEOPLE_VIEWABLE_IMPRESSION_REACH_SHARE_PERCENT",
  "pct_viewable_population_reach":"METRIC_VIRTUAL_PEOPLE_VIEWABLE_IMPRESSION_REACH_PERCENT",
}