# HelpBar

**Add a HelpBar to your product that allows your Users to search your Help center, Product, and any custom content. This allows for a straightforward implementation of federated search (i.e. search of all your content).**

> **You have content within your product, even if you don't think of it that way. Any database records that your Users would want to find is a piece of content, akin to a Google search result. Send this content to Chameleon and we will surface it to your Users in the Chameleon HelpBar. The content can be scoped to a specific [Company](apis/company.md), be pinned to the top when the HelpBar is opened and can perform any action from clicking an item.**.

------

See the specific APIs for more information on how to use Search your product.

 - [REST API](apis/search.md?id=search-rest-api)
 - [JavaScript API](apis/search.md?id=search-js-api)
 - [Limits](apis/search.md?id=limits)


#### To get HelpBar up and running, complete these items:

1. Create a [HelpBar](apis/search.md?id=schema), configure it with `placeholder` etc.
2. Add your Help center as a [`SearchGroup`](apis/search.md?id=schema-search-groups).
3. Add the top-level navigation within your product; First download this CSV [template](apis/search.md?id=search-imports-template) or [example](apis/search.md?id=search-imports-example) then [Import](apis/search.md?id=schema-search-imports) it.
4. [Optional] Add specific content from your database by creating a [SearchItem](apis/search.md?id=schema-search-items) per database record you want to be searchable.
5. Publish your HelpBar by setting the `published_at` timestamp on the `Search`.
6. Visit your product where Chameleon is installed and hit `CMD` + `k` (or how you configured `key_meta` and `key_uid`).
7. Test a few search terms!

-----

## HelpBar REST API :id=search-rest-api

With the Chameleon REST API for Search, you can:

- Index custom content (the data from your product) into searchable [SearchItem](apis/search.md?id=schema-search-items)s.
- Import your product navigation to allow your Users to jump to a specific thing they are looking for with a [SearchImport](apis/search.md?id=schema-search-imports).
- Configure [SearchGroups](apis/search.md?id=schema-search-groups) to pull content from public sources (i.e. your Help center, Blog etc.).
- Define a [SearchLabelTheme](apis/search.md?id=schema-search-label-themes) to label your [SearchItem](apis/search.md?id=schema-search-items)s for greater visibility.
- Add labels to the title or description of `SearchItem`s as [SearchLabel](apis/search.md?id=schema-search-labels)s.


## `Search` bar Schema :id=schema

> `Search` is associated with `groups`: [SearchGroups](apis/search.md?id=schema-search-groups), and `label_themes`: [SearchLabelThemes](apis/search.md?id=schema-search-groups)

| Property                      | Type      | Description                                                                                                                                                       |
|-------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                          | ID        | The Chameleon ID                                                                                                                                                  |
| `created_at`                  | timestamp | When this happened or when this was added to the Database                                                                                                         |
| `updated_at`                  | timestamp | The last time any property was updated                                                                                                                            |
| `placeholder`                 | string    | The text used as the Search input placeholder                                                                                                                     |
| `key_meta`                    | boolean   | For the keyboard shortcut activation, is the CMD / CTRL key required to activate the HelpBar                                                                      |
| `key_uid`                     | string    | For the keyboard shortcut activation, the letter to be used in combination with `key_meta` to activate the HelpBar bar                                            |
| `title_recent`                | string    | The label given to the group of "Recent items"                                                                                                                    |
| `title_pinned`                | string    | The label given to the group of "Pinned items"                                                                                                                    |
| `published_at`                | timestamp | The time this was most recently published                                                                                                                         |
| `style_color_background`      | string    | The background color of this HelpBar                                                                                                                              |
| `style_color_text`            | string    | The font color of this HelpBar                                                                                                                                    |
| `style_item_color_highlight`  | string    | The hover color of the items of HelpBar                                                                                                                           |
| `style_item_border_highlight` | string    | The left-hand-side highlight color of the items of this HelpBar                                                                                                   |
| `url_group_ids`               | array     | The [`Environment`](apis/urls.md?id=url-groups) that this is enabled to run on                                                                                    |
| `published_updated_at`        | timestamp | A copy of the Updated time (`updated_at`) when this was most recently published; used to track if an Experience is edited since last publish                      |
| `published_user_id`           | ID        | The Chameleon ID of User who most recently published this                                                                                                         |
| `oids`                        | none      | A set of pre-known IDs to directly add [SearchItem](apis/search.md?id=schema-search-items)s to the default [SearchGroup](apis/search.md?id=schema-search-groups)s |
| `label_themes`                | array     | The array of `SearchLabelTheme` models                                                                                                                            |


## `SearchGroups` Schema :id=schema-search-groups

