# Product Demos

A Product Demo is recorded by a Chameleon admin and shown to your end-users. It typically demonstrates a new feature, a key value that your
software provides, or just explains a complex workflow with the product itself.
It is typically delivered as an embed on your marketing site, or as part of a Chameleon [Tour](apis/tours.md).

- Product marketing and marketing teams use Demos as the main content of feature-specific landing pages.
- Product managers and product marketing use Demos in-product to drive awareness, upsell, and education.
- Prospects are more likely to buy software they have seen/experienced

> The demo can run in Profile or Anonymous modes as outlined below. If possible, run Product Demos in Profile mode 

## Embedding

> Replace the `:id` below with the Demo ID from the dashboard OR copy the embed code from the Sharing section.

### Examples :id=examples

#### Profile mode (logged-in user or email address) :id=mode-profile

Any and all times that you have information about the logged-in user. All of the information about what properties/data
to send is in the main documentation about [Identifying users](js/profiles.md) but the Tl;DR; is that you should send at least a
`uid` as the ID from your database, the `email`, and `name`.

```html
<iframe class="chmln-demo" src="https://fast.chameleon.io/edit/demos/:id" width="100%" height="100%"></iframe>
```

<details>
<summary>Adding User data</summary>

```javascript
(async () => {
  const user = await fetchCurrentUser(); // Note: use your current user function

  if(!user?.id) {
    return;
  }

  const { id: uid, email, name } = user;

  // Add user data to Product demos
  const demos = [...document.querySelectorAll('.chmln-demo')];
  const profile = JSON.stringify({ uid, email, name });

  demos.forEach(demoEl => demoEl.setAttribute('data-profile', profile));

  //
  // Example things one might do with logged-in user info
  //  - Change "Log in" buttons to "Dashboard"
  //  - Fill email fields with user.email
  //  - Fetch the company info and show content relevant to their industry
  //  - Personalize the pricing page with "current plan" info
  //
})();
```
</details>

<details>
<summary>Adding Email</summary>

```javascript
(async () => {
  const email = localStorage.getItem('user-input:email'); // Note: this assumes that you store email when its added to a "login" or "subscribe to updates" form

  if(!email) {
    return;
  }

  // Add email data to Product demos
  const demos = [...document.querySelectorAll('.chmln-demo')];
  const profile = JSON.stringify({ email });

  demos.forEach(demoEl => demoEl.setAttribute('data-profile', profile));

  //
  // Example things one might do with email address
  //  - Fill email fields with email
  //  - Fetch the company info and show content relevant to their industry
  //
})();
```
</details>


#### Anonymous mode (the default) :id=mode-anonymous

When `data-profile` is missing the Demo runs in **anonymous mode**.

```html
<iframe class="chmln-demo" src="https://fast.chameleon.io/edit/demos/:id" width="100%" height="100%"></iframe>
```


### Consent to track (cookies etc.) :id=cookie-consent

Start with consent mode of "consent not yet given" and use either `pending` or `denied`, then update when the user gives or denies
consent by setting the `data-consent` value on the Demos.

> Typically Product Demos fall into the **Functional** category.

```html
<iframe class="chmln-demo" src="https://fast.chameleon.io/edit/demos/:id" width="100%" height="100%"></iframe>
```

Once the consent screen is dismissed

```javascript
const demos = [...document.querySelectorAll('.chmln-demo')];
const functionalAllowed = true; // Note: Use your method to check for this true/false value
const consent = functionalAllowed ? 'granted' : 'denied';

demos.forEach(demoEl => demoEl.setAttribute('data-consent', consent));
```


### Schema of `data-*` properties :id=schema

These control different aspects of the Product Demo including identity, use of cookies, prefilled data, etc.
Sending either the `data-email` or the `data-profile` are **highly recommended** as a method of connecting the dots from
engagement with Product Demos into the other experiences that Chameleon offers such as [Tours](apis/tours.md)),
[Microsurveys](apis/surveys.md), and [HelpBar](apis/search.md).


| Property               | Values                          | Description                                                                                                     |
|------------------------|---------------------------------|-----------------------------------------------------------------------------------------------------------------|
| `data-consent`         | `granted`, `denied` , `pending` | Whether or not consent has been given. Defaults to `granted`. Change this when the user gives or denies consent |
| `data-profile`         | {"uid":"5a17d4", ...}           | A JSON object of data about the current user                                                                    |
| `data-profile`         | {"email":"alice@acme.io"}       | A JSON object with a known email address                                                                        |


## JavaScript API :id=js-api

