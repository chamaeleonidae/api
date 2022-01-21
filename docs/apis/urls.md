# Domains and Environments

**A Url is a record of authorization and permission. Without a Url record enabled for a particular domain:**

- **The Live Experiences will not display and the Chameleon JavaScript will not be loaded onto the page.**
- **HTTP requests to our Internal APIs (to edit any Experiences or content) will fail.**


*If you want to know more about managing domains and subdomains in Chameleon, please visit our [product documentation](https://help.trychameleon.com/en/articles/1318033-managing-domains-and-subdomains).*


**[Jump to Environments](apis/urls.md?id=url-groups)**

------

## Domains (Urls)


Enabling Domains on your Chameleon account via API can be helpful for:

- Enabling new domains on a top-level-domain.
- Enabling Chameleon on a white-label application.



With the Chameleon API for Domains, you can:

- Enable new domains [jump ↓](apis/urls.md?id=urls-create).
- Assign domains to different Environments [jump ↓](apis/urls.md?id=url-groups-create) (production,staging,test,etc.).
- Enable or disable an existing domain.
- Retrieve all domains that correspond to the specified parameters (search by tld).
- Retrieve a specific domain based on its `id`.


## Domain Schema (Url) :id=schema

| Property        | Type      | Description                                                                                                                                     |
|-----------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`            | ID        | The Chameleon ID                                                                                                                                |
| `created_at`    | timestamp | When this happened or when this was added to the Database                                                                                       |
| `updated_at`    | timestamp | The last time any property was updated                                                                                                          |
| `url_group_id`  | ID        | The Environment ([Url Group](apis/urls.md?id=url-groups)) this Url is a part of. `null` to be part of all Environments.                         |
| `host`          | string    | The fully qualified domain of this Url (i.e. app.example.com)                                                                                   |
| `domain`        | string    | The top-level domain (i.e. example.com)                                                                                                         |
| `enabled`       | string    | The authorization state of this Url. `subdomain` means that new urls are `on` vs safely defaulting to `off`: One of `off`, `on`, or `subdomain` |
| `installed_at`  | timestamp | When the JavaScript snippet was installed on this domain                                                                                        |
| `first_seen_at` | timestamp | When this domain had its first User Profile identified                                                                                          |
| `last_seen_at`  | timestamp | The most recent time a User Profile as identified                                                                                               |
| `unlisted`      | boolean   | [deprecated; replaced by `archived_at`] If this Url is hidden from the list of domains                                                          |
| `archived_at`   | timestamp | The time when this was archived                                                                                                                 |                                                                                                                                          |


## Create a Url (enable a new domain) :id=urls-create

#### HTTP Request

```
POST https://api.trychameleon.com/v3/edit/urls
```

| param         | -        | description                                                  |
|---------------| -------- | ------------------------------------------------------------ |
| `host`        | required | The fully qualified domain of this Url (i.e. app.example.com) |
| `enabled`     | optional | The authorization state to create with. Default is `on`. Values are one of `on`, `off`, or `subdomain` |
| `unlisted`    | optional | [deprecated; replaced by `archived_at`] Whether or not the Url is displayed on the [Domains page](https://app.trychameleon.com/settings/domains) in the dashboard |
| `archived_at` | optional | To archive set to a timestamp, to unarchive set to `null`                                          |

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



## Update a Url :id=urls-update

#### HTTP Request

```
PUT|PATCH https://api.trychameleon.com/v3/edit/urls/:id
```

| param          | -        | description                                                                                                                                                       |
|----------------| -------- |-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`           | required | The Chameleon ID of the Url to update                                                                                                                             |
| `enabled`      | optional | The authorization state to create with. Default is `on`. Values are one of `on`, `off`, or `subdomain`                                                            |
| `unlisted`     | optional | [deprecated; replaced by `archived_at`] Whether or not the Url is displayed on the [Domains page](https://app.trychameleon.com/settings/domains) in the dashboard |
| `archived_at`  | optional | To archive set to a timestamp, to unarchive set to `null`                                                                                                         |
| `url_group_id` | optional | The Environment ([Url Group](apis/urls.md?id=url-groups)) to assign this Url to                                                                                                                 |

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



## Bulk a Url :id=urls-bulk-update

#### HTTP Request

```
POST https://api.trychameleon.com/v3/edit/urls/batch
```

| param          | -        | description                                                                       |
|----------------| -------- |-----------------------------------------------------------------------------------|
| `ids`          | required | An array of Chameleon IDs of the Urls to update                                   |
| `enabled`      | optional | The authorization state to change to.                                             |
| `archived_at`  | optional | To archive set to a timestamp, to unarchive set to `null`                         |
| `url_group_id` | optional | The Environment ([Url Group](apis/urls.md?id=url-groups)) to assign these Urls to |

#### HTTP Response

All of the Urls given in the request `ids` are updated with the value given by `enabled`, `archived_at`, or `url_group_id`. They are sent back even if they were already in the resulting bulk-update state.

```json
{
  "urls": [
    {
      "id": "5c4950c34733cc0004d5bfd7",
      "host": "test2.example.com",
      "domain": "example.com",
      "enabled": "on",
      ...
    },
    {
      "id": "5c4950c34733cc0004d5bfd8",
      "host": "test4.example.com",
      "domain": "example.com",
      "enabled": "on",
      ...
    }
  ]
}
```



## Listing all Urls :id=urls-index

#### HTTP Request

```
GET https://api.trychameleon.com/v3/edit/urls
```

| param  | -        | description                                                  |
| ------ | -------- | ------------------------------------------------------------ |
| `domain` | optional | Filter to urls only on this domain (i.e. ex.io will return app.ex.io, dashboard.ex.io but not app.example.com) |
| `limit`  | optional | Defaults to `50` with a maximum of `500`                     |
| `before` | optional | Used when paginating, use directly from the `cursor` object from the previous response |
| `before` | optional | Read as "created `before`" and can be given as a timestamp to get only `limit` items that were created before this time |
| `after`  | optional | Read as "created `after`" and can be given as a timestamp or ID to get only `limit` items that were created after this time |

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



## Retrieve a Url :id=urls-show

#### HTTP Request

```
GET https://api.trychameleon.com/v3/edit/urls/:id
```

| param | -        | description                           |
| ----- | -------- | ------------------------------------- |
| `id`    | required | The Chameleon ID of the Url to show |

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

---------------

## Environments (Url Groups) :id=url-groups

> Environments are in BETA at the moment ([Contact us](https://app.trychameleon.com/help) to join).

An Environment is a group of Domains. The purpose of an Environment is to:

1. Split data out into groups; the groups are used in the Chameleon Dashboard to display your Experience data by environment.
2. Allow Chameleon Admins a simple way to publish Experiences first to Staging/QA then to Production without needing to change the [Url Rules](https://help.trychameleon.com/en/articles/1183932). 
3. Have greater visibility into what your end-users will be eligible for.


> All Urls and all Experiences are part of the Default Environment by default
> Assigning a `url_group_id` to a TLD means that all future subdomains of that TLD are 


## Environment Schema (Url Group) :id=url-groups-schema

| Property                 | Type      | Description                                                                      |
|--------------------------|-----------|----------------------------------------------------------------------------------|
| `id`                     | ID        | The Chameleon ID                                                                 |
| `created_at`             | timestamp | When this happened or when this was added to the Database                        |
| `updated_at`             | timestamp | The last time any property was updated                                           |
| `archived_at`            | timestamp | The time when this was archived                                                  |                                                                                                                                          |
| `name`                   | string    | The name given by an administrator of Chameleon                                  |
| `description`            | string    | The display description                                                          |
| `short_name`             | string    | Up to 3 characters abbreviating the name (i.e. PR for Production)                |
| `style_short_name_color` | string    | A easily recognizable color; an uppercase 6 char hex code excluding the `#`.     |


## Create a Url Group :id=url-groups-create

#### HTTP Request

```
POST https://api.trychameleon.com/v3/edit/url_groups
```

| param                  | -        | description                                                                                     |
|------------------------| -------- |-------------------------------------------------------------------------------------------------|
| `name`                   | required | The name of this Environment                                                                    |
| `description`            | optional | A description to display along with the Environment `name`                                      |
| `short_name`             | optional | 1-3 character 'short code' that should be the short version of the name (PR for Production etc.) |
| `style_short_name_color` | optional | A 6 character hex code color to identify the Environment                                    |

#### HTTP Response

```json
{
  "url_group": {
     "id": "6c4950c34733cc0004d5bff1",
     "name": "Test QA #1",
     "description": "Pre-production for our QA team",
     "short_name": "Q1",
     "style_short_name_color": "E7AD5A",
     ...
  }
}
```


## Update a Url Group :id=url-groups-update

#### HTTP Request

```
PUT|PATCH https://api.trychameleon.com/v3/edit/url_groups/:id
```


| param                    | -        | description                                                                                     |
|--------------------------|----------|-------------------------------------------------------------------------------------------------|
| `id`                     | required | The Url Group ID.                                                                   |
| `name`                   | optional | The name of this Environment                                                                    |
| `description`            | optional | A description to display along with the Environment `name`                                      |
| `short_name`             | optional | 1-3 character 'short code' that should be the short version of the name (PR for Production etc.) |
| `style_short_name_color` | optional | A 6 character hex code color to identify the Environment                                   |
| `archived_at`            | optional | To archive set to a timestamp, to unarchive set to `null`                                       |


#### HTTP Response

```json
{
  "url_group": {
    "name": "QA #1",
    ...
  }
}
```

## Add Domains to an Environment

[Updating a Url](apis/urls.md?id=urls-update) with a `url_group_id` of an Environment ([Url Group](apis/urls.md?id=url-groups)) will assign it to that Environment


## Removing Domains from an Environment

[Updating a Url](apis/urls.md?id=urls-update) with a `url_group_id` equal to `null` will assign it to the Default Environment



## Listing all Url Groups :id=url-groups-index

#### HTTP Request

```
GET https://api.trychameleon.com/v3/edit/url_groups
```

| param  | -        | description                                                                                                                 |
| ------ | -------- |-----------------------------------------------------------------------------------------------------------------------------|
| `limit`  | optional | Defaults to `50` with a maximum of `500`                                                                                    |
| `before` | optional | Used when paginating, use directly from the `cursor` object from the previous response                                      |
| `before` | optional | Read as "created `before`" and can be given as a timestamp to get only `limit` items that were created before this time     |
| `after`  | optional | Read as "created `after`" and can be given as a timestamp or ID to get only `limit` items that were created after this time |

#### HTTP Response

```json
{
  "urls": [
    {
      "id": "6c4950c34733cc0004d5bff1",
      "name": "Test QA #1",
      "description": "Pre-production for our QA team",
      "short_name": "Q1",
      "style_short_name_color": "E7AD5A",
      ...
    },
    {
      "id": "6c4950c34733cc0004d5bff2",
      "name": "Staging",
      "description": null,
      "short_name": "ST",
      "style_short_name_color": "6D95C0",
      ...
    },
     {
       "id": "6c4950c34733cc0004d5bff2",
       "name": "Production",
       "description": "Live for customers",
       "short_name": "PR",
       "style_short_name_color": "8FC06D",
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



## Retrieve a Url Group :id=url-groups-show

#### HTTP Request

```
GET https://api.trychameleon.com/v3/edit/url_groups/:id
```

| param  | -        | description                                                                            |
|--------| -------- |----------------------------------------------------------------------------------------|
| `id`   | required | The Chameleon ID of the Environment ([Url Group](apis/urls.md?id=url-groups)) to show  |

#### HTTP Response

```json
{
  "url": {
    "id": "6c4950c34733cc0004d5bff2",
    "name": "Staging",
    "description": null,
    "short_name": "ST",
    "style_short_name_color": "6D95C0",
    ...
  }
}
```
