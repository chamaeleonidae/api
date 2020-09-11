# Update Domains via REST API

**Automate which domains Chameleon is enabled for**



> **Note:** The domain preauthorize API is **available by request**. Please [email us](mailto:help@trychameleon.com?subject=enable domains api) to enable for your account.



*For an overview of how the Chameleon API works, please first read* [*this article*](https://help.trychameleon.com/developer-docs/api-basics)*.*

------



Enabling Domains on your Chameleon account via API can be helpful for: 

- Enabling new domains on a top-level-domain.
- Enabling Chameleon on a white-label application.



## Enabling a domain via REST API

#### **Create a domain on your account**

Send a `POST`  to `https://app.trychameleon.com/urls/preauthorize` .

Include a `host` value for the domain being added or updated (required).

> *Note: domains (e.g. google.com) must be submitted to Chameleon prior to subdomains (e.g. mail.google.com).*

Include an `enable` and set to `on` or `off` to enable or disable the domain (optional).

> *Note: by default, enable is set to `on`.* 

**Example: Enabling a domain unseen by Chameleon**

Request:

```
curl -X POST https://app.trychameleon.com/urls/preauthorize -H "X-Account-Secret: SECRET" -d '{"host":"myenableddomain.com"}' -H 'Content-Type: application/json'
```

Response:

```
{
    "url":{
        "id":"5c4950c34733cc0004d5bfd7",
        "created_at":"2019-01-24T05:44:35.000Z",
        "updated_at":"2019-01-24T21:47:33.472Z",
        "enabled":"subdomain",
        "host":"myenableddomain.com",
        "domain":"myenableddomain.com",
        "installed_at":null,
        "first_seen_at":null,
        "last_seen_at":null
    }
}
```



#### Update a domain on your account

Send a `POST`  to  `https://app.trychameleon.com/urls/preauthorize`.
Include the same information as when enabling an unseen domain. 
Include an `enable` and set to `"on"` or `"off"` to enable or disable the domain (optional).

> *Note: by default, enable is set to `on`.* 



**Example: Disabling a subdomain seen by Chameleon**

Request:

```
curl -X POST https://app.trychameleon.com/urls/preauthorize -H "X-Account-Secret: SECRET" -d '{"host":"subdomain.myenableddomain.com","enabled":"off"}' -H 'Content-Type: application/json'
```

Response:

```
{
    "url":{
        "id":"5c4950c34733cc0004d5bfd7",
        "created_at":"2019-01-24T05:44:35.000Z",
        "updated_at":"2019-01-24T21:47:33.472Z",
        "enabled":"off",
        "host":"subdomain.myenableddomain.com",
        "domain":"subdomain.myenableddomain.com",
        "installed_at":null,
        "first_seen_at":null,
        "last_seen_at":null
    }
}
```

