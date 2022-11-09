# Data Imports

Imports are used to add data to Chameleon via CSV. Each row should correspond with one record in the Chameleon database (called a model below).
You may Import data into a [User Profiles](apis/profiles.md) or a [Company](apis/companies.md) with the `model_kind` property.

When using a CSV to create new records that are not yet in Chameleon, you must provide a mapping to the `uid` property, this is the same value you pass to `chmln.identify` via the [JS API](js/profiles.md).

Using a tagging `kind` (`tag_csv` or `tag_filters`) will either create a new User Tag or a new Company Tag and add all of the matching models to the new Tag.

## Schema :id=schema

| Property                    | Type                  | Description |
|-----------------------------|-----------------------| --- |
| `id`                        | ID                    | The Chameleon ID |
| `created_at`                | timestamp             | When this happened or when this was added to the Database |
| `updated_at`                | timestamp             | The last time any property was updated |
| `name`                      | string                | The name given by an administrator of Chameleon |
| `kind`                      | string                | The kind of Import to be processed: One of `tag_csv`, `tag_filters`, `update_csv`, `delete_csv` or `delete_filters` |
| `model_kind`                | string                | The target data collection to update: One of `profile` or `company`. Note that deleting companies is not currently supported. |
| `tag_import_id`             | ID                    | To add members to a previous Import, specify this as the ID of a previous Import |
| `on_model_missing`          | string                | The strategy to use when data present in the Import is missing in Chameleon (i.e. [User Profile](apis/profiles.md) or [Company](apis/companies.md) has **not yet** been identified to Chameleon): One of `create` or `ignore` |
| `head_columns`              | array&lt;Object&gt;   | A list representing the parsed version of the first 5 lines. Each object has a header column `name` and `values` are an ordered array of the next 4 rows for that column |
| `import_at`                 | timestamp             | The "trigger" to start the importing process (for convenience, use the string `$now`). At this point, the CSV upload is completed, all `properties` are confirmed, and the Import starts |
| `properties`                | array&lt;Property&gt; | The list of definitions of how to map CSV column headers to [Properties](apis/properties.md) on the model. [example ↓](apis/imports.md?id=examples-profiles-tag-all) |
| `properties.$.name`         | string                | The column header of this property in the CSV file |
| `properties.$.prop`         | string                | The `prop` value of the [Property](apis/properties.md) to store on the model. New properties are created dynamically for missing `prop` values. |
| `filters`                   | array&lt;SegmentFilter&gt; | For filter-based imports, an array of items that each define a [Segmentation Filter expression](concepts/filters.md) |
| `stats`                     | object                | The details of the data itself and of the last run of this Import |
| `stats.data_size`           | number                | The number of bytes contained in the uploaded file |
| `stats.rows_count`          | number                | The number of rows in the file |
| `stats.last_row`            | number                | The row number of the most recent processed row (used for mid-import progress bar) |
| `stats.last_import_state`   | string                | The current state of the import: One of `started`, `completed`, `retrying`, or `error` |
| `stats.last_import_error`   | string                | A representation of the error the last import encountered |
| `stats.last_import_at`      | timestamp             | The last time this import was run |
| `stats.last_import_elapsed` | number                | The total time (in seconds) that the import took. |
| `stats.created_count`       | number                | The number of records created by this Import |
| `stats.updated_count`       | number                | The number of records updated by this Import |

------

## Limitations :id=limits

- Imports must be less than 50MB (200MB on the Growth plan) [1]
- Imports must be less 20 columns (100 on the Growth plan) [1]
- Only 20 Imports total can be created (50 on the Growth plan) [1]
 - Imports "Tags" can be reused with `tag_import_id`, reused imports do not count against this limit.
- Once an Import is marked as triggered (when `import_at` has a timestamp value) the Import can no longer be updated.
- Only one Import will be run concurrently (though many can be triggered at the same time)

