# Overview


The Javascript API is the client-side portion of Chameleon's API. With it, you can access and manipulate a wide variety of data that exists on the client.

> If you use `package.json` within your client application, please use our package [@chamaeleonidae/chmln](https://www.npmjs.com/package/@chamaeleonidae/chmln).

---


## Ideas for how you can use the JavaScript API

- Send data about whether a user has completed a specific Tour to your marketing automation tool, so you can send emails accordingly.
- Update user records in Chameleon when users take key actions in your product, in order to target them with relevant Tours.
- Update user records in Chameleon with data from other data sources that we don't yet integrate with, such as a Customer Support tool or NPS provider.
- Start a Tour when a user completes uploading some key data to their account, to congratulate them and show them the next steps.
- Change the branding of Chameleon Tours based on the brand settings for any particular customer account.


#### Examples

Identify the current user when you know who it is. Assuming you have expose the `currentUser` on the `window`.

```javascript
chmln.identify(window.currentUser.id, {
  email: window.currentUser.email,
  // other custom data
});
```

Identify the current user after loading asynchronously from your backend.

```javascript
import { loadUser } from '../../lib/actions/users';

loadUser().then(user => {
  chmln.identify(user.id, {
    email: user.email,
    // other custom data
  });
})
```

Allow Chameleon to "navigate" your **Single Page Application (SPA)** with `pushState`

```javascript
chmln.on('app:navigate', (opts) => { return history.pushState(null, null, opts.to); });
```


Allow Chameleon to "navigate" your **React** router based SPA

```javascript
// lib/Chmln/Hooks.jsx

import { useMemo } from 'react';
import { useHistory } from 'react-router-dom';

export const ChmlnHooks = () => {
  let history = useHistory();

  useMemo(() => {
    window.chmln && window.chmln.on('app:navigate', (opts) => { return history.push(opts.to); });
  }, [history]);

  return null;
};

// Then in your App.js (or where you define routes etc.)
import { ChmlnHooks } from './lib/Chmln/Hooks';

  // ...

  <ChmlnHooks />

```

Track an Event to Chameleon when a user Imports data

```javascript
chmln.track('Imported data');
```


Listen for Chameleon sourced events (Tour Started, Microsurvey finished, etc)

```javascript
chmln.on('chmln:event', (name, options) => {
  window.yourCustomIntegration.track(name, options);
});


```


