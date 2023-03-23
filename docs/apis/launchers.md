# Launchers

**A Launcher is a collection of items shown in a menu to your end-users when they meet all of the predefined matching criteria**

 - **The current page URL matches.**
 - **Segmentation matches (User is the right person) - required but can be to match All Users.**
 - **Launcher menu Icon or Custom Icon must be clicked.**



*To know more about Launchers, feel free to visit our [product documentation](https://help.chameleon.io/en/collections/1587145-launchers).*

---



With the Chameleon API for Launchers, you can:

- List all Launchers based on the specified set of parameters.
- Retrieve a specific Launcher based on its `id`.



## Schema :id=schema

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated |
| `name` | string | The name given by an administrator of Chameleon |
| `title` | string | The display title |
| `description` | string | The display description |
| `preset` | string | The preconfigured type: One of `icon`, `element`, `icon_checklist`, `updates`, or `faqs` |
| `segment_id` | ID | The Chameleon ID of the configured [Segment](apis/segments.md?id=schema) |
| `published_at` | timestamp | The time this was most recently published |
| `tag_ids` | array&lt;ID&gt; | The Chameleon IDs of the [Tags](apis/tags.md) attached to this model |
| `list_type` | string | If this is a checklist or a normal list: One of `default` or `checklist` |
| `search_placeholder` | string | Search placeholder |
| `quantifier_url` | string | This must match the current page URL _[deprecated]_ |
| `quantifier_urls` | array | List of URL matching conditions that must match the current page URL |
| `quantifier_urls.url` | none | The specific URL used in this matching condition |
| `quantifier_urls.match_type` | none | The type of matching used. One of: `simple`, `exact`, `regex`, `inverse_simple`, or `inverse_exact` |
| `trigger_text` | string | Trigger text |
| `blocked_domains` | string | Domains that, if matched, will make this now show |
| `empty_state_content` | string | Markdown content to show when all items in the Launcher are completed/hidden |
| `icon_size` | string | Icon size |
| `screen_position` | string | Screen position: One of `bottom_left` or `bottom_right` |
| `position_type` | string | Position type: One of `relative_to_screen` or `snap_to_element` |
| `trigger` | string | Trigger: One of `click` or `hover` |
| `trigger_type` | string | Trigger type: One of `custom_icon`, `element`, `icon_lightbulb`, `icon_question`, `icon_checklist`, `icon_signpost`, `icon_bell`, or `text` |
| `items` | array&lt;LauncherItem&gt; | An array of items that define the Launcher menu contents (see full schema below) |
| `stats` | object | Aggregated statistics for this model (all-time) |
| `stats.displayed_count` | number | Number of times the Launcher widget (icon) was shown to end-users |
| `stats.last_displayed_at` | timestamp | Most recent time the Launcher widget (icon) was shown to end-users |
| `stats.started_count` | number | Number of times the Launcher menu was opened by an end-user |
| `stats.last_started_at` | timestamp | Most recent time the Launcher menu was opened by an end-user |

## Launcher Item Schema :id=item-schema

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated |
| `kind` | string | The type of item this is: One of `url`, `tour`, `survey`, `script`, or `divider` |
| `title` | string | The display title in the Launcher menu |
| `description` | string | The display description in the Launcher menu |
| `segment_id` | ID | The Chameleon ID of the configured [Segment](apis/segments.md?id=schema) |
| `url` | string | The URL to link to when `kind=url |
| `campaign_id` | ID | The Chameleon ID of the [Tour](apis/tours.md) or [Microsurvey](apis/surveys.md) referenced when `kind=tour` or `kind=survey` |
| `script` | string | The JavaScript code snippet to execute when this item is clicked by your end-user |
| `hide` | boolean | Whether or not to remove this item from the list after clicked/completed |

## List Launchers :id=launchers-index

List all Launchers based on the specified set of parameters.

#### HTTP Request

```
GET https://api.chameleon.io/v3/edit/launchers
```

| param  | -        | description                                                  |
| ------ | -------- | ------------------------------------------------------------ |
| `limit`  | optional | Defaults to `50` with a maximum of `500`                     |
| `before` | optional | Used when paginating, use directly from the `cursor` object from the previous response |
| `before` | optional | Read as "created `before`" and can be given as a timestamp to get only `limit` items that were created before this time |
| `after`  | optional | Read as "created `after`" and can be given as a timestamp or ID to get only `limit` items that were created after this time |

#### HTTP Response

```json
{
  "launchers": [
    {
      "id": "5f3c4232c712de665632a6d5",
      "name": "Admin Onboarding checklist",
      "position": 1,
      "published_at": "2029-04-07T12:18:00Z",
       ...
    },
    {
      "id": "5f3c4232c712de665632a2a1",
      "name": "Admin Self-serve menu",
      "position": 0,
      "published_at": "2029-04-07T12:38:00Z",
       ...
    },
    ...
  ],
  "cursor": {
    "limit": 50,
    "before": "5f3c4232c712de665632a2a1"
  }
}
```

## Filtering by Segment :id=filter-segment

See [Listing Related models](apis/segments.md?id=segment-experiences-index)

## Retrieve a Launcher :id=launchers-show

Retrieve a single Launcher.

#### HTTP Request

```
GET https://api.chameleon.io/v3/edit/launchers/:id
```

| param | - | description |
|---|---|---|
| `id` | required | A Launcher ID to lookup

```json
{
  "launcher": {
    "id": "5f3c4232c712de665632a2a1",
    "name": "Admin Self-serve menu",
    "position": 0,
    "published_at": "2029-04-07T12:38:00Z",
    ...
  }
}
```
