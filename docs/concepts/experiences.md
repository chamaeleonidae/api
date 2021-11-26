# Experiences

Chameleon **_Experience_** is the generic name for any of [Tour](apis/tours.md), [Microsurvey](apis/surveys.md), [Launcher](apis/launchers.md), or [Tooltip](apis/tooltips.md).

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