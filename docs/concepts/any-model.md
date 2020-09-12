# Listing any Model

The Chameleon API allows generic listing and showing of models. Currently supported models are:

| Model + details | List URL | Show URL |
| --- | --- | --- |
| [Segments](apis/segments.md) | `GET /v3/edit/segments` | `GET /v3/edit/segments/:id` |
| [Tours](apis/tours.md) | `GET /v3/edit/tours` | `GET /v3/edit/tours/:id` |
| [Microsurveys](apis/surveys.md) | `GET /v3/edit/surveys` | `GET /v3/edit/surveys/:id` |
| [Launchers](apis/launchers.md) | `GET /v3/edit/launchers` | `GET /v3/edit/launchers/:id` |
| [Tooltips](apis/tooltips.md) | `GET /v3/edit/tooltips` | `GET /v3/edit/tooltips/:id` |
| [Domains](apis/urls.md) | `GET /v3/edit/urls` | `GET /v3/edit/urls/:id` |

#### HTTP Responses

All responses look the same with a pluralized top-level key with the list of models.

 ```json
{
  "segments": [
    {
      "id": "5f3c4232c712de665632a2a1",
      ...
    }
  ]
}
```

```json
{
  "launchers": [
    {
      "id": "5f3c4232c712de665632a2a3",
      ...
    }
  ]
}
```

#### When Retrieving a single item, it will be singular!

```json
{
  "launcher": {
    "id": "5f3c4232c712de665632a2a3",
    ...
  }
}
```

Missing ones you care about? [Contact us](mailto:hello@trychameleon.com?subject=Listing+any+Model) to request a different one.
