# HelpBar

**Add a Search bar to your product that allows your Users to search your Product, Help center, and any custom content.**

> **You have content within your product, even if you don't think of it that way. Any database records that your Users would want to find is a piece of content, akin to a Google search result. Send this content to Chameleon and we will surface it to your Users in the Chameleon search bar. The content can be scoped to a specific [Company](apis/company.md), be recommended when the HelpBar is opened and can perform any action from clicking an item.**.

------

See the specific APIs for more information on how to use Search your product.

 - [REST API](apis/search.md?id=search-rest-api)
 - [JavaScript API](apis/search.md?id=search-js-api)


#### To get Search up and running, complete these items:

1. Create a [HelpBar](apis/search.md?id=schema), configure it with `placeholder` etc.
2. Add your Help center as a [`SearchGroup`](apis/search.md?id=schema-search-group).
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

| Property            | Type                          | Description                                                                                                           |
|---------------------|-------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `id`                | ID                            | The Chameleon ID                                                                                                      |
| `created_at`        | timestamp                     | When this happened or when this was added to the Database                                                             |
| `updated_at`        | timestamp                     | The last time any property was updated                                                                                |
| `placeholder`       | string                        | The text used as the search input placeholder                                                                         |
| `key_meta`          | boolean                       | For the keyboard shortcut activation, is the CMD / CTRL key required to activate the HelpBar                          |
| `key_uid`           | string                        | For the keyboard shortcut activation, the letter to be used in combination with `key_meta` to activate the HelpBar    |
| `title_recent`      | string                        | The label given to the group of "Recent items"                                                                        |
| `title_suggestions` | string                        | The label given to the group of "Suggested items"                                                                     |
| `title_results`     | string                        | The label given to the group of "Custom Search Result items"                                                          |
| `published_at`      | timestamp                     | The time this was most recently published                                                                             |
| `url_group_ids`     | array&lt;ID&gt;               | The [`Environment`](apis/urls.md?id=url-groups) that this `Search` bar is enabled to run on                           |
| `groups`            | array&lt;SearchGroup&gt;      | The array of `SearchGroup` models                                                                                     |
| `label_themes`      | array&lt;SearchLabelTheme&gt; | The array of `SearchLabelTheme` models                                                                                |



## `SearchGroups` Schema :id=schema-search-groups

| Property         | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`             | ID        | The Chameleon ID                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `created_at`     | timestamp | When this happened or when this was added to the Database                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `updated_at`     | timestamp | The last time any property was updated                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `url`            | string    | The URL of the endpoint to                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `kind`           | string    | The kind of search to use for this group: One of: `public`, `private`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `title`          | string    | The label given to this group in the `Search` box                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `icon`           | object    | The `SearchIcon` info to display for all results of this `SearchGroup`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `icon.kind`      | string    | The "kind" of icon being used, one of `uid` or `image`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `icon.uid`       | string    | When using `kind="uid"`, a specific Chameleon supplied svg-based icon [2]. One of: `academic_cap`, `badge_check`, `beaker`, `bell`, `book_open`, `bulb`, `cake`, `calculator`, `calendar`, `chart_bar`, `chart_pie`, `chat_messages`, `chat_dots`, `chip`, `clipboard`, `clock`, `cloud_download`, `cloud`, `code`, `cog`, `color_swatch`, `connection`, `database`, `document_add`, `document_report`, `download`, `film`, `finger_print`, `fire`, `flag`, `folder`, `gift`, `globe`, `home`, `identification`, `key`, `leon`, `library`, `lightning_bolt`, `link`, `location_marker`, `map`, `microsurvey`, `music_note`, `paper_airplane`, `paper_clip`, `photograph`, `pop_out`, `presentation_chart`, `puzzle`, `qr_code`, `question_mark_circle`, `refresh`, `scale`, `search`, `segments`, `server`, `shield_check`, `sparkles`, `speakerphone`, `star`, `sun`, `support`, `table`, `tag`, `target`, `ticket`, `hammer`, `tooltip`, `signpost`, `truck`, `user_circle`, `user`, `users`, `variable`, `boards`, `grid`, `grid_add`, `list`, `warning`, `zoom_in`, `zoom_out`, `thumbs_up`, `thumbs_down`, `cube`, `company`, `click`, `hash`, or `toggle` |
| `icon.image_url` | string    | When using `kind="image"`, the url to an appropriate icon for this `SearchGroup`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `icon.image_alt` | string    | When using `kind="image"`, the alt text for the icon                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |



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
  "title_suggestions": "Recommended",
  "title_results": "Your Results"
}
```

