# Search your User-generated content

In this guide we will talk about how to make your User-generated content ([SearchItem](apis/search.md?id=schema-search-items)s) searchable with the HelpBar. This guide makes some assumptions
about how you install Chameleon, than you pass the User ID + Account ID to like this: `chmln.identify(user.id, { company: { uid: account.id } })` and that you have installed with `chmln.on("app:navigate", opts => { ... })`

Your Saas Product likely has the concept of Users, Accounts and a variety of things (content) that Users can create. Each item
has a set of Users (i.e. members of an Account) that have access to the content they create.

Here is some sample data that we will work off. Imagine that your SaaS product is called **Dashy** (`app.dashy.run`) where Users create metric-based Dashboards.
When a User has access to a Dashboard they will see it in their list of Dashboards on `https://app.dashy.run/dashboards`

- By default, Dashboard are only available/visible to the creator of the Dashboard.
- A Dashboard can be published/shared to all Users of the Account
- A Dashboard can be published/shared specific Users

## Sample Data in the Dashy database :id=example-data

###### Users
| ID     | Account ID | Name      | [Notes]                         |
|--------|------------|-----------|---------------------------------|
| `134`  | `d3fa1`    | **Jane**  | On the same Account as **John** |
| `137`  | `f2d3a`    | **John**  | On the same Account as **Jane** |
| `139`  | `f2d3a`    | **Alice** | Only User on this Account       |

###### Accounts
| ID      | Name      | [Notes]                            |
|---------|-----------|------------------------------------|
| `d3fa1` | **Jexar** | 2 Users are: **Jane** and **John** |
| `f2d3a` | **Apex**  | 1 User is: **Alice**               |

###### Dashboards
| ID    | Account ID | User ID | User name | Title                       | [Notes] |
|-------|------------|---------|-----------|-----------------------------|---------|
| `413` | `d3fa1`    | `134`   | **Jane**  | Q3 Northstar metrics        |         |
| `435` | `d3fa1`    | `134`   | **Jane**  | Product usage - Power users |         |
| `476` | `d3fa1`    | `137`   | **John**  | Website/Ads metrics 2029-03 |         |
| `498` | `f2d3a`    | `139`   | **Alice** | FY29 Financial reports      |         |


## Lifecycle of content (CRUD) :id=lifecycle-crud

- Create: Add content to HelpBar [example ↓](guides/helpbar/user-generated-content.md?id=examples-crud-create-basic)
- Read: skip because the content doesn't change
- Update: Conditionally update with important changes [example ↓](guides/helpbar/user-generated-content.md?id=examples-crud-update-basic)
- Delete: Remove content from HelpBar [example ↓](guides/helpbar/user-generated-content.md?id=examples-crud-delete-basic)


### Create: Add this content to HelpBar :id=examples-crud-create-basic

1. **Jane** creates a Dashboard called **Q3 Northstar metrics** it's visible only to **Jane**.
2. **John** creates a Dashboard called **Website/Ads metrics 2029-03** it's visible only to **John** AND **Jane** but not to new Users who join **Jexar** (since it's visible explicitly to Users `134` and `137`).
3. **Alice** creates a Dashboard called **FY29 Financial reports** it's visible to all Users who join **Apex** (since it's visible to Account `f2d3a`).

- Pull the `SEARCH_GROUP_ID` from the URL for the Chameleon [SearchGroup](apis/search.md?id=schema-search-groups) that you want to add this content to (e.g. `https://app.chameleon.io/helpbar/edit/content/654001081b27ac5e6ae5a08e`)
- Send a `uid` that will be stable for the life of this content. `dashboard-413` in this example; you use this to update / delete.
- In this example we use `profile_uids` as an array of 1 item, **Jane**, because only 1 User should have access to search for this.
- Use 1 [SearchActions](apis/search.md?id=schema-search-actions) in `actions` with `kind=navigate`. When clicked in the HelpBar
  the page will receive a callback into `chmln.on("app:navigate", (opts) => { /* opts.to will be "/dashboards/413" */ })`.

```bash
# 1.
curl -X POST -H 'X-Account-Secret: ACCOUNT_SECRET' -H 'Content-Type: application/json' \
  -d '{"search_group_id": SEARCH_GROUP_ID, "uid": "dashboards-413", "title": "Q3 Northstar metrics", "profile_uids": ["134"], actions: [{ "kind": "navigate", "url": "/dashboards/413" }] }' \
  'https://api.chameleon.io/v3/edit/search_items'

# 2.
curl -X POST -H 'X-Account-Secret: ACCOUNT_SECRET' -H 'Content-Type: application/json' \
  -d '{"search_group_id": SEARCH_GROUP_ID, "uid": "dashboards-476", "title": "Website/Ads metrics 2029-03", "profile_uids": ["134", "137"], actions: [{ "kind": "navigate", "url": "/dashboards/476" }] }' \
  'https://api.chameleon.io/v3/edit/search_items'

# 3.
curl -X POST -H 'X-Account-Secret: ACCOUNT_SECRET' -H 'Content-Type: application/json' \
  -d '{"search_group_id": SEARCH_GROUP_ID, "uid": "dashboards-498", "title": "FY29 Financial reports", "company_uids": ["f2d3a"], actions: [{ "kind": "navigate", "url": "/dashboards/498" }] }' \
  'https://api.chameleon.io/v3/edit/search_items'
```

When **Jane**  hits `CMD+k` in your product and searches via HelpBar for "metrics" it will display 2 results, "Q3 Northstar metrics" and "Website/Ads metrics 2029-03".
When **John**  hits `CMD+k` in your product and searches via HelpBar for "metrics" it will display 1 result, "Website/Ads metrics 2029-03".
When **Alice** hits `CMD+k` in your product and searches via HelpBar for "metrics" it will display 1 result, "Website/Ads metrics 2029-03".

### Update: Conditionally update with important changes :id=examples-crud-update-basic

When **Jane** updates the title and adds a note about how to use this Dashboard. Note: this content will retain its other state such as actions, visibility etc.

```bash
curl -X PATCH -H 'X-Account-Secret: ACCOUNT_SECRET' -H 'Content-Type: application/json' \
  -d '{"uid": "dashboards-413", "title": "Q3 Northstar metrics - final", "description": "See how we are tracking for Q3 and help hit goals" }' \
  'https://api.chameleon.io/v3/edit/search_items'
```

When **Jane** has finalized the metrics and makes this visible to the full **Jexar** Account. Setting `company_uids` will allow
any User on the given Account access to search for this content

```bash
curl -X PATCH -H 'X-Account-Secret: ACCOUNT_SECRET' -H 'Content-Type: application/json' \
  -d '{"uid": "dashboards-413", "company_uids": ["d3fa1"] }' \
  'https://api.chameleon.io/v3/edit/search_items'
```

Now if **Jane** OR **John** hit `CMD+k` in your product and search via HelpBar for "metrics" they will both have one result, "Q3 Northstar metrics - final". 

### Delete: Remove content from HelpBar :id=examples-crud-delete-basic

Now that Q3 was a smashing success, **Jane** deletes the Q3 Dashboard

```bash
curl -X DELETE -H 'X-Account-Secret: ACCOUNT_SECRET' -H 'Content-Type: application/json' \
  -d '{"uid": "dashboards-413"}' \
  'https://api.chameleon.io/v3/edit/search_items'
```

