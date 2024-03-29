# Changes

**Changes are a record of every update made to your key models (Experiences).**

- [Tours](apis/tours.md)
- [Mirosurveys](apis/surveys.md)
- [Launchers](apis/launchers.md)
- [Tooltips](apis/tooltips.md)
- [Steps](apis/steps.md)

---

Use the feed of changes to:

- Export a paper trail to know which changes made the biggest impact.
- Ensure that your most important Experiences stay static. Do this by listing all changes for a specific Experience and make sure the set of changes is empty
- Audit an issue with the delivery of an Experience.

## Schema :id=schema


| Property        | Type      | Description                                                                                                                                                                                                           |
|-----------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`            | ID        | The Chameleon ID                                                                                                                                                                                                      |
| `created_at`    | timestamp | When this happened or when this was added to the Database                                                                                                                                                             |
| `updated_at`    | timestamp | The last time any property was updated                                                                                                                                                                                |
| `experience_id` | ID        | The ID of the parent model that this change represents. (a [Tour](apis/tour.md) when model is a [Step](apis/steps.md)                                                                                                 |
| `model_id`      | ID        | The ID of the model that this change represents                                                                                                                                                                       |
| `model_type`    | string    | The type of the model that this change represents                                                                                                                                                                     |
| `kind`          | string    | The type of change this represents: One of: `create`, `update`, `destroy`, `raw`, `partial`, `related`, `revert`, or `apply`                                                                                          |
| `path`          | string    | They keypath this change represents                                                                                                                                                                                   |
| `object`        | object    | The underlying value of this change. It can be an object with scalar values (for a `kind=create` or `kind=destroy`) or values as a 2-item array of the [`before`, `after`] [diff](api/changes.md?id=schema-diff-item) |
| `options`       | object    | A hash of other information about this change. Values are a [diff](api/changes.md?id=schema-diff-item).                                                                                                               |


### Change "Diff item" Schema :id=schema-diff-item

Each value is a 2-item array `[BEFORE, AFTER]`. If the value changed from `"silver"` to `"gold"` then:

```
["silver", "gold"]
```

In the context of a Change `object`:

```json
{
  "plan": ["silver", "gold"],
  "monthly_spend": [99, 249]
}
```

## List Changes :id=changes-index

List all Changes.

#### HTTP Request

```
GET https://api.chameleon.io/v3/edit/changes
GET https://api.chameleon.io/v3/edit/:model_kind/:model_id/changes
```

| param        | -        | description                                                                                                                 |
|--------------|----------|-----------------------------------------------------------------------------------------------------------------------------|
| `limit`      | optional | Defaults to `50` with a maximum of `500`                                                                                    |
| `before`     | optional | Used when paginating, use directly from the `cursor` object from the previous response                                      |
| `before`     | optional | Read as "created `before`" and can be given as a timestamp to get only `limit` items that were created before this time     |
| `after`      | optional | Read as "created `after`" and can be given as a timestamp or ID to get only `limit` items that were created after this time |
| `filters`    | optional | An array of properties to filter `Changes` with; use this to fetch "all changes for a specific set of properties"           |
| `model_kind` | optional | A `kind` of model to fetch changes for. One of `tour`, `survey`, `launcher`, or `tooltip`.                                  |
| `model_id`   | optional | The ID of the model to fetch changes for                                                                                    |


##### Examples

Only changes for the `6f3c4232c712de665632a6d5` Tour

```
GET https://api.chameleon.io/v3/edit/tours/6f3c4232c712de665632a6d5/changes
```

Only changes to the `published_at` property of any Experience

```
GET https://api.chameleon.io/v3/edit/changes?filter=published_at
```


#### HTTP Response

```json
{
  "changes": [
    {
      "id": "6f3c4232c712de665632a6d5",
      "created_at": "2029-04-07T12:38:00Z",
      "experience_id": "6f3c1931c712d632a6d5e665",
      "model_id": "6f3c1931c712d632a6d5e665",
      "model_type": "Campaign",
      "kind": "create",
      "path": "model",
      "object": {
        "id": "6f3c1931c712d632a6d5e665",
        "name": "New data importing options",
        ...
      },
      ...
    },
    {
      "id": "6f3c4232c712de665632a6d6",
      "created_at": "2029-04-07T12:38:00Z",
      "experience_id": "6f3c1931c712d632a6d5e665",
      "model_id": "6e3c193a6d5e51c712d63266",
      "model_type": "Step",
      "kind": "create",
      "path": "model",
      "object": {
        "id": "6f3c1931c712d632a6d5e665",
        "body": "### We've updated all of the data things!",
        ...
      },
      ...
    },
    {
      "id": "6f3c4232c712de665632a6d6",
      "created_at": "2029-04-07T12:38:00Z",
      "experience_id": "6f3c1931c712d632a6d5e665",
      "model_id": "6e3c193a6d5e51c712d63266",
      "model_type": "Step",
      "kind": "create",
      "path": "model",
      "object": {
        "body": ["### We've updated all of the data things!", "### We've upgraded the data things!"],
        "modal_width": [450, 520],
        ...
      },
      "object": {
        "capture_id": ["6d3c4232c665632a712de2f1", "6d3c423665632a2c712de2f7"]
      },
      ...
    },
    ...
  ],
  "cursor": {
    "limit": 50,
    "before": "6f3c4232c712de665632a6d6"
  }
}
```


# Summary of Changes

## Summary Schema :id=schema-summary

| Property     | Type                       | Description                                                                                                                                                                                                            |
|--------------|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `model_id`   | ID                         | The ID of the model that this change represents                                                                                                                                                                        |
| `path`       | string                     | They keypath this change represents                                                                                                                                                                                    |
| `kind`       | string                     | The type of change this represents: One of: `create`, `update`, `destroy`                                                                                                                                              |
| `change_id`  | array                      | A 2-item array of the [`before`, `after`] [diff](api/changes.md?id=schema-diff-item) of Screen Capture ID of this change. Note some changes are no represented visually and will have null value for the `after` value |
| `capture_id` | array                      | A 2-item array of the [`before`, `after`] [diff](api/changes.md?id=schema-diff-item) of Screen Capture ID of this change. Note some changes are no represented visually and will have null value for the `after` value |
| `object`     | object&lt;ChangeUpdate&gt; | A [ChangeUpdate](api/changes.md?id=schema-summary-change-update-item) of properties that have changed for this model                                                                                                   |
| `changes`    | array&lt;ChangeUpdate&gt;  | An Array of [ChangeUpdate](api/changes.md?id=schema-summary-change-update-item) items representing changes to child associated models ([Steps](apis/steps.md), [Buttons](apis/buttons.md) etc.                         |



### Change update object Schema :id=schema-summary-change-update-item

| Property      | Type   | Description                                                                                                                                                                                                           |
|---------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`        | string | The name of the underlying property that changed                                                                                                                                                                      |
| `description` | string | A longer description of the underlying property                                                                                                                                                                       |
| `value`       | object | The underlying value of this change. It can be an object with scalar values (for a `kind=create` or `kind=destroy`) or values as a 2-item array of the [`before`, `after`] [diff](api/changes.md?id=schema-diff-item) |

