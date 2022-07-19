# Experiences

Chameleon **_Experience_** is the generic name for any of [Tour](apis/tours.md), [Microsurvey](apis/surveys.md), [Launcher](apis/launchers.md), or [Tooltip](apis/tooltips.md).


## Lists of Experiences :id=list
> When a list of experiences is returned each object will contain a `kind` key (see example below).


```json
{
  "experiences": [
    {
      "id": "5f3c4232c712de665632a2a3",
      "kind": "tour",
      ...
    },
    {
      "id": "5e3c4232c712de665632a2a4",
      "kind": "survey",
      ...
    },
    {
      "id": "5d3c4232c712de665632a2a5",
      "kind": "tooltip",
      ...
    },
    {
      "id": "5c3c4232c712de665632a2a6",
      "kind": "launcher",
      ...
    },
  ]
}
```


## Tags and Environments :id=tags-and-url-groups

When [Tags](apis/tags.md) or [Environments](apis/urls.md) are added to an experience, it will look like this:

```json
{
  "experiences": [
    {
      "id": "5f3c4232c712de665632a2a3",
      "kind": "tour",
      "name": "New Data Imports are here",
      "tags": [
        {
          "id": "6f3c4232de66c7225632a2a4",
          "uid": "announcement",
          "name": "Feature announcement",
          ...
        },
        {
          "id": "6e3c4232de66c7225632a2a5",
          "uid": "2029 Q1 releases",
          "name": "Features in 2029 Q1",
          ...
        },
        ...
      ],
      "url_groups": [
        {
          "id": "6f885a88e7daf3000e3e4b8f",
          "name": "Production",
          "short_name": "PR",
          "urls": {
            "dashboard": "https://app.chameleon.io/domains/6f885a88e7daf3000e3e4b8f"
          }
        },
        {
          "id": "6f885aaf3088e7d00e3e4b9e",
          "name": "EU Production",
          "short_name": "EU",
          "urls": {
            "dashboard": "https://app.chameleon.io/domains/6f885a88e7daf3000e3e4b9e"
          }
        },
        ...
      ],
      ...
    },
    ...
  ]
}
```
