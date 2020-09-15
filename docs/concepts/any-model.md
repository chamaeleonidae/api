# Listing Models

The Chameleon API allows a generic retrieval and listing of data models. 

------



The currently supported models are:

| Model + details                                              | List URL                 | Show URL                     |
| ------------------------------------------------------------ | ------------------------ | ---------------------------- |
| [Segments](https://github.com/chamaeleonidae/api/blob/master/docs/concepts/apis/segments.md) | `GET /v3/edit/segments`  | `GET /v3/edit/segments/:id`  |
| [Tours](https://github.com/chamaeleonidae/api/blob/master/docs/concepts/apis/tours.md) | `GET /v3/edit/tours`     | `GET /v3/edit/tours/:id`     |
| [Microsurveys](https://github.com/chamaeleonidae/api/blob/master/docs/concepts/apis/surveys.md) | `GET /v3/edit/surveys`   | `GET /v3/edit/surveys/:id`   |
| [Launchers](https://github.com/chamaeleonidae/api/blob/master/docs/concepts/apis/launchers.md) | `GET /v3/edit/launchers` | `GET /v3/edit/launchers/:id` |
| [Tooltips](https://github.com/chamaeleonidae/api/blob/master/docs/concepts/apis/tooltips.md) | `GET /v3/edit/tooltips`  | `GET /v3/edit/tooltips/:id`  |
| [Domains](https://github.com/chamaeleonidae/api/blob/master/docs/concepts/apis/urls.md) | `GET /v3/edit/urls`      | `GET /v3/edit/urls/:id`      |



#### HTTP Responses

All the HTTP responses look the same, with a pluralized top-level key with the list of models.

```
{
 "segments": [
   {
     "id": "5f3c4232c712de665632a2a1",
     ...
   }
 ]
}
{
  "launchers": [
    {
      "id": "5f3c4232c712de665632a2a3",
      ...
    }
  ]
}
```



When retrieving a single item, its designation will be singular (`launchers` becomes `launcher`).

```
{
  "launcher": {
    "id": "5f3c4232c712de665632a2a3",
    ...
  }
}
```



> **Are we missing a model you need and care about?** [Contact us](mailto:hello@trychameleon.com?subject=Listing+any+Model) to request a different one.