The iFrame uses `window.postMessage` to communicate information back to the parent page including to the Chameleon
JavaScript [installation](https://help.chameleon.io/en/articles/1161793-installing-directly-using-javascript). Below are listed
the messages you can expect from the iframe at the relevant times in the Demo. Message are described below as being sent but this just
means that any listener to `iframe.addEventListener('message', message => ...)` will be called.

The `message` parameter to the callback function is a [MessageEvent](https://developer.mozilla.org/en-US/docs/Web/API/MessageEvent) where `message.data` is the object sent
from inside the iframe, akin to webhooks (but on the client side).

### Message event kinds :id=schema-kinds


| Event kind                     | Event name             | Description                                                                                          |
|--------------------------------|------------------------|------------------------------------------------------------------------------------------------------|
| `chmln:demo:loaded`            | Demo Loaded            | Once the Demo is ready for interaction                                                               |
| `chmln:demo:started`           | Demo Started           | When the user clicks on the first step                                                               |
| `chmln:demo:completed`         | Demo Completed         | When the last step of the demo is reached. This can happen directly or via branching                 |
| `chmln:demo:step:started`      | Demo Step started      | When a Step is displayed to the user; typically because of clicking on the previous step             |
| `chmln:demo:component:clicked` | Demo Component clicked | When a Hotspot, Tooltip, etc. is clicked                                                             |
| `chmln:demo:button:clicked`    | Demo Button clicked    | When a Button is clicked. Buttons appear in many different places including Tooltips, Chapters, etc. |
| `chmln:demo:form:submitted`    | Demo Form submitted    | When a form is submitted such as adding an email address and clicking "Learn more"                   |


### Examples

The example code using `analytics.track` should be adapted for if/how you track analytics. This can also be completely omitted from your
implementation and Demos will run just fine. _Consider this optional_.


#### Generic analytics tracking :id=example1

```javascript
iframe.addEventListener('message', message => {
  const { origin, data: { kind, eventName, event = {} } } = message;

  if(/^chmln:demo:/.test(kind)) {
    analytics.track(eventName, event);
  }
});
```

#### All message kinds listed + analytics tracking :id=example1

```javascript
iframe.addEventListener('message', message => {
  const { origin, data: { kind, demo, event = {} } } = message;
  // `kind` is one of the value in the following table
  // `demo` is the full demo object
  // `event` will hold a nicely formatted object that can be passed to Segment, Mixpnel, Amplitude, etc. and you can expect at least the following 
  //   `event.demo_id`: the ID of the demo
  //   `event.demo_name`
  //   `event.item_id`: the ID of the demo step
  //   `event.elapsed` : the time since the demo started
  //   ...others

  if (kind === 'chmln:demo:loaded') {
    //
    // The demo is loaded and ready to be interacted with
    //   this is called very quickly after adding the iframe to the page
    //
  } else if (kind === 'chmln:demo:started') {
    //
    // The starting chapter or the first demo interaction was clicked
    //
    analytics.track('Chameleon Demo started', event);

    //
    // An suitable Event name is prodvided for convenience and is used in the example above
    //
    const { eventName } = message.data;

    analytics.track(eventName, event);
    //
  } else if (kind === 'chmln:demo:completed') {
    //
    // The final chapter or final screen was reached
    //
    analytics.track('Chameleon Demo Completed', event);
    //
  } else if (kind === 'chmln:demo:step:started') {
    //
    // The user advances to this screen
    //
    analytics.track('Chameleon Demo Step started', event);
    //
  } else if (kind === 'chmln:demo:component:clicked') {
    //
    // `event` will have component-specfiic data
    //   - `event.component_kind`: values such as hotspot, tooltip, sticker,
    //   - `event.component_text`: the text of this component
    //
    analytics.track('Chameleon Demo Component clicked', event);
    //
  } else if (kind === 'chmln:demo:button:clicked') {
    //
    // `event` will have button-specfiic data
    //   - `event.button_actions`: an array of actions taken, e.g. ['hubspot_scheduler', 'hubspot_flow']
    //   - `event.button_text`: the text of this button, e.g. 'Book demo'
    //
    analytics.track('Chameleon Demo Button clicked', event);
    //
  } else if (kind === 'chmln:demo:form:submitted') {
    //
    // `event` will have form/button-specfiic data
    //   - `event.form_email`
    //   - `event.button_text`: the text of this button, e.g. 'Book demo'
    //
    analytics.track('Chameleon Demo Form submitted', event);
    //
    const { form } = message.data;
    //
    // `form` will contain form-specific data
    // `form.email`
  }
});
```

## Speed, Performance, Caching :id=caching

Including a Product Demo in your marketing site will give your prospective users an inside view
into what it is like to use your product. It may given them the confidence to make a purchase, book a demo, or recommend you to their team.
It's very important to us that your Product Demos load and run very quickly, do not count against your lighthouse score, etc.

If you know that "space" that the Product Demo is given, change the iFrame embed code to specify the height and width in
absolute terms or use CSS to give it a fixed size. This will help with [Cumulative Layout Shift (CLS)](https://web.dev/articles/cls).

Another important metric is [First Contentful Paint (FCP)](https://web.dev/articles/fcp) for which the above-the-fold content is
expected to render very quickly. The Product Demo page, that loads in the iFrame, is cached with `Cache-Control: max-age=31556952, public, no-cache` which
means the page is stored in the user's browser and only re-downloaded if the Demo is changed. Its typically less than 20KB depending
on the length and complexity of the Demo. This page is also cached and served from the global CDN edge nodes of [Fastly](https://fastly.com/) typically
without need to return to the origin server.