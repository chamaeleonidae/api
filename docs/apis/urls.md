# Domains

## Schema :id=schema

| Property | Type | Description |
| --- | --- | --- |
| `id` | ID | The Chameleon ID |
| `created_at` | timestamp | When this happened or when this was added to the Database |
| `updated_at` | timestamp | The last time any property was updated |
| `host` | string | The fully qualified domain of this URL (i.e. app.example.com) |
| `domain` | string | The top-level domain (i.e. example.com) |
| `enabled` | string | The authorization state of this Url, `subdomain` means that new urls are `on` vs safely defaulting to `off`: One of `off`, `on`, or `subdomain` |
| `installed_at` | timestamp | When the JavaScript snippet was installed on this domain |
| `first_seen_at` | timestamp | When this domain had its first User Profile identified |
| `last_seen_at` | timestamp | The most recent time a User Profile as identified |
| `unlisted` | boolean | If this Url is hidden from the list of domains |

A Url is a record of authorization and permission ([read more here](https://help.trychameleon.com/en/articles/1318033-managing-domains-and-subdomains)).

Without a Url record authorizing a particular domain:
 - The Live Experiences will not display and the Chameleon JavaScript will not be loaded onto the page.
 - HTTP requests it our Internal APIS (to edit any Experiences or content) will fail.

Enabling Domains on your Chameleon account via API can be helpful for: 

- Enabling new domains on a top-level-domain.
- Enabling Chameleon on a white-label application.

------

## Create a Url (Enable a new domain) :id=urls-create

#### HTTP Request
`POST` to `https://api.trychameleon.com/v3/edit/urls`.

| param | - | description |
|---|---|---|
| host | required | The fully qualified domain of this URL (i.e. app.example.com) |
| enabled | optional | The authorization state to create with. Default is `on`. Values are one of `on`, `off`, or `subdomain` |
| unlisted | optional | Whether or not the Url is displayed on the [Domains page](https://app.trychameleon.com/settings/domains) in the dashboard |


#### HTTP Response

```json
{
  "url": {
     "id": "5c4950c34733cc0004d5bfd7",
     "host": "app.example.com",
     "domain": "example.com",
     "enabled": "on",
     ...
  }
}
```

-------

## Update a Url :id=urls-update

#### HTTP Request
`POST` to `https://api.trychameleon.com/v3/edit/urls/:id`.

| param | - | description |
|---|---|---|
| id | required | The Chameleon ID of the Url to update|
| enabled | optional | The authorization state to create with. Default is `on`. Values are one of `on`, `off`, or `subdomain` |
| unlisted | optional | Whether or not the Url is displayed on the [Domains page](https://app.trychameleon.com/settings/domains) in the dashboard |


#### HTTP Response

```json
{
  "url": {
     "id": "5c4950c34733cc0004d5bfd7",
     "host": "app.example.com",
     "domain": "example.com",
     "enabled": "on",
     ...
  }
}
```

-------

## Listing all Urls :id=urls-index

#### HTTP Request
`GET` to `https://api.trychameleon.com/v3/edit/urls`.

| param | - | description |
|---|---|---|
| domain | optional | Filter to urls only on this domain (i.e. ex.io will return app.ex.io, dashboard.ex.io but not app.example.com) |
| limit | optional | Defaults to `50` with a maximum of `500` |
| before | optional | Used when paginating, use directly from the `cursor` object from the previous response |
| before | optional | Read as "created `before`" and can be given as a timestamp to get only `limit` items that were created before this time |

#### HTTP Response

```json
{
  "urls": [
     {
       "id": "5c4950c34733cc0004d5bfd7",
       "host": "app.example.com",
       "domain": "example.com",
       "enabled": "on",
       ...
    },
     {
       "id": "5c4950c34733cc0004d5bfd4",
       "host": "example.com",
       "domain": "example.com",
       "enabled": "subdomain",
       ...
    },
     {
       "id": "5c4950c34733cc0004d5bfd2",
       "host": "internal.example.com",
       "domain": "example.com",
       "enabled": "off",
       ...
    },
    ...
  ],
  "cursor": {
    "limit": 50,
    "before": "5c4950c34733cc0004d5bfd2"
  }
}
```

-------


## Retrieve a Url :id=urls-show

#### HTTP Request
`GET` to `https://api.trychameleon.com/v3/edit/urls/:id`.

| param | - | description |
|---|---|---|
| id | required | The Chameleon ID of the Url to update|


#### HTTP Response

```json
{
  "url": {
     "id": "5c4950c34733cc0004d5bfd7",
     "host": "app.example.com",
     "domain": "example.com",
     "enabled": "on",
     ...
  }
}
```