> [1] Import limits can be increased on an Growth / Enterprise plan. [Contact us](https://app.trychameleon.com/help) to talk about your use case.


------

## List all Imports :id=imports-index

#### HTTP Request

```
GET https://api.trychameleon.com/v3/edit/imports
```


```json
{
  "imports": [
    {
      "id": "5f3c4232c712de665632a6d9",
      "kind": "tag_csv",
      "name": "Feedback Request: Post-BETA1",
      "model_kind": "profile",
      "properties": [
        {
          "name": "User ID",
          "prop": "uid"
        }
      ],
      "head_columns": [
        {
          "name": "User ID",
          "values": ["5a1fe53", "621f8e7"]
        }
      ],
      "stats": {
        "rows_count": 142934,
        "last_row": 112000,
        "last_import_state": "started",
        "last_import_at": null
      },
      ...
    },
    ...
  ]
}
```


## Create an Import :id=imports-create

- Check out the [cURL Examples](apis/imports.md?id=examples-all-curl) below to see this in action.

#### HTTP Request

```
POST https://api.trychameleon.com/v3/edit/imports
```

| param               | -        | type                  | description    |
| ------------------- |----------|-----------------------| -------------- |
| `name`              | optional | string                | The name given to this Import, defaults to `<Your name>'s Import - <DATE>` |
| `kind`              | optional | string                | The kind of Import to be processed: One of `tag_csv`, `tag_filters`, `update_csv`, `delete_csv` or `delete_filters`. Defaults to `tag_csv` |
| `model_kind`        | optional | string                | The target data collection to update: One of `profile` or `company`. Defaults to `profile` |
| `tag_import_id`     | optional | ID                    | To add members to a previous Import, specify this as the ID of a previous Import |
| `on_model_missing`  | optional | string                | The strategy to use when data present in the Import is missing in Chameleon (i.e. a User Profile or Company has **not yet** been identified to Chameleon): One of `create` or `ignore`. Defaults to `create` |
| `properties`        | required | array&lt;Property&gt; | The list of definitions of how to map CSV column headers to [Properties](apis/properties.md) on the model. |
| `properties.$.name` | required | string                | The column header of this property in the CSV file |
| `properties.$.prop` | required | string                | The `prop` value of the [Property](apis/properties.md) to store on the model |
| `file`              | required | File                  | The CSV file to be imported |
| `filters`                   | array&lt;SegmentFilter&gt; | For filter-based imports, an array of items that each define a [Segmentation Filter expression](concepts/filters.md) |
| `import_at`         | optional | timestamp             | The "trigger" to start the importing process. At this point, the CSV upload is completed, all `properties` are confirmed, and the import starts |

> For CSV-based import `kind`, both valid `properties` and `file` are required before `import_at` can be set.

##### Errors (for both `create` and `update`)

- When the Import has already been started (when `import_at` has a value).
- When the `on_model_missing` is `create` and the `uid` property is not mapped in properties.
- When any of the supplied `properties` are not found as Headers in the uploaded file.
- When the `tag_import_id` refers to an import that has not been finished


| Code  | description                                                                                                            |
|-------|------------------------------------------------------------------------------------------------------------------------|
| `409` | Once an Import has been started it cannot be updated                                                                   |
| `409` | The number of Imports limit has been reached, see [limits ↑](apis/imports.md?id=limits) for details                    |
| `422` | The `kind`, `model_kind`, or `on_model_missing` have unrecognized values                                               |
| `422` | The `properties` contains a `name` that was not found as a header in the CSV                                           |
| `422` | The `on_model_missing` is `create` and the `uid` property is not mapped in properties.                                 |
| `422` | The `import_at` was sent before both `properties` and `file` was set                                                   |
| `422` | The file is larger than the current limits [limits ↑](apis/imports.md?id=limits) allow                                 |
| `422` | The file has more columns than the current limits [limits ↑](apis/imports.md?id=limits) allow                          |
| `422` | The `kind=tag_csv` + `model_kind=profile` and `properties` does not map to a `uid` or `email`                          |
| `422` | The `kind=tag_csv` + `model_kind=company` and `properties` does not map to a `uid`                                     |
| `422` | The `tag_import_id` refers to an import that has not been finished (when `stats.last_import_state` is not `completed`) |


##### Errors during Import

- When an error occurs during the Import, the `stats.last_import_state` will change to `retrying` or `error` and `stats.last_import_error` will have a value.


##### Using `kind=tag_csv` to tag User Profiles via a User ID :id=examples-profiles-tag-all

> This will be the same User ID you send to Chameleon when calling `chmln.identify` => [Identifying Users](js/profiles.md).

With a CSV `file` like this, specify the header of `User ID` as mapping to the Chameleon User Profile field of `uid`.

```text
User ID
5a1fe53
621f8e7
```

Request:

```json
{
  "kind": "tag_csv",
  "name": "Feedback Request: Post-BETA1",
  "model_kind": "profile",
  "properties": [
    {
      "name": "User ID",
      "prop": "uid"
    }
  ],
  ...
}
```

Response:

```json
{
  "import": {
    ...
    "head_columns":[
      {
        "name": "User ID",
        "values": ["5a1fe53", "621f8e7"]
      }
    ]
  }
}
```

##### Using `kind=tag_csv` to tag User Profiles with Email

With a CSV `file` like this, specify the header of `Email address` as mapping to the Chameleon User Profile field of `email`.

> You must set `on_model_missing` to `ignore` because no field maps to the `uid` Property.

```text
Email address
jill@sample.com
aaron@example.com
```

Request:

```json
{
  "kind": "tag_csv",
  "name": "Feedback Request: Post-BETA2",
  "on_model_missing": "ignore",
  "properties": [
    {
      "name": "Email address",
      "prop": "email"
    }
  ],
  ...
}
```

Response:

```json
{
  "import": {
    ...
    "head_columns": [
      {
        "name":"Email address",
        "values": ["jill@sample.com", "aaron@example.com"]
      }
    ]
  }
}
```


##### Using `kind=tag_csv` to tag Companies via a Company ID :id=examples-companies-tag-all

> This will be the same Company ID you send to Chameleon when calling `chmln.identify` => [Identifying Company](js/profiles.md?id=company).

With a CSV `file` like this, specify the header of `Company ID` as mapping to the Chameleon Company field of `uid`.

```text
Company ID
721f8e8
6a1fe54
```

Request:

```json
{
  "kind": "tag_csv",
  "name": "Company Feedback Request: Post-BETA1",
  "model_kind": "company",
  "properties": [
    {
      "name": "Company ID",
      "prop": "uid"
    }
  ],
  ...
}
```

Response:

```json
{
  "import": {
    ...
    "head_columns": [
      {
        "name": "Company ID",
        "values": ["721f8e8", "6a1fe54"]
      }
    ]
  }
}
```

##### Using `kind=update_csv` to update User Profile data :id=examples-profiles-update-all

With a CSV `file` like this, use `properties` to specify the headers as mapped to the `prop` field of Chameleon [Property](apis/properties.md).

```text
User ID,User Role,Role ICP Fit
5a1fe53,Customer Success Engineer,63
621f8e7,Customer Success Manager,88
```

Request:

```json
{
  "kind": "tag_csv",
  "name": "Feedback Request: Post-BETA1",
  "model_kind": "profile",
  "properties": [
    {
      "name": "User ID",
      "prop": "uid"
    },
    {
      "name": "User Role",
      "prop": "role"
    },
    {
      "name": "Role ICP Fit",
      "prop": "role_fit"
    }
  ],
  ...
}
```

Response:

```json
{
  "import": {
    ...
    "head_columns": [
      {
        "name": "User ID",
        "values": ["5a1fe53", "621f8e7"]
      },
      {
        "name": "User Role",
        "values": ["Customer Success Engineer", "Customer Success Manager"]
      },
      {
        "name": "Role ICP Fit",
        "values": [63, 68]
      }
    ]
  }
}
```

##### Using `kind=delete_csv` to delete User Profiles via a User ID :id=examples-profiles-delete-by-id

> This will be the same User ID you send to Chameleon when calling `chmln.identify` => [Identifying Users](js/profiles.md).

With a CSV `file` like this, specify the header of `User ID` as mapping to the Chameleon User Profile field of `uid`.

```text
User ID
5a1fe53
621f8e7
```

Request:

```json
{
  "kind": "delete_csv",
  "name": "Data deletion request 54Dw",
  "model_kind": "profile",
  "properties": [
    {
      "name": "User ID",
      "prop": "uid"
    }
  ],
  ...
}
```

Response:

```json
{
  "import": {
    ...
    "head_columns":[
      {
        "name": "User ID",
        "values": ["5a1fe53", "621f8e7"]
      }
    ]
  }
}
```

##### Using `kind=delete_csv` to delete User Profiles with Email :id=examples-profiles-delete-by-email

With a CSV `file` like this, specify the header of `Email address` as mapping to the Chameleon User Profile field of `email`.


```text
Email address
jill@sample.com
aaron@example.com
```

Request:

```json
{
  "kind": "delete_csv",
  "name": "Data deletion request 65fx",
  "on_model_missing": "ignore",
  "properties": [
    {
      "name": "Email address",
      "prop": "email"
    }
  ],
  ...
}
```

Response:

```json
{
  "import": {
    ...
    "head_columns": [
      {
        "name":"Email address",
        "values": ["jill@sample.com", "aaron@example.com"]
      }
    ]
  }
}
```


#### HTTP Response

```json
{
  "import": {
    "id": "5f3c4232c712de665632a6d9",
    "kind": "tag_csv",
    "name": "Feedback Request: Post-BETA1",
    "model_kind": "profile",
    "properties": [
      {
        "name": "User ID",
        "prop": "uid"
      }
    ],
    ...
  }
}
```

## Show an Import :id=imports-show

Get information about the this Import which is typically used to track the Import's progress and to know when it finishes.
Use `stats.rows_count` and `stats.last_row` to give a percentage complete.
The Import is finished when `stats.last_import_state` is `completed`, at that point all other `stats` keys will have a relevant values. (i.e. `stats.last_import_at` and `stats.last_import_elapsed`).

#### HTTP Request

```
GET https://api.trychameleon.com/v3/edit/imports/:id
```

| param | -        | description                                                  |
| ----- | -------- | ------------------------------------------------------------ |
| `id`    | required | The Chameleon ID of the Import                         |


#### HTTP Response

```json
{
  "import": {
    "id": "5f3c4232c712de665632a6d9",
    "kind": "tag_csv",
    "name": "Feedback Request: Post-BETA1",
    "model_kind": "profile",
    "properties": [...],
    "stats": {
      "rows_count": 142934,
      "last_row": 112000,
      "last_import_state": "started",
      "last_import_at": null,
      "created_count": 921,
      "updated_count": 111079
    },
    ...
  }
}
```


## Update an Import :id=imports-update

> The main reason to update an import is to "capture a workflow" or to separately upload the CSV file for convenience via `cURL`.
> A workflow is typical of an Import UI but not typical of an API

#### HTTP Request

```
PATCH https://api.trychameleon.com/v3/edit/imports/:id
```

**See options for [Creating an Import](apis/imports.md?id=imports-create)**




--------



## cURL Examples :id=examples-all-curl

To [Authenticate](concepts/authentication.md), replace `ACCOUNT_SECRET` below with your secret token. This can be generated on your [dashboard](https://app.trychameleon.com/integrations/tokens).


<details>
<summary>Tagging User Profiles by <b>UID</b></summary>

- `kind=tag_csv` + `model_kind=profile` means Tag Users Profiles by CSV.
- Using `on_model_missing=create` means that any User Profile that is not found by UID will be added to Chameleon and Tagged with the Import `name`.

With a CSV like this (`feedback-request-post-BETA1.csv`):

```text
User ID
c4235f3
2de2c71
632665
```

First, Create the import, naming it and mapping the `User ID` CSV header to the `uid` Chameleon property:

```bash
curl -X POST -H 'X-Account-Secret: ACCOUNT_SECRET' \
  -H 'Content-Type: application/json' \
  -d '{"name": "Feedback Request: Post-BETA1", "model_kind": "profile", "kind": "tag_csv", "on_model_missing": "create", "properties": [{"name":"User ID","prop":"uid"}] }' \
  'https://api.trychameleon.com/edit/v3/imports'
```

Then Upload the CSV called `feedback-request-post-BETA1.csv` and trigger the import with `import_at=now`

- Use the `import.id` from the last request in place of IMPORT_ID:

```bash
curl -X PATCH -H 'X-Account-Secret: ACCOUNT_SECRET' \
  -F file=@feedback-request-post-BETA1.csv \
  'https://api.trychameleon.com/edit/v3/imports/IMPORT_ID?import_at=now'
```

Optional: Check on the Import status:

```bash
curl -H 'X-Account-Secret: ACCOUNT_SECRET' 'https://api.trychameleon.com/edit/v3/imports/IMPORT_ID'
```

</details>


<details>
<summary>Tagging User Profiles by <b>Email</b></summary>

- `kind=tag_csv` + `model_kind=profile` means Tag Users Profiles by CSV.
- Using `on_model_missing=create` means that any User Profile that is not found by UID will be added to Chameleon and Tagged with the Import `name`.

With a CSV like this (`feedback-request-post-BETA1.csv`):

```text
Email address
jill@example.co
jess@product.io
jamie@example.com
```

First, Create the import, naming it and mapping the `Email address` CSV header to the `email` Chameleon property:

```bash
curl -X POST -H 'X-Account-Secret: ACCOUNT_SECRET' \
  -H 'Content-Type: application/json' \
  -d '{"name": "Feedback Request: Post-BETA1", "model_kind": "profile", "kind": "tag_csv", "on_model_missing": "create", "properties": [{"name":"Email address","prop":"email"}] }' \
  'https://api.trychameleon.com/edit/v3/imports'
```

Then Upload the CSV called `feedback-request-post-BETA1.csv` and trigger the import with `import_at=now`

- Use the `import.id` from the last request in place of IMPORT_ID:

```bash
curl -X PATCH -H 'X-Account-Secret: ACCOUNT_SECRET' \
  -F file=@feedback-request-post-BETA1.csv \
  'https://api.trychameleon.com/edit/v3/imports/IMPORT_ID?import_at=now'
```

Optional: Check on the Import status:

```bash
curl -H 'X-Account-Secret: ACCOUNT_SECRET' 'https://api.trychameleon.com/edit/v3/imports/IMPORT_ID'
```

</details>


<details>
<summary>Tagging Companies by <b>UID</b></summary>

- `kind=tag_csv` + `model_kind=company` means Tag Companies by CSV.
- Using `on_model_missing=create` means that any Companies that are not found by UID will be added to Chameleon and Tagged with the Import `name`.

With a CSV like this (`feedback-request-accounts-post-BETA1.csv`):

```text
Company ID
5f3c423
2c712de
665632
```

First, Create the import, naming it and mapping the `Company ID` CSV header to the `uid` Chameleon property:

```bash
curl -X POST -H 'X-Account-Secret: ACCOUNT_SECRET' \
  -H 'Content-Type: application/json' \
  -d '{"name": "Feedback Request Accounts: Post-BETA1", "model_kind": "company", "kind": "tag_csv", "on_model_missing": "create", "properties": [{"name":"Company ID","prop":"uid"}] }' \
  'https://api.trychameleon.com/edit/v3/imports'
```

Then Upload the CSV called `feedback-request-accounts-post-BETA1.csv` and trigger the import with `import_at=now`

- Use the `import.id` from the last request in place of IMPORT_ID:

```bash
curl -X PATCH -H 'X-Account-Secret: ACCOUNT_SECRET' \
  -F file=@feedback-request-accounts-post-BETA1.csv \
  'https://api.trychameleon.com/edit/v3/imports/IMPORT_ID?import_at=now'
```

Optional: Check on the Import status:

```bash
curl -H 'X-Account-Secret: ACCOUNT_SECRET' 'https://api.trychameleon.com/edit/v3/imports/IMPORT_ID'
```

</details>

<details>
<summary>Tagging User Profiles using Filters</summary>

- `kind=tag_filters` + `model_kind=profile` means Tag Users Profiles matching the given Filters.

```bash
curl -X POST -H 'X-Account-Secret: ACCOUNT_SECRET' \
  -H 'Content-Type: application/json' \
  -d '{"name": "Gmail users", "model_kind": "profile", "kind": "tag_filters", "filters": [{"kind": "property", "prop": "email", "op": "in", "value": "gmail.com"}], "import_at": "$now"}' \
  'https://api.trychameleon.com/edit/v3/imports'
```

Optional: Check on the Import status:

```bash
curl -H 'X-Account-Secret: ACCOUNT_SECRET' 'https://api.trychameleon.com/edit/v3/imports/IMPORT_ID'
```

</details>

<details>
<summary>Deleting User Profiles by <b>UID</b></summary>

- `kind=delete_csv` + `model_kind=profile` means Delete Users Profiles by CSV.

With a CSV like this (`data-deletion-request-54Dw.csv`):

```text
User ID
c4235f3
2de2c71
632665
```

First, Create the import, naming it and mapping the `User ID` CSV header to the `uid` Chameleon property:

```bash
curl -X POST -H 'X-Account-Secret: ACCOUNT_SECRET' \
  -H 'Content-Type: application/json' \
  -d '{"name": "Data deletion request 54Dw", "model_kind": "profile", "kind": "delete_csv", "properties": [{"name":"User ID","prop":"uid"}] }' \
  'https://api.trychameleon.com/edit/v3/imports'
```

Then Upload the CSV called `data-deletion-request-54Dw.csv` and trigger the import with `import_at=now`

- Use the `import.id` from the last request in place of IMPORT_ID:

```bash
curl -X PATCH -H 'X-Account-Secret: ACCOUNT_SECRET' \
  -F file=@data-deletion-request-54Dw.csv \
  'https://api.trychameleon.com/edit/v3/imports/IMPORT_ID?import_at=now'
```

Optional: Check on the Import status:

```bash
curl -H 'X-Account-Secret: ACCOUNT_SECRET' 'https://api.trychameleon.com/edit/v3/imports/IMPORT_ID'
```

</details>


<details>
<summary>Deleting User Profiles by <b>Email</b></summary>

- `kind=delete_csv` + `model_kind=profile` means Delete Users Profiles by CSV.

With a CSV like this (`data-deletion-request-54Dw.csv`):

```text
Email address
jill@example.co
jess@product.io
jamie@example.com
```

First, Create the import, naming it and mapping the `Email address` CSV header to the `email` Chameleon property:

```bash
curl -X POST -H 'X-Account-Secret: ACCOUNT_SECRET' \
  -H 'Content-Type: application/json' \
  -d '{"name": "Feedback Request: Post-BETA1", "model_kind": "profile", "kind": "delete_csv", "properties": [{"name":"Email address","prop":"email"}] }' \
  'https://api.trychameleon.com/edit/v3/imports'
```

Then Upload the CSV called `data-deletion-request-54Dw.csv` and trigger the import with `import_at=now`

- Use the `import.id` from the last request in place of IMPORT_ID:

```bash
curl -X PATCH -H 'X-Account-Secret: ACCOUNT_SECRET' \
  -F file=@data-deletion-request-54Dw.csv \
  'https://api.trychameleon.com/edit/v3/imports/IMPORT_ID?import_at=now'
```

Optional: Check on the Import status:

```bash
curl -H 'X-Account-Secret: ACCOUNT_SECRET' 'https://api.trychameleon.com/edit/v3/imports/IMPORT_ID'
```

</details>

<details>
<summary>Deleting User Profiles using Filters</summary>

- `kind=delete_filters` + `model_kind=profile` means Delete Users Profiles matching the given Filters.

```bash
curl -X POST -H 'X-Account-Secret: ACCOUNT_SECRET' \
  -H 'Content-Type: application/json' \
  -d '{"name": "Remove users not seen in a year", "model_kind": "profile", "kind": "tag_filters", "filters": [{"kind": "property","prop":"last_seen_at","op":"lt-d","value":"365"}], "import_at": "$now"}' \
  'https://api.trychameleon.com/edit/v3/imports'
```

Optional: Check on the Import status:

```bash
curl -H 'X-Account-Secret: ACCOUNT_SECRET' 'https://api.trychameleon.com/edit/v3/imports/IMPORT_ID'
```

</details>






----------