##### Examples

```json
{
  "name": "Step created",
  "description": null,
  "value": {
    "id": "6f3c4232c712de665632a6d6",
    ...
  }
}
```


```json
{
  "name": "Body",
  "description": "The content of the Step",
  "value": ["New features are here!", "New features have arrived!"],
}
```


## Change Summary :id=change-summary-index

List all Change Summaries

#### HTTP Request

```
GET https://api.chameleon.io/v3/edit/:model_kind/:model_id/changes/summary
```

| param        | -        | description                                                                                |
|--------------|----------|--------------------------------------------------------------------------------------------|
| `model_kind` | required | A `kind` of model to fetch changes for. One of `tour`, `survey`, `launcher`, or `tooltip`. |
| `model_id`   | required | The ID of the model to fetch changes for                                                   |



#### HTTP Response

```json
{
  "model_id": "6f3c1931c712d632a6d5e665",
  "kind": "create",
  "change_id": [
    "5e3c4232c712de665632a6d9",
    "5f3c42665632a6d932c712de"
  ],
  "path": "model",
  "object": {
    "id": "6f3c1931c712d632a6d5e665",
    "name": "New data importing options",
    ...
  },
  "changes": [
    {
      "model_id": "6e3c193a6d5e51c712d63266",
      "kind": "create",
      "capture_id": [ ... ],
      "object": {
        "id": "6e3c193a6d5e51c712d63266",
        "body": "Welcome!",
        ...
      },
      ...
    },
    {
      "model_id": "6e3c193a6d5e51c712d63266",
      "kind": "update",
      "capture_id": [ ... ],
      "object": {
        "body": ["Welcome!", "Hello and Welcome"],
        ...
      }
      ...
    }
  ],
  ...
}
```