| Property                    | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                        | ID        | The Chameleon ID                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `created_at`                | timestamp | When this happened or when this was added to the Database                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `updated_at`                | timestamp | The last time any property was updated                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `url`                       | string    | The URL that this [SearchGroup](apis/search.md?id=schema-search-groups) uses to fetch Search content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `title`                     | string    | The label given to this group in the HelpBar `Search` box                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `integration`               | string    | The backend search integration to search with (defaults to `bing`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `position`                  | number    | The order that these appear in lists (starting from 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `last_test_at`              | timestamp | At the completion of a test of the configured URL, this value is set to the current timestamp.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `icon`                      | object    | The `SearchIcon` info to display for all results of this [SearchGroup](apis/search.md?id=schema-search-groups)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `icon.kind`                 | none      | The "kind" of icon being used, one of `uid` or `image`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `icon.uid`                  | none      | When using `kind="uid"`, a specific Chameleon supplied svg-based icon [2]. One of: `academic_cap`, `badge_check`, `beaker`, `bell`, `book_open`, `bulb`, `cake`, `calculator`, `calendar`, `chart_bar`, `chart_pie`, `chat_messages`, `chat_dots`, `chip`, `clipboard`, `clock`, `cloud_download`, `cloud`, `code`, `cog`, `color_swatch`, `connection`, `database`, `document_add`, `document_report`, `download`, `film`, `finger_print`, `fire`, `flag`, `folder`, `gift`, `globe`, `home`, `identification`, `key`, `leon`, `library`, `lightning_bolt`, `link`, `location_marker`, `map`, `microsurvey`, `music_note`, `paper_airplane`, `paper_clip`, `photograph`, `pop_out`, `presentation_chart`, `puzzle`, `qr_code`, `question_mark_circle`, `refresh`, `scale`, `search`, `segments`, `server`, `shield_check`, `sparkles`, `speakerphone`, `star`, `sun`, `support`, `table`, `tag`, `target`, `ticket`, `hammer`, `tooltip`, `signpost`, `truck`, `user_circle`, `user`, `users`, `variable`, `boards`, `grid`, `grid_add`, `list`, `warning`, `zoom_in`, `zoom_out`, `thumbs_up`, `thumbs_down`, `cube`, `company`, `click`, `hash`, or `toggle` |
| `icon.image_url`            | none      | When using `kind="image"`, the url to an appropriate icon for this [SearchGroup](apis/search.md?id=schema-search-groups)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `icon.image_alt`            | none      | When using `kind="image"`, the alt text for the icon                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `url_options`               | object    | When configuring this [SearchGroup](apis/search.md?id=schema-search-groups) for an Search integration, Chameleon will fetch some information about the given URL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `url_options.integration`   | none      | The detected integration of the URL; (`intercom`, `zendesk`, `readme`, etc.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `url_options.title`         | none      | The title of the page loaded for URL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `url_options.results_count` | none      | The number of public search results for this URL (0-10)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## `SearchPage` Schema :id=schema-search-page

| Property          | Type      | Description                                                          |
|-------------------|-----------|----------------------------------------------------------------------|
| `id`              | ID        | The Chameleon ID                                                     |
| `created_at`      | timestamp | When this happened or when this was added to the Database            |
| `updated_at`      | timestamp | The last time any property was updated                               |
| `name`            | string    | The name given by an administrator of Chameleon                      |
| `position`        | number    | The order that these appear in lists (starting from 0)               |
| `url_match_all`   | boolean   | Url match all                                                        |
| `quantifier_urls` | array     | List of URL matching conditions that must match the current page URL |


## `SearchLabelTheme` Schema :id=schema-search-label-themes

> To reference a `LabelTheme` when adding `title_labels` or `description_labels` to `SearchItem`s, use the `id` field returned in the `label_themes` wen listing the `Search` with `GET /searches` or Creating with `POST /searches`.

| Property                 | Type      | Description                                                                                             |
|--------------------------|-----------|---------------------------------------------------------------------------------------------------------|
| `id`                     | ID        | The Chameleon ID                                                                                        |
| `created_at`             | timestamp | When this happened or when this was added to the Database                                               |
| `updated_at`             | timestamp | The last time any property was updated                                                                  |
| `name`                   | string    | The name given by an administrator of Chameleon                                                         |
| `style`                  | string    | The basic look of the label: One of: `outline` or `filled`                                              |
| `style_color_text`       | string    | The text color as a hex code of a `style=filled` label, the text and outline of a `style=outline` label |
| `style_color_background` | string    | The background color as a hex code, of a `style=filled` label                                           |



## List all HelpBars :id=searches-index

There is only one per account.

#### HTTP Request

```
GET https://api.trychameleon.com/v3/edit/searches
```


#### HTTP Response

```json
{
  "searches": [
    {
      "id": "6adae460426f060a00000000",
      "placeholder": "Search for help...",
      "key_meta": true,
      "key_uid": "k",
      ...
    }
  ]
}
```


## Create / Update your HelpBar :id=searches-create

There is only one per account so an update uses the same endpoint as create. Use any of the properties available in the [schema](apis/search.md?id=schema)

#### HTTP Request

```
POST https://api.trychameleon.com/v3/edit/searches
```

###### Examples

With a basic config activating with `CMD` + `k` (or `CTRL` + `k`).

```json
{
  "placeholder": "Search for help...",
  "key_meta": true,
  "key_uid": "k",
  "title_recent": "Recently clicked",
  "title_pinned": "Pinned"
}
```

Add two search groups of all help-center content on `help.your-product.com` and of all of your posts to your blog at `blog.your-product.com`.
Help center content defaults to the `book_open` `icon` and `film` for the blog content.

```json
{
  "search_groups": [
    {
      "title": "Help center",
      "url": "https://help.your-product.com",
      "integration": "bing",
      "icon": {
        "kind": "uid",
        "uid": "book_open"
      }
    },
    {
      "title": "Best practices",
      "url": "https://blog.your-product.com",
      "integration": "bing",
      "icon": {
        "kind": "uid",
        "uid": "film"
      }
    }
  ]
}
```

Add a theme for filled-red labels, and one for filled green labels.

> To reference a `LabelTheme` when adding `title_labels` or `description_labels` to `SearchItem`s, use the `id` field returned with each theme.

```json
{
  "label_themes": [
    {
      "style": "filled",
      "style_color_text": "FFF",
      "style_color_background": "FF6666"
    },
    {
      "style": "filled",
      "style_color_text": "FFF",
      "style_color_background": "66FF66"
    }
  ]
}
```

> After you configure/update your HelpBar must publish it!

Publish by setting `published_at` to the current time. This makes your HelpBar available to your Users

```json
{
  "published_at": "2029-04-07T12:18:00Z"
}
```

#### HTTP Response :id=searches-create-http-response

```json
{
  "search": {
    "id": "5f3c4232c712de665632a6d9",
    "placeholder": "Search for help...",
    "key_meta": true,
    "key_uid": "k",
    "title_pinned": "Recommended",
    "title_recent": "Recent",
    "published_at": "2029-04-07T12:18:00Z",
    "label_themes": [
      {
        "id": "6f3c4232c712de632a6d9656",
        "style": "filled",
        "style_color_text": "FFF",
        "style_color_background": "FF6666"
      },
      {
        "id": "62c73c423f12de632a6d96fa",
        "style": "filled",
        "style_color_text": "FFF",
        "style_color_background": "66FF66"
      }
    ]
  }
}
```


------

## `SearchItem` Schema :id=schema-search-items

A search item is a discrete unit of searchable content akin to a Google search result. You have content within your product, even if you don't think of it that way. Any database records that your Users would want to find is a piece of content. Send us this content to surface it to your Users in the Chameleon HelpBar.

> `SearchItem`s are associated with `actions`: [SearchActions](apis/search.md?id=schema-search-actions), and `title_labels` / `description_labels`: [SearchLabels](apis/search.md?id=schema-search-labels)

| Property             | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                 | ID        | The Chameleon ID                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `created_at`         | timestamp | When this happened or when this was added to the Database                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `updated_at`         | timestamp | The last time any property was updated                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `uid`                | string    | The external ID of the search content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `title`              | string    | The display title                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `description`        | string    | The display description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `pinned_at`          | timestamp | Only `SearchItem`s with a timestamp here will show up in the "Pinned" / "Recommended" items search results group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `search_group_id`    | string    | The [SearchGroup](apis/search.md?id=schema-search-groups) that this `SearchItem` will display in.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `profile_ids`        | array     | The IDs of the [User Profile](apis/profiles.md) that has access to this `SearchItem`. Only members these specific [User Profiles](apis/profiles.md) will be displayed this `SearchItem` as a search result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `company_ids`        | array     | The IDs of the [Company](apis/companies.md) that has access to this `SearchItem`. Only members of this [Company](apis/companies.md) will be displayed this `SearchItem` as a search result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `segment_ids`        | array     | The IDs of the [Segment](apis/segments.md) that has access to this `SearchItem`. Only current members of this [Segment](apis/segment.md) will be displayed this `SearchItem` as a search result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `company_uids`       | array     | The external ID (from in your database) for which Company has access to this `SearchItem`. Only members of this [Company](apis/companies.md) will be displayed this `SearchItem` as a search result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `profile_uids`       | array     | The external ID of the [User Profile](apis/profiles.md) that has access to this `SearchItem`. Only members these specific [User Profiles](apis/profiles.md) will be displayed this `SearchItem` as a search result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `icon.kind`          | string    | The "kind" of icon being used, one of `uid` or `image`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `icon.uid`           | string    | When using `kind="uid"`, a specific Chameleon supplied svg-based icon [2]. One of: `academic_cap`, `badge_check`, `beaker`, `bell`, `book_open`, `bulb`, `cake`, `calculator`, `calendar`, `chart_bar`, `chart_pie`, `chat_messages`, `chat_dots`, `chip`, `clipboard`, `clock`, `cloud_download`, `cloud`, `code`, `cog`, `color_swatch`, `connection`, `database`, `document_add`, `document_report`, `download`, `film`, `finger_print`, `fire`, `flag`, `folder`, `gift`, `globe`, `home`, `identification`, `key`, `leon`, `library`, `lightning_bolt`, `link`, `location_marker`, `map`, `microsurvey`, `music_note`, `paper_airplane`, `paper_clip`, `photograph`, `pop_out`, `presentation_chart`, `puzzle`, `qr_code`, `question_mark_circle`, `refresh`, `scale`, `search`, `segments`, `server`, `shield_check`, `sparkles`, `speakerphone`, `star`, `sun`, `support`, `table`, `tag`, `target`, `ticket`, `hammer`, `tooltip`, `signpost`, `truck`, `user_circle`, `user`, `users`, `variable`, `boards`, `grid`, `grid_add`, `list`, `warning`, `zoom_in`, `zoom_out`, `thumbs_up`, `thumbs_down`, `cube`, `company`, `click`, `hash`, or `toggle` |
| `icon.image_url`     | sting     | When using `kind="image"`, the url to an appropriate icon for this [SearchGroup](apis/search.md?id=schema-search-groups)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `icon.image_alt`     | string    | When using `kind="image"`, the alt text for the icon                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `actions`            | array     | An array of the [`SearchAction`](apis/search.md?id=schema-search-actions) that run when this `SearchItem` is clicked/selected in the HelpBar                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `title_labels`       | array     | An array of the [`SearchLabel`](apis/search.md?id=schema-search-labels) items displayed in the title of this `SearchItem`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `description_labels` | array     | An array of the [`SearchLabel`](apis/search.md?id=schema-search-labels) items displayed under the description of this `SearchItem`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |


## `SearchLabel` Schema :id=schema-search-labels

| Property    | Type   | Description                                                                                                                                                                                                                                                 |
|-------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `text`      | string | The display text of the label                                                                                                                                                                                                                               |
| `theme_uid` | string | The theme of this label, either the ID of a `SearchLabelTheme` configured on the `Search`, or a predefined theme: One of: `filled_green`, `filled_blue`, `filled_yellow`, `filled_red`, `outline_green`, `outline_blue`, `outline_yellow`, or `outline_red` |




## List all Search Items :id=search-items-index

`SearchItem`s are for private content, and are added to Chameleon via CSV or directly via this REST API.
They can be scoped on a per-company basis and there can be many thousands of custom search items,
use the `cursor` to list as many as you need.

> Note: this is how you iterate through all searchable content but it's not how your Users search for this content, if you want to query your data like and end-user, feel free to [Contact us](https://app.trychameleon.com/help) to learn more.


#### HTTP Request

```
GET https://api.trychameleon.com/v3/edit/search_items
```

| param              | -        | description                                                                                                                                     |
|--------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| `limit`            | optional | Defaults to `50` with a maximum of `500`                                                                                                        |
| `before`           | optional | Used when paginating, use directly from the `cursor` object from the previous response                                                          |
| `before`           | optional | Read as "created `before`" and can be given as a timestamp to get only `limit` items that were created before this time                         |
| `after`            | optional | Read as "created `after`" and can be given as a timestamp or ID to get only `limit` items that were created after this time                     |
| `search_import_id` | optional | Fetch only the `SearchItem`s that were created (or updated most recently) by the given [SearchImport](apis/search.md?id=schema-search-imports). |


#### HTTP Response

```json
{
  "search_items": [
    {
      "id": "5f3c4232c712de665632a5f1",
      "title": "Data onboarding",
      "description": "The first step in making the switch is to import your first round of data.",
      ...
    },
    ... 48 more
    {
      "id": "5f3c4232c712de665632a5a2",
      "title": "Invite your team",
      "description": "Enable the rest of your team to collaborate, close items in your boards and see your workflows.",
      ...
    },
  ],
  "cursor": {
    "limit": 50,
    "before": "5f3c4232c712de665632a5f2"
  }
}
```


## Create / Update your `SearchItem`s :id=search-items-create

Use any of the properties available in the [schema](apis/search.md?id=schema-search-items).

You must either send a `uid` field (as the unique identifier for a piece of content) OR the Chameleon ID in the url path.
Using the POST-based endpoint below and sending the required `uid` acts as a "create or update" (upsert).

When content relates to a specific database item, include the database ID of that record in the `uid`

#### HTTP Request

With the parameter of `uid`; this endpoint will "create or update" (upsert) your content:

```
POST https://api.trychameleon.com/v3/edit/search_items
```

or if you have stored the SearchItem ID field from when you created it:

```
PATCH https://api.trychameleon.com/v3/edit/search_items/:id
```

###### Examples

Add a specific important action within your product for the Company in your DB with ID=14203, navigate to the onboarding page

```json
{
  "uid": "data-onboarding",
  "title": "Data onboarding",
  "description": "The first step in making the switch is to import your first round of data.",
  "company_uids": ["14203"],
  "actions": [
    {
      "kind": "navigate",
      "url": "/data/import"
    }
  ]
}
```


Upsell with a search result, directly book a demo with Calendly

```json
{
  "uid": "data-onboarding-book-demo",
  "title": "Data onboarding - see it in action",
  "description": "Book a demo with us to see the immediate value we can provide.",
  "actions": [
    {
      "kind": "calendly",
      "calendly_url": "https://calendly.com/your-company/sales-team-data-demo"
    }
  ]
}
```

Target content to a Chameleon [Segment](apis/segments.md) of Users

```json
{
  "uid": "data-onboarding-admins-book-demo",
  "title": "Data onboarding - see it in action",
  "description": "Book a demo with us to see the immediate value we can provide.",
  "segment_ids": ["5f3c4232c712de665632a6d9"],
  "actions": [
    {
      "kind": "calendly",
      "calendly_url": "https://calendly.com/your-company/sales-team-data-demo"
    }
  ]
}
```

Target content to three Chameleon [Companies](apis/companies.md) -- Only members of these companies will be able to search for this item.

As parameters you can send either `company_uids` as the ID from **your database** or you can first lookup the
Chameleon [Companies](apis/companies.md?id=companies-show) and then send `company_ids` parameter.

```json
{
  "uid": "data-example-multi-company-book-demo",
  "title": "Data onboarding - see it in action",
  "description": "Book a demo with us to see the immediate value we can provide.",
  "company_uids": ["44621", "93821", "1265"],
  "actions": [
    {
      "kind": "calendly",
      "calendly_url": "https://calendly.com/your-company/sales-team-data-demo"
    }
  ]
}
```

Target content to a Chameleon [Company](apis/companies.md) -- Only members of this Company will be able to search for this item.

```json
{
  "uid": "data-onboarding-admins-book-demo",
  "title": "Data onboarding - see it in action",
  "description": "Book a demo with us to see the immediate value we can provide.",
  "company_uids": ["93821"],
  "actions": [
    {
      "kind": "calendly",
      "calendly_url": "https://calendly.com/your-company/sales-team-data-demo"
    }
  ]
}
```

Target content to a Chameleon [User Profile](apis/profiles.md) -- Only this specific User will be able to search for this item.

```json
{
  "uid": "data-onboarding-59324-book-demo",
  "title": "Data onboarding for {{first_name fallback='you'}} - see it in action",
  "description": "Book a demo with us to see the immediate value we can provide.",
  "profile_uids": ["59324"],
  "actions": [
    {
      "kind": "calendly",
      "calendly_url": "https://calendly.com/your-company/sales-team-data-demo"
    }
  ]
}
```

A hypothetical "car dealership" wants to make a used car searchable, track an event to
all [configured Integrations](https://app.trychameleon.com/integrations) and open the listing in a new tab.
It also includes a title label of `NEW` themed with an [example theme](apis/search.md?id=searches-create-http-response) from above.

```json
{
  "uid": "cars:28192",
  "title": "2029 just off lease!!!",
  "description": "Come check this one out today, nice inside and out, 105kW battery, 6400 miles.",
  "actions": [
    {
      "kind": "event",
      "event_name": "Clicked Search => Car Listing"
    },
    {
      "kind": "url",
      "url": "https://my.cars.com/listings/2029-04/car/28192",
      "url_blank": true
    }
  ],
  "title_labels": [
    {
      "text": "NEW",
      "theme_uid": "62c73c423f12de632a6d96fa"
    }
  ]
}
```

## Batch Update your `SearchItem`s :id=search-items-batch-update

```
POST https://api.trychameleon.com/v3/edit/search_items/batch
```

| param     | -        | description                                                                                                  |
|-----------|----------|--------------------------------------------------------------------------------------------------------------|
| `ids`     | required | An array of `SearchItem` IDs to update                                                                       |
| `*others` | optional | Use any of the properties available in the [single SearchItem update](apis/search.md?id=search-items-create) |


To update the icon of many items:

```json
{
   "ids": [
     "6f3c42a6dd656232c712de63",
     "6f4c42a6d92f2c712d656e65",
     "6f5c42a6df232d656e2c7167"
   ],
   "icon": {
      "kind": "uid",
      "uid": "Puzzle"
   }
}
```


To update the [SearchGroup](apis/search.md?id=schema-search-group) of many items:

```json
{
   "ids": [
     "6f3c42a6dd656232c712de63",
     "6f4c42a6d92f2c712d656e65",
     "6f5c42a6df232d656e2c7167"
   ],
   "search_group_id": "5f3c4232c712de665632a6d9"
}
```


## Delete a `SearchItem`s :id=search-items-destroy

Send the `uid` of a previously created `SearchItem`.


#### HTTP Request

```
DELETE https://api.trychameleon.com/v3/edit/search_items
```


## Bulk Delete a `SearchItem`s :id=search-items-bulk-destroy

Send the `ids` of a previously created `SearchItem`.


#### HTTP Request

```
DELETE https://api.trychameleon.com/v3/edit/search_items/batch
```

```json
{
   "ids": [
     "6f3c42a6dd656232c712de63",
     "6f5c42a6df232d656e2c7167"
   ]
}
```


## `SearchAction` Schema :id=schema-search-actions

A search action is one item in a collection of actions attached to a [SearchItem](apis/search.md?id=schema-search-items)s. When
the item is clicked the actions will be run in order (configure `kind=navigate` / `kind=url` last).


Base schema

| Property        | Type      | Description                                                                                                                                                                                                                                                                  |
|-----------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `updated_at`    | timestamp | The last time any property was updated                                                                                                                                                                                                                                       |
| `kind`          | string    | The kind of action to take: One of: `url`, `navigate`, `event`, `identify`, `tour`, `survey`, `script`, `function`, `airtable`, `calendly`, `chili_piper`, `figma`, `helpscout`, `hubspot_lists`, `intercom`, `link`, `livestorm`, `loom`, `pitch`, `typeform`, or `zendesk` |
| `helpbar_state` | string    | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open`                                                                                                                                                                      |
| `*others`       | optional  | Any other integration specific configuration (more info below in the specific schemas)                                                                                                                                                                                       |

### Integration specific schemas


## `SearchAction` with `kind=url` Schema :id=schema-search-action-url

| Property | Type | Description                                                                                             |
| --- | --- |---------------------------------------------------------------------------------------------------------|
| `kind` | `string` | "url" (required)                                                                                        |
| `helpbar_state` | string | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open` |
| `url` | `string` | The URL to use/open. Can be a full URL including https, or can be relative to the current page etc.)    |
| `url_blank` | `string` | If the URL opens in a new tab (defaults to `true`)                                                        |

```json
{
   "kind": "url",
   "url": "https://help.your-product.com/posts/339201-learn-more-about-it"
}
```

## `SearchAction` with `kind=navigate` Schema :id=schema-search-action-navigate

| Property | Type | Description |
| --- | --- | --- |
| `kind` | `string` | "navigate" (required) |
| `helpbar_state` | string | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open` |
| `url` | `string` | The URL to use/open. Can be a full URL including https, or can be relative to the current page etc.) |

```json
{
   "kind": "navigate",
   "url": "/cars/339201/edit"
}
```


## `SearchAction` with `kind=event` Schema :id=schema-search-action-event

Track an event to Chameleon and all of your [configured integrations](https://app.chameleon.io/integrations).

| Property | Type | Description |
| --- | --- | --- |
| `kind` | `string` | "event" (required) |
| `helpbar_state` | string | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open` |
| `event_name` | `string` | The name of the Event to track to your configured integrations |

```json
{
   "kind": "event",
   "event_name": "Search action taken (custom)"
}
```


## `SearchAction` with `kind=identify` Schema :id=schema-search-action-identify

Send user data to Chameleon and all of your [configured integrations](https://app.chameleon.io/integrations).

| Property | Type | Description |
| --- | --- | --- |
| `kind` | `string` | "identify" (required) |
| `helpbar_state` | string | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open` |
| `identify_key` | `string` | The specific key to set to your configured integrations  |
| `identify_value` | `string` | The specific value to set to your configured integrations  |


```json
{
   "kind": "identify",
   "identify_key": "opted_in_for_product_research",
   "identify_value": "true"
}
```


## `SearchAction` with `kind=tour` Schema :id=schema-search-action-tour

Show a Chameleon Tour immediately (calls `chmln.show` with the configured `tour_id`). Quickly access this ID in the URL on the [Chameleon dashboard](https://app.chameleon.io/tours).
[JavaScript API reference](js/show-tour.md)

| Property | Type | Description |
| --- | --- | --- |
| `kind` | `string` | "tour" (required) |
| `helpbar_state` | string | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open` |
| `tour_id` | `string` | The ID of the published Chameleon Tour to trigger |

```json
{
   "kind": "tour",
   "tour_id": "6f7dfada300116393481bbbb"
}
```



## `SearchAction` with `kind=survey` Schema :id=schema-search-action-survey

Show a Chameleon Microsurvey immediately (calls `chmln.show` with the configured `survey_id`). Quickly access this ID in the URL on the [Chameleon dashboard](https://app.chameleon.io/surveys).
[JavaScript API reference](js/show-tour.md)

| Property | Type | Description |
| --- | --- | --- |
| `kind` | `string` | "survey" (required) |
| `helpbar_state` | string | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open` |
| `survey_id` | `string` | The ID of the published Chameleon Microsurvey to trigger |

```json
{
   "kind": "survey",
   "survey_id": "6d7dfad00116393ba481bb3c"
}
```


## `SearchAction` with `kind=script` Schema :id=schema-search-action-script

Run customized JavaScript when this item is clicked in the HelpBar. Check variables, user data, or page
state before performing different actions.

| Property | Type | Description |
| --- | --- | --- |
| `kind` | `string` | "script" (required) |
| `helpbar_state` | string | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open` |
| `script` | `string` | The JavaScript string to evaluate |


```json
{
   "kind": "script",
   "script": "const pageStateDone = /#state=finished/.test(window.location.href);\nif(pageStateDone) { showFinishedModal() } else { showTodoModal() }"
}
```


## `SearchAction` with `kind=function` Schema :id=schema-search-action-function

After you have exposed a function on the `window` object within your application, call it when this item is clicked.

| Property | Type | Description |
| --- | --- | --- |
| `kind` | `string` | "function" (required) |
| `helpbar_state` | string | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open` |
| `fn` | `string` | The name of a function to call (without arguments (i.e. customChameleonFn_032) |

```json
{
   "kind": "function",
   "fn": "showCustomModal_chameleonAction_19"
}
```


## `SearchAction` with `kind=airtable` Schema :id=schema-search-action-airtable

Show an Airtable form directly in your product.

| Property         | Type | Description                                                                                             |
|------------------| --- |---------------------------------------------------------------------------------------------------------|
| `kind`           | `string` | "airtable" (required)                                                                                   |
| `helpbar_state`  | `string` | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open` |
| `href`           | `string` | The URL to use                                                                                          |

```json
{
   "kind": "airtable",
   "href": "https://airtable.com/1AyOshrwxGUPn"
}
```

## `SearchAction` with `kind=arcade` Schema :id=schema-search-action-arcade

Launch an Arcade Demo in a full screen modal

| Property        | Type      | Description                                                                                             |
|-----------------|-----------|---------------------------------------------------------------------------------------------------------|
| `kind`          | `string`  | "arcade" (required)                                                                                     |
| `helpbar_state` | `string`  | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open` |
| `href`          | `string`  | The URL to use (Arcade Share URL)                                                                       |

```json
{
   "kind": "arcade",
   "href": "https://app.arcade.software/share/E4EoapWRfxxeN3nX1rRe"
}
```

## `SearchAction` with `kind=calendly` Schema :id=schema-search-action-calendly

Show a Calendly scheduling modal directly in your product.


| Property | Type | Description |
| --- | --- | --- |
| `kind` | `string` | "calendly" (required) |
| `helpbar_state` | `string` | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open` |
| `href` | `string` | The URL to use |

```json
{
   "kind": "calendly",
   "href": "https://calendly.com/chameleon/demo"
}
```

[Merge tags](concepts/personalizing.md) are available for the `href` field; add the right Calendly link as [User data](webhooks/profiles.md) and merge it in the action. (`csm` below refers to a customer success manager)

```json
{
   "kind": "calendly",
   "href": "{{calendly_csm_url}}"
}
```


## `SearchAction` with `kind=chili_piper` Schema :id=schema-search-action-chili_piper

Show a ChiliPiper scheduling modal directly in your product.

| Property | Type | Description |
| --- | --- | --- |
| `kind` | `string` | "chili_piper" (required) |
| `helpbar_state` | `string` | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open` |
| `selected` | `string` | The type of Experience to enable. One of: `router` or `href` |
| `router` | `string` | The ChiliPiper Router name associated with this calendar |
| `href` | `string` | The URL to use |

For a scheduling link

```json
{
   "kind": "chili_piper",
   "selected": "href",
   "href": "https://chameleon.na.chilipiper.com/book/queuey-queue"
}
```

For a ChiliPiper router

```json
{
   "kind": "chili_piper",
   "selected": "router",
   "router": "csm-router"
}
```

[Merge tags](concepts/personalizing.md) are available for the `href` field; add the right Calendly link as [User data](webhooks/profiles.md) and merge it in the action. (`csm` below refers to a customer success manager)

```json
{
   "kind": "chili_piper",
   "selected": "href",
   "href": "https://chameleon.na.chilipiper.com/book/{{chilipiper_csm_queue}}"
}
```

## `SearchAction` with `kind=embed` Schema :id=schema-search-action-embed

Launch any embeddable page in a full screen modal.


| Property        | Type     | Description                                                                                             |
|-----------------|----------|---------------------------------------------------------------------------------------------------------|
| `kind`          | `string` | "embed" (required)                                                                                     |
| `helpbar_state` | `string` | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open` |
| `href`          | `string` | The URL to use (this URL needs to be a embeddable)                                                      |

```json
{
   "kind": "embed",
   "href": "https://content.acme.co/embeds/custom-widgets/23s2a"
}
```


## `SearchAction` with `kind=figma` Schema :id=schema-search-action-figma

Show a Figma file or prototype directly in your product.


| Property | Type | Description |
| --- | --- | --- |
| `kind` | `string` | "figma" (required) |
| `helpbar_state` | `string` | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open` |
| `href` | `string` | The URL to use |

```json
{
   "kind": "figma",
   "href": "https://www.figma.com/file/QFEMdNRma0Y1WDcMRCw9Fz/Prototyping-in-Figma?node-id=0-1&t=YfflZMSK0tnWnCCu-0"
}
```

## `SearchAction` with `kind=google` Schema :id=schema-search-action-google

Show a Google Doc / Sheet / Form / Slides in a full screen modal.


| Property | Type | Description                                                                                             |
| --- | --- |---------------------------------------------------------------------------------------------------------|
| `kind` | `string` | "google" (required)                                                                                     |
| `helpbar_state` | `string` | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open` |
| `href` | `string` | The URL to use (this Google doc needs to be "Published to Web" to be embeddable)                        |

```json
{
   "kind": "google",
   "href": "https://docs.google.com/document/d/e/2PACX-1vQ7tXBCx-9gAlzHvROHNGC1_cklni0CmbBPHk/pub"
}
```

## `SearchAction` with `kind=helpscout` Schema :id=schema-search-action-helpscout

| Property | Type | Description                                                                                                             |
| --- | --- |-------------------------------------------------------------------------------------------------------------------------|
| `kind` | `string` | "helpscout" (required)                                                                                                  |
| `helpbar_state` | `string` | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open`                 |
| `helpscout_kind` | `string` | The type of HelpScout Experience to enable. One of: `open_chat`, `open_answers`, `search_term`, or `open_help_center`   |
| `query` | `string` | The search term to use for this action                                                                                  |
| `article_url` | `string` | The specific URL / Help article to load                                                                                 |
| `article_mode` | `string` | Where to display this article. One of: `null`, `menu`, or `new_tab` (defaults to `null` and opens in a HelpScout modal) |

Open the `Beacon` to the default state

```json
{
   "kind": "helpscout",
   "helpscout_kind": "open_chat"
}
```


Open HelpScout modal in your product to a specific article.

```json
{
   "kind": "helpscout",
   "helpscout_kind": "open_help_center",
   "article_url": "https://help.your-product.com/article/596-billing-and-plans-guide"
}
```

Open the `Beacon` to a specific article.

```json
{
   "kind": "helpscout",
   "helpscout_kind": "open_help_center",
   "article_url": "https://help.your-product.com/article/596-billing-and-plans-guide",
   "article_mode": "menu"
}
```


Open the `Beacon` to the answers tab

```json
{
   "kind": "helpscout",
   "helpscout_kind": "open_answers"
}
```

Open the `Beacon` to a specific search query. Help users understand what is available in the help center

```json
{
   "kind": "helpscout",
   "helpscout_kind": "search_term",
   "query": "Import data",
}
```


## `SearchAction` with `kind=hubspot_lists` Schema :id=schema-search-action-hubspot_lists

| Property | Type | Description |
| --- | --- | --- |
| `kind` | `string` | "hubspot_lists" (required) |
| `helpbar_state` | `string` | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open` |
| `href` | `string` | The URL to use |

```json
{
   "kind": "hubspot",
   "href": "https://meetings.hubspot.com/chameleon-sales/11-chat-30-minutes"
}
```


## `SearchAction` with `kind=intercom` Schema :id=schema-search-action-intercom

| Property | Type | Description |
| --- | --- | --- |
| `kind` | `string` | "intercom" (required) |
| `helpbar_state` | `string` | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open` |
| `selected` | `string` | The type of Experience to enable. One of: `open_chat`, `search_term`, or `open_help_center` |
| `message` | `string` | A pre-filled message to provide a hint of the proposed message to your team |
| `search_term_article` | `string` | The search term to use for this action |
| `specific_article` | `string` | The specific URL / Help article to load |
| `article_mode` | `string` | Where to display this article |

```json
{
   "kind": "intercom",
   "selected": "open_chat"
}
```


```json
{
   "kind": "intercom",
   "selected": "open_help_center",
   "specific_article": "https://help.chameleon.io/en/collections/3572193-chameleon-101"
}
```


## `SearchAction` with `kind=livestorm` Schema :id=schema-search-action-livestorm

Directly register a user for a webinar session; combine with a second action for `kind=url` that takes them to your "success" page.

| Property | Type | Description |
| --- | --- | --- |
| `kind` | `string` | "livestorm" (required) |
| `helpbar_state` | `string` | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open` |
| `session_uid` | `string` | The Livestorm Session ID copied from your Livestorm dashboard |
| `utm_campaign` | `string` | The UTM Campaign parameter for this Livestorm Session registration |
| `utm_source` | `string` | The UTM Source parameter for this Livestorm Session registration |
| `utm_medium` | `string` | The UTM Medium parameter for this Livestorm Session registration |

```json
{
   "kind": "livestorm",
   "session_uid": "b820db33-3f2c-4159-a991-126fe03a7931",
   "utm_source": "chameleon_helpbar"
}
```


## `SearchAction` with `kind=loom` Schema :id=schema-search-action-loom

Show a Loom video directly in your product.

| Property | Type | Description |
| --- | --- | --- |
| `kind` | `string` | "loom" (required) |
| `helpbar_state` | `string` | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open` |
| `href` | `string` | The URL to use |

```json
{
   "kind": "loom",
   "href": "https://www.loom.com/share/827d72cda9ed4724b30ba663f9ca00d3"
}
```

## `SearchAction` with `kind=navattic` Schema :id=schema-search-action-navattic

Launch an Navattic Demo in a full screen modal.

| Property        | Type     | Description |
|-----------------|----------| --- |
| `kind`          | `string` | "navattic" (required) |
| `helpbar_state` | `string` | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open` |
| `href`          | `string` | The URL to use |

```json
{
   "kind": "navattic",
   "href": "https://capture.navattic.com/cl4r18309ml5cngqz3e4fu84k"
}
```


## `SearchAction` with `kind=pitch` Schema :id=schema-search-action-pitch

Show a Pitch presentation directly in your product.

| Property | Type | Description |
| --- | --- | --- |
| `kind` | `string` | "pitch" (required) |
| `helpbar_state` | `string` | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open` |
| `href` | `string` | The URL to use |

```json
{
   "kind": "pitch",
   "href": "https://pitch.com/public/23e42e85-8142-4401-814e-509b597f06b0"
}
```


## `SearchAction` with `kind=typeform` Schema :id=schema-search-action-typeform

Show a Typeform survey directly in your product.

| Property | Type | Description |
| --- | --- | --- |
| `kind` | `string` | "typeform" (required) |
| `helpbar_state` | `string` | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open` |
| `href` | `string` | The URL to use |
| `mode` | `string` | The Typeform display mode for this survey. One of: `popup`, `drawer_left`, `drawer_right`, or `popover` |

```json
{
   "kind": "typeform",
   "href": "https://trychameleon.typeform.com/to/ahn7QkmE#source=developer_docs",
   "mode": "popup"
}
```


## `SearchAction` with `kind=zendesk` Schema :id=schema-search-action-zendesk

| Property | Type | Description |
| --- | --- | --- |
| `kind` | `string` | "zendesk" (required) |
| `helpbar_state` | `string` | If the HelpBar stays open or closes when taking this action (optional defaults to null): One of: `open` |
| `selected` | `string` | The type of Experience to enable. One of: `open_chat`, `search_term`, or `open_help_center` |
| `search_term_article` | `string` | The search term to use for this action |
| `specific_article` | `string` | The specific URL / Help article to load |

Open the `window.zE` chat window

```json
{
   "kind": "zendesk",
   "selected": "open_chat"
}
```

Search your Zendesk help center for the given search term

```json
{
   "kind": "zendesk",
   "selected": "search_term",
   "search_term_article": "Import data"
}
```


-----

## Search JavaScript API :id=search-js-api

At a high level, Chameleon uses the `chmln` object on the page via `chmln.on` to allow you to control the HelpBar experience. **All of these event listeners are optional**.

See the [Type definitions below ↓](apis/search.md?id=search-js-types)

##### Recommended

```javascript

chmln.on('app:navigate', (opts: NavigateOpts) => {
  /*
  Nagivate with React router / Vue router / pushState / call window.open / etc.

  Frameworks:
    - React info here => https://www.npmjs.com/package/@chamaeleonidae/chmln
    - Add more frameworks with a PR to this file and receive a $50 gift card

  opts.to is the `url` from the SearchAction; this SearchAction is configured with `kind=navigate`

  */
});
```

##### Optional

```javascript

chmln.on('helpbar:search', (opts: SearchOpts, ctx: Context) => {
  /*
  Optional:
    - Generally Chameleon will handle search for you
    - If you need to add custom "Search" logic use this event to pass back the right items, two options:
      - directly return an array<SearchGroup>; include and `id`, `title`, and `search_items` keys for each SearchGroup
      - return a Promise that will resolve with the first argument being an array<SearchItem>.
    - Best used when you already use Algolia or have a custom search endpoint internally

  Called when:
    - The User has entered in a query; when a user enters text and pauses

   return array<SearchGroup>
   return Promise that resolves with the first argument as array<SearchGroup>
   return null (or don't implement) to use the search results as pulled from Chameleon

   opts.query is the search term queried for

   */
});

chmln.on('helpbar:opened', (opts: BlankOpts, ctx: Context) => {
  /*
  Optional:
    - This is purely informational but can be used for custom tracking etc.

  Called when:
    - The HelpBar is triggerd (opened by the User)

  ctx.source will tell you how it was opened

  */
});

chmln.on('helpbar:closed', (opts: BlankOpts, ctx: Context) => {
  /*
  Optional:
    - This is purely informational but can be used for custom tracking etc.

  Called when:
    - The HelpBar is closed by the User

  */
});

chmln.on('helpbar:items:recent', (opts: RecentOpts, ctx: Context) => {
  /*
  Optional:
    - Chameleon will handle recent items for you
    - If you need to add custom "Recent items" logic use this event to pass back the right items

  Called when:
    - the HelpBar needs a list of the most recent actions taken

  return Array or Promise of recent actions taken
  return null (or don't implement) to use the recent items as tracked by Chameleon

  opts.items is an array<SearchItem>; the 4 most recent actions taken

  */
});

chmln.on('helpbar:items:pinned', (opts: BlankOpts, ctx: Context) => {
  /*
  Optional:
    - Chameleon will handle pinned items for you
    - If you need to add custom "Suggestion items" logic use this event to pass back the right items

  Called when:
    - the HelpBar needs a list of the pinned items

  return Array or Promise of pinned items to display
  return null (or don't implement) to use the pinned items as added to Chameleon backend via SearchItem

  */
});

chmln.on('helpbar:search:items', (opts: SearchItemsOpts, ctx: Context) => {
  /*
   Optional:
     - This is purely informational but can be used for custom tracking etc.

   Called when:
     - The Search query finished with 1 or more search results

   opts.query is the search term queried for
   opts.items an array<SearchItem> of all search results for this query
      - opts.items.length will equal 0 when no results were returned

  */
});

chmln.on('helpbar:item:action', (opts: ActionOpts, ctx: Context) => {
  /*
  Optional:
    - Chameleon performs the configured actions automatically in the order they are defined in.
    - If you need to know when a specific "SearchItem" is clicked/triggered, use this event to know

  Called when:
    - When the SearchItem is clicked/triggered/selected and its actions are about to run

  opts.item is a SearchItem
  opts.item.actions is the array<SearchAction> that will be run

  */
});

chmln.on('helpbar:item:action:error', (opts: ActionErrorOpts, ctx: Context) => {
  /*
  Optional:
    - Chameleon may encounter an error when triggering an action.

  Called when:
    - When an action encounters an error

  opts.item is a SearchItem
  opts.action is a SearchAction that errored

  */
});

```

### JS API type definitions :id=search-js-types

<details>
<summary>Type definitions for JS API</summary>

```typescript
// Describes the context of the User when they do a specific action
type Context = {
  source: 'shortcut' | 'element' | 'js_api';
  elapsed: number;
};

// just a plan object with no properties
type BlankOpts = {
};

type SearchOpts = {
  query: string,
};

type SearchItemsOpts = {
  query: string,
  items: array<SearchItem>,
};

type RecentOpts = {
  items: array<SearchItem>,
};

// See SearchAction above for schema
type ActionOpts = {
  item: <SearchItem>,
};

type ActionErrorOpts = {
  item: <SearchItem>,
  action: <SearchAction>,
};

type NavigateOpts = {
  to: string,
};

```

</details>



## Limits :id=limits

> When these limits are exceeded, the endpoints will return a status code `409` with a descriptive error message please [Contact us](https://app.trychameleon.com/help) with any questions.

1. Each `SearchItem` can be targeted to one or many `Company`, `Segment`, or `Profile`s. 
   1. An Free/Startup account is limited to 10 per `SearchItem` and in aggregate across all `SearchItem`s.
   2. A Growth/Enterprise account is limited to 30 per `SearchItem` and in aggregate across all `SearchItem`s..
2. Each `SearchGroup` can be targeted to one or many `Company` or `Segment`.
   1. An Free/Startup account is limited to 10 in use across all `SearchGroup`s and in aggregate across all `SearchGroup`s.
   2. A Growth/Enterprise account is limited to 30 in use across all `SearchGroup`s and in aggregate across all `SearchGroup`s.
3. Each HelpBar can have many groups (`SearchGroup`) and each can be targeted to one or many `Segment`s.
   1. An Free/Startup account is limited to 20 `SearchGroup`s.
   2. A Growth/Enterprise account is limited to 100 `SearchGroup`s.



----

## Search Item Importing via CSV (`SearchImport`) :id=schema-search-imports

| Property                    | Type      | Description                                                                                                                                                              |
|-----------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                        | ID        | The Chameleon ID                                                                                                                                                         |
| `created_at`                | timestamp | When this happened or when this was added to the Database                                                                                                                |
| `updated_at`                | timestamp | The last time any property was updated                                                                                                                                   |
| `file`                      | File      | The file to import, please use the [template](https://chmln.co/helpbar-content-template) to make this easier.                                                            |
| `filename`                  | string    | The name of the original file uploaded                                                                                                                                   |
| `search_group_id`           | string    | The [SearchGroup](apis/search.md?id=schema-search-groups) that all of the resulting `SearchItem`s will display in.  (and/or this can be customized per row with "HelpBar Group ID" column) |
| `head_columns`              | array     | A list representing the parsed version of the first 5 lines. Each object has a header column `name` and `values` are an ordered array of the next 4 rows for that column |
| `stats`                     | object    | The details of the data itself and of the last run of this [SearchImport](apis/search.md?id=schema-search-imports).                                                      |
| `stats.rows_count`          | number    | The number of rows in the file                                                                                                                                           |
| `stats.last_row`            | number    | The row number of the most recent processed row (used for mid-import progress bar)                                                                                       |
| `stats.last_import_state`   | string    | The current state of the import                                                                                                                                          |
| `stats.last_import_error`   | string    | A representation of the error the last import encountered                                                                                                                |
| `stats.last_import_at`      | timestamp | The last time this import was run                                                                                                                                        |
| `stats.last_import_elapsed` | number    | The total time (in seconds) that the import took.                                                                                                                        |
| `stats.created_count`       | number    | The number of records created by this Import                                                                                                                             |
| `stats.updated_count`       | number    | The number of records updated by this Import                                                                                                                             |
| `stats.deleted_count`       | number    | The number of records removed by this Import                                                                                                                             |


## Create a Search Import :id=search-imports-create

Use `Content-Type: multipart/form-data` to create an Import in one request, include the `file` parameter with a CSV based on the [template](https://chmln.co/helpbar-content-template).

#### HTTP Request

```
POST https://api.trychameleon.com/v3/edit/search_imports
```

## Get a Search Import :id=search-imports-show

Useful to track the progress of this import. Small imports (< 100 rows) will finish within approx 1 second.

#### HTTP Request

```
GET https://api.trychameleon.com/v3/edit/search_imports/:id
```

## Trigger HelpBar :id=trigger-search-api

This command triggers the display of the HelpBar. Additionally, you can use variations of this command with options to prefill a query or specify a custom placeholder, enhancing the user experience and engagement with the HelpBar.

```
chmln.show('helpbar')
```

This variation of the command allows for additional customization by accepting options. The `query` option enables the prefilling of a query within the HelpBar, serving as a starting point for user inquiries. Additionally, you can specify a custom placeholder using the `placeholder` option to provide users with a helpful prompt.

```
chmln.show('helpbar', options)
```

#### Options:

- `query` (optional): Specifies a pre-filled query string to assist users in formulating their inquiries. If pre-filled as a question, it will also trigger the AI to generate an aswer.

- `placeholder` (optional): Sets a custom placeholder text within the HelpBar, guiding users on what they can search for or ask.

#### Examples:

- Prefill query

```
chmln.show('helpbar', { query: 'annual billing' })
```

- When pre-filled as a question, this will trigger the AI to provide an asnwer.

```
chmln.show('helpbar', { query: 'What is a tour?' })
```

- Specify placeholder text:

```
chmln.show('helpbar', { placeholder: 'Search for it...' })
```