Add two search groups of all help-center content on `help.your-product.com` and of all of your posts to your blog at `blog.your-product.com`.
Help center content defaults to the book `icon` and `film` for the blog content.

```json
{
  "groups": [
    {
      "kind": "public",
      "title": "Help center",
      "url": "https://help.your-product.com",
      "icon": {
        "kind": "uid",
        "uid": "book_open"
      }
    },
    {
      "kind": "public",
      "title": "Best practices",
      "url": "https://blog.your-product.com",
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
    "title_recent": "Recently clicked",
    "title_suggestions": "Recommended",
    "title_results": "Your Results",
    "published_at": "2029-04-07T12:18:00Z",
    "groups": [
      {
        "kind": "public",
        "title": "Help center",
        "url": "https://help.your-product.com",
        "icon": {
          "kind": "uid",
          "uid": "book_open"
        }
      },
      {
        "kind": "public",
        "title": "Best practices",
        "url": "https://blog.your-product.com",
        "icon": {
          "kind": "uid",
          "uid": "film"
        }
      }
    ],
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

A search item is a discrete unit of searchable content akin to a Google search result. You have content within your product, even if you don't think of it that way. Any database records that your Users would want to find is a piece of content. Send us this content to surface it to your Users in the Chameleon search bar

> `SearchItem`s are associated with `actions`: [SearchActions](apis/search.md?id=schema-search-actions), and `title_labels` / `description_labels`: [SearchLabels](apis/search.md?id=schema-search-labels)


| Property             | Type                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                 | ID                        | The Chameleon ID                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `created_at`         | timestamp                 | When this happened or when this was added to the Database                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `updated_at`         | timestamp                 | The last time any property was updated                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `uid`                | string                    | The external ID (from in your database) of the search content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `company_uid`        | string                    | The external ID (from in your database) of the [Company](apis/companies.md?id=schema) that has access to this `SearchItem`. This property is not sent back but is included here for clarity in how to use this API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `company_id`         | string                    | The Chameleon ID of the [Company](apis/companies.md?id=schema) that has access to this `SearchItem`. Only members of this company will be displayed this `SearchItem` as a search result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `title`              | string                    | The display title                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `description`        | string                    | The display description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `suggested_at`       | timestamp                 | Only `SearchItem`s with a timestamp here will show up in the "Suggested" / "Recommended" items reach results group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `icon`               | object                    | The `SearchIcon` info to display for all results of this `SearchGroup`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `icon.kind`          | string                    | The "kind" of icon being used, one of `uid` or `image`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `icon.uid`           | string                    | When using `kind="uid"`, a specific Chameleon supplied svg-based icon [2]. One of: `academic_cap`, `badge_check`, `beaker`, `bell`, `book_open`, `bulb`, `cake`, `calculator`, `calendar`, `chart_bar`, `chart_pie`, `chat_messages`, `chat_dots`, `chip`, `clipboard`, `clock`, `cloud_download`, `cloud`, `code`, `cog`, `color_swatch`, `connection`, `database`, `document_add`, `document_report`, `download`, `film`, `finger_print`, `fire`, `flag`, `folder`, `gift`, `globe`, `home`, `identification`, `key`, `leon`, `library`, `lightning_bolt`, `link`, `location_marker`, `map`, `microsurvey`, `music_note`, `paper_airplane`, `paper_clip`, `photograph`, `pop_out`, `presentation_chart`, `puzzle`, `qr_code`, `question_mark_circle`, `refresh`, `scale`, `search`, `segments`, `server`, `shield_check`, `sparkles`, `speakerphone`, `star`, `sun`, `support`, `table`, `tag`, `target`, `ticket`, `hammer`, `tooltip`, `signpost`, `truck`, `user_circle`, `user`, `users`, `variable`, `boards`, `grid`, `grid_add`, `list`, `warning`, `zoom_in`, `zoom_out`, `thumbs_up`, `thumbs_down`, `cube`, `company`, `click`, `hash`, or `toggle` |
| `icon.image_url`     | string                    | When using `kind="image"`, the url to an appropriate icon for this `SearchGroup`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `icon.image_alt`     | string                    | When using `kind="image"`, the alt text for the icon                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `actions`            | array&lt;SearchAction&gt; | An array of the [`SearchAction`](apis/search.md?id=schema-search-actions) that run when this `SearchItem` is clicked/selected in the HelpBar                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `title_labels`       | array&lt;SearchLabel&gt;  | An array of the [`SearchLabel`](apis/search.md?id=schema-search-labels) items displayed in the title of this `SearchItem`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `description_labels` | array&lt;SearchLabel&gt;  | An array of the [`SearchLabel`](apis/search.md?id=schema-search-labels) items displayed under the description of this `SearchItem`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |



## `SearchAction` Schema :id=schema-search-actions

| Property           | Type      | Description                                                                                                                                                                        |
|--------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `updated_at`       | timestamp | The last time any property was updated                                                                                                                                             |
| `kind`             | string    | The kind of action to take: One of: `url`, `navigate`, `event`, `identify`, `tour`, `survey`, `typeform`, `calendly`, `intercom`, `zendesk`, `help_scout`, `hubspot`, `chili_piper`, `script`, or `function` |
| `url`              | string    | When using `kind="url"` or `kind="navigate"` the new URL to load/use.                                                                                                              |
| `url_blank`        | boolean   | When using `kind="url"` does the URL open in a new tab?                                                                                                                            |
| `script`           | string    | When using `kind="script"` The specific JavaScript code snippet to run                                                                                                             |
| `tour_id`          | ID        | When using `kind="tour"` the Chameleon ID of the published Tour to start                                                                                                           |
| `survey_id`        | ID        | When using `kind="script"` the Chameleon ID of the published Microsurvey to start                                                                                                  |
| `event_name`       | string    | When using `kind="event"` the event name to track to your configured Integrations                                                                                                  |
| `identify_key`     | string    | When using `kind="identify"` the property "key" to send to your configured Integrations                                                                                            |
| `identify_value`   | string    | When using `kind="identify"` the property "value" to send to your configured Integrations                                                                                          |
| `intercom_message` | string    | When using `kind="intercom"` the message text to prefill in the messenger                                                                                                          |
| `typeform_url`     | string    | When using `kind="typeform"` the Typeform share URL to load                                                                                                                        |
| `zendesk_message`  | string    | When using `kind="zendesk"` the message text to send via Chat                                                                                                                      |
| `calendly_url`     | string    | When using `kind="calendly"` the specific scheduling URL to schedule with                                                                                                          |
| `hubspot_url`     | string    | When using `kind="hubspot"` the specific scheduling URL to schedule with                                                                                                            |




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

| param    | -        | description                                                                                                                 |
|----------|----------|-----------------------------------------------------------------------------------------------------------------------------|
| `limit`  | optional | Defaults to `50` with a maximum of `500`                                                                                    |
| `before` | optional | Used when paginating, use directly from the `cursor` object from the previous response                                      |
| `before` | optional | Read as "created `before`" and can be given as a timestamp to get only `limit` items that were created before this time     |
| `after`  | optional | Read as "created `after`" and can be given as a timestamp or ID to get only `limit` items that were created after this time |


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

Use any of the properties available in the [schema](apis/search.md?id=schema-search-items) with the addition of `company_uid`. To associate this `SearchItem` with a [Company](apis/companies.md), send the same UID you will send to `chmln.identify` for this Company.

You must always send a `uid` field as the unique identifier for a piece of content. When content relates to a specific database item, include the database ID of that record in the `uid`

#### HTTP Request

```
POST https://api.trychameleon.com/v3/edit/search_items
```

###### Examples

Add a specific key action within your product for the Company in your DB with ID=14203, navigate to the onboarding page

```json
{
  "uid": "data-onboarding",
  "title": "Data onboarding",
  "description": "The first step in making the switch is to import your first round of data.",
  "company_uid": "14203",
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


## Delete a `SearchItem`s :id=search-items-destroy

Send the `uid` of a previously created `SearchItem`.


#### HTTP Request

```
DELETE https://api.trychameleon.com/v3/edit/search_items
```



----

## Search Item Importing via CSV :id=schema-search-imports

| Property                    | Type      | Description                                                                                                                                                              |
|-----------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                        | ID        | The Chameleon ID                                                                                                                                                         |
| `created_at`                | timestamp | When this happened or when this was added to the Database                                                                                                                |
| `updated_at`                | timestamp | The last time any property was updated                                                                                                                                   |
| `file`                      | File      | The file to import, please use the [template](apis/search.md?id=search-imports-template) or [example](apis/search.md?id=search-imports-example) to make this easier.     |
| `filename`                  | string    | The name of the original file uploaded                                                                                                                                   |
| `head_columns`              | array     | A list representing the parsed version of the first 5 lines. Each object has a header column `name` and `values` are an ordered array of the next 4 rows for that column |
| `stats`                     | object    | The details of the data itself and of the last run of this SearchImport                                                                                                  |
| `stats.rows_count`          | number    | The number of rows in the file                                                                                                                                           |
| `stats.last_row`            | number    | The row number of the most recent processed row (used for mid-import progress bar)                                                                                       |
| `stats.last_import_state`   | string    | The current state of the import                                                                                                                                          |
| `stats.last_import_error`   | string    | A representation of the error the last import encountered                                                                                                                |
| `stats.last_import_at`      | timestamp | The last time this import was run                                                                                                                                        |
| `stats.last_import_elapsed` | number    | The total time (in seconds) that the import took.                                                                                                                        |
| `stats.created_count`       | number    | The number of records created by this Import                                                                                                                             |
| `stats.updated_count`       | number    | The number of records updated by this Import                                                                                                                             |
| `stats.deleted_count`       | number    | The number of records removed by this Import                                                                                                                             |



## Download the Search Import CSV template :id=search-imports-template

Start here when adding your product's navigation to the Chameleon HelpBar

#### HTTP Request

```
GET https://api.trychameleon.com/v3/edit/search_imports/template
```

## Download the Search Import CSV example :id=search-imports-example

Use this example to see what is possible when adding your product's navigation to the Chameleon HelpBar

#### HTTP Request

```
GET https://api.trychameleon.com/v3/edit/search_imports/example
```


## Create a Search Import :id=search-imports-create

Use `Content-Type: multipart/form-data` to create an Import in one request, include the `file` parameter with a CSV based on the [template](apis/search.md?id=search-imports-template) or [example](apis/search.md?id=search-imports-example).

#### HTTP Request

```
POST https://api.trychameleon.com/v3/edit/search_imports
```

## Get a Search Import :id=search-imports-show

Useful to track the progress of this import

#### HTTP Request

```
GET https://api.trychameleon.com/v3/edit/search_imports/:id
```



-----

## Search JavaScript API :id=search-js-api

At a high level, Chameleon uses the `chmln` object on the page via `chmln.on` to allow you to control the HelpBar experience. **All of these event listeners are optional**.

See the [Type definitions below ↓](apis/search.md?id=search-js-types)

##### Recommended

> When using React, add `<ChmlnHook>` at the same level as your Router => https://www.npmjs.com/package/@chamaeleonidae/chmln

```javascript

chmln.on('app:navigate', (opts: NavigateOpts) => {
  /*
  Nagivate with React router / Vue router / pushState / call window.open / etc.

  Frameworks:
    - React info here => https://www.npmjs.com/package/@chamaeleonidae/chmln
    - Add more frameworks with a PR to this file and receive a $50 gift card

  opts.to is the url configured in the SearchAction configured with `kind=navigate`

  */
});
```

##### Optional

```javascript

chmln.on('helpbar:search', (opts: SearchOpts, ctx: Context) => {
  /*
  Optional:
    - Chameleon will handle search for you
    - If you need to add custom "Search" logic use this event to pass back the right items, two options:
      - directly return an array<SearchItem>
      - return a Promise that will resolve with the first argument being an array<SearchItem>.
    - Best used when you already use Algolia or have a custom search endpoint internally

  Called when:
    - The User has entered in a query; when a user enters text and pauses

   return array<SearchItem>
   return Promise that resolves with the first argument as array<SearchItem>
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

chmln.on('helpbar:items:suggestions', (opts: BlankOpts, ctx: Context) => {
  /*
  Optional:
    - Chameleon will handle suggestions for you
    - If you need to add custom "Suggestion items" logic use this event to pass back the right items

  Called when:
    - the HelpBar needs a list of the suggestions

  return Array or Promise of suggestions to display
  return null (or don't implement) to use the suggested items as added to Chameleon backend via SearchItem

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


