# Localization / Internationalization [BETA]

**The content of Chameleon Experiences can be Localized / Internationalized into a reasonable number of languages**

> Localization is in BETA at the moment ([Contact us](https://app.chameleon.io/help) to join) and available as an add-on to our Grown / Enterprise plans.
>
> The main [Help page](https://help.chameleon.io/en/articles/5868890) on this topic may be more helpful for a typical workflow.

1. [Download](apis/translation.md?id=i18ns-show) or from the [various lists of Experiences](https://app.chameleon.io).
2. Translate
3. [Upload](apis/translation.md?id=i18ns-create) or from the [Localization page](https://app.chameleon.io/settings/translations).
4. Set Experiences live

----

## Downloading Translation files :id=i18ns-show

#### HTTP Request

```
# Translation file for a single experience [A]
GET|POST https://api.chameleon.io/v3/edit/:kind/:id/i18n(.:format)

# Translation file for all experiences of a specific kind
GET|POST https://api.chameleon.io/v3/edit/:kind/i18n(.:format)

# Translation file for a mixture of many different experience types [B]
GET|POST https://api.chameleon.io/v3/edit/experiences/i18n(.:format)
```


| param                |                     | -        | description                                                                                                             |
|----------------------|---------------------|----------|-------------------------------------------------------------------------------------------------------------------------|
| `kind`               | string              | optional | One of `tour`, `survey`, `lanuncher`, `tooltip`                                                                         |
| `id`                 | ID                  | optional | The ID of a Chameleon Experience                                                                                        |
| `format`             | string              | required | One of `yaml`, `json`                                                                                                   |
| `experiences`        | array&lt;Object&gt; | optional | Each member of this array has two keys `kind` and `id` [examples](apis/translations.md?id=example-download-experiences) |
| `experiences.$.kind` | string              | optional | One of `tour`, `survey`, `lanuncher`, `tooltip`                                                                                                              |
| `experiences.$.id`   | string              | optional | The ID of a Chameleon Experience                                                                                                                       |



#### HTTP Response

###### Downloading into `.yaml` :id=example-download-model-yaml

```
# Example [A]
GET https://api.chameleon.io/v3/edit/tours/6f3c4232c712de665632a5f1/i18n.yaml
```

```yaml
id: "6f3c4232c712de665632a419"

language:
  code: "default"
  options: ["default", "es", "fr"]

experiences:
  -
    id: "6f3c4232c712de665632a5f1"
    name: "01 Onboarding 🚧"
    steps:
      -
        id: "6f3c4232c712de665632a5f2"
        translations:
          title:
            text: "Hello and Welcome!"
          body:
            text: "The best place to get started is right here, Import your first 100 data points"
          dismiss_text:
            text: "not now"
          buttons:6f3c4232c5632a5f3712de66:text:
            text: "Show me"
      -
        id: "6f3c4232c712de665632a5f3"
        translations:
          body:
            text: "Drag and drop your data here"
```

###### Downloading into `.json` :id=example-download-json

```
# Example [A]
GET https://api.chameleon.io/v3/edit/tours/6f3c4232c712de665632a5f1/i18n.json
```

```json
{
  "id": "6f3c4232c712de665632a419",
  "language": {
    "code": "default",
    "options": ["default", "es", "fr"]
  },
  "experiences": [
    {
      "id": "6f3c4232c712de665632a5f1",
      "name": "01 Onboarding 🚧",
      "steps": [
        {
          "id": "6f3c4232c712de665632a5f2",
          "translations": {
            "title": {
              "text": "Hello and Welcome!"
            },
            "body": {
              "text": "The best place to get started is right here, Import your first 100 data points"
            },
            "dismiss_text": {
              "text": "not now"
            }
          }
        },
        {
          "id": "6f3c4232c712de665632a5f2",
          "translations": {
            "body": {
              "text": "Drag and drop your data here"
            }
          }
        }
      ]
    }
  ]
}
```

##### Example with mixed Experiences :id=example-download-experiences

```
# Example [B]
POST https://api.chameleon.io/v3/edit/experiences/i18n.yaml
```

###### Request body

```json
{
  "experiences": [
    { "kind": "tour", "id": "6f3c4232c712de665632a5ef" },
    { "kind": "survey", "id": "6312dfe6c4232c765632a5f0" },
    { "kind": "tour", "id": "62c7f3c42312de665632a5f1" },
    { "kind": "launcher", "id": "6de665632f3c4232c712a5f2" },
    { "kind": "tooltip", "id": "6f3c4232c712de665632a5f3" }
  ]
}
```


## Uploading Translation files :id=i18ns-create

#### HTTP Request

```
POST https://api.chameleon.io/v3/edit/i18n
```


| param                |                   | -        | description                                |
|----------------------|-------------------|----------|--------------------------------------------|
| `file`               | File              | optional | A single file to process for translations  |
| `files`              | array&lt;File&gt; | optional | Multiple files to process for translations |


**Single file**:

```text
curl -X POST -H "X-Account-Secret: CHAMELEON_SECRET" https://api.chameleon.io/v3/edit/i18n \
  -F file=@renamed-translation-file-in-ES.yaml

curl -X POST -H "X-Account-Secret: CHAMELEON_SECRET" https://api.chameleon.io/v3/edit/i18n \
  -F file=@renamed-translation-file-in-FR.yaml
```

**Multiple files**:

```text
curl -X POST -H "X-Account-Secret: CHAMELEON_SECRET" https://api.chameleon.io/v3/edit/i18n \
  -F 'files[]='@renamed-translation-file-in-ES.yaml -F 'files[]='@renamed-translation-file-in-FR.yaml
```




