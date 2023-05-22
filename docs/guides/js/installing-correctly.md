# Installing correctly

In your SaaS product you likely have Users and Accounts (simply a group of Users often from the same real Company)

Chameleon is designed to mirror this in its design of [User Profiles](apis/profiles.md), [Companies](apis/companies.md),
[Segments](apis/segments.md), searchable [HelpBar content](guides/helpbar/user-generated-content.md), etc.

> **First, generate JavaScript Code on the [installation page](https://app.chameleon.io/setup/install)** and adapt based on this guide. 

## The entrypoint JavaScript :id=on-page-script

The sets up the Chameleon object called `chmln` on the page and adds relevant hooks for loading the rest of Chameleon

```javascript
!function(d,w){var t="...
```

## Identifying users :id=identify

On each page load (and full-page refresh) you need to identify the current User + Account to Chameleon.

```javascript
chmln.identify(user.id, { company: { uid: account.id } });
```

We highly recommend using [Identity verification](https://help.chameleon.io/en/articles/4281577) where Chameleon will only accept verified requests.
On your server, you generate a `SHA256` of the User ID and the current timestamp connected with a dash inside and outside the hash (the `chameleon_uid_hash` key shown below is just an example key name).

> The [full list](https://github.com/chamaeleonidae/verification) of Examples in [Node.js](https://github.com/chamaeleonidae/verification/blob/master/verification.js), [Python](https://github.com/chamaeleonidae/verification/blob/master/verification.py), [Ruby](https://github.com/chamaeleonidae/verification/blob/master/verification.rb), etc.

```javascript
const crypto = require('crypto');

const secret = process.env.CHAMELEON_VERIFICATION_SECRET;
const now = Math.floor(Date.now() / 1000);

const uid_hash = [crypto.createHmac('sha256', secret).update(`${uid}-${now}`).digest('hex'), now].join('-');
```

Then pass `uid_hash` in the options to `chmln.identify`

```javascript
chmln.identify(user.id, { uid_hash: user.chameleon_uid_hash, company: { uid: account.id } });
```


## Navigating your Application :id=on-app-navigate

Imagine that you want to send your Users to the billing page. With this script you can setup a Navigate type of HelpBar [SearchItem](apis/search.md?id=schema-search-items) for the Billing page and link to `/settings/billing`.
When this item is clicked you will receive a callback to `app:navigate` with opts set to `{ to: "/settings/billing" }`

##### React :id=on-app-navigate-js

```javascript
chmln.on('app:navigate', (opts) => {
  /* opts.to is the URL to navigate to. This value is set by previous calls to add SearchItems */

  window.history.pushState(null, null, opts.to);
});
```

##### React :id=on-app-navigate-react

```jsx
import { useMemo } from 'react';
import { useHistory } from 'react-router-dom';

const ChmlnHooks = () => {
  let history = useHistory();

  useMemo(() => {
    chmln.on('app:navigate', (opts) => { return history.push(opts.to); });
  }, [history]);
}

  // then in index.js
  <ChmlnHooks />
```