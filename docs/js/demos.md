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

#### Profile mode (logged-in user ID) :id=mode-profile

Any and all times that you have information about the logged-in user. All of the information about what properties/data
to send is in the main documentation about [Identifying users](js/profiles.md) but the Tl;DR is that you should send at least a
`uid` as the User ID from your database, the `email`, and `name`.

Feel free to adjust anything other than `class` and `src`.

```html
<iframe class="chmln-demo" loading="lazy" src="https://fast.chameleon.io/edit/demos/:id" style="width: 100%; height: 100%" allow="fullscreen"></iframe>
```

<details>
<summary>Adding User data</summary>

Identifying the user and adding user data allows Demo specific data to be tied back to specific individuals and used in
future segmentation / audience. e.g. the User took a Product Demo of an Enterprise feature and prompt them in-product to start an Enterprise trial

_For simplicity, and unless otherwise specified, adding User ID for an identified user, changes to [consent](js/demos.md?id=cookie-consent) of `granted`._

```javascript
(async () => {
  const user = await fetchCurrentUser(); // Note: use your current user function

  if(!user?.id) {
    return;
  }

  const { id: uid, email, name } = user;

  // Add user data to Product demos
  const demoElements = [...document.querySelectorAll('.chmln-demo')];
  const profile = { uid, email, name };

  demoElements.forEach(demoEl => demoEl.src = srcWithData(demoEl.src, JSON.stringify({ profile })));

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


#### Anonymous mode (the default) :id=mode-anonymous

When `profile` is missing the Demo runs in **anonymous mode**.

```html
<iframe class="chmln-demo" loading="lazy" src="https://fast.chameleon.io/edit/demos/:id" style="width: 100%; height: 100%" allow="fullscreen"></iframe>
```


### Consent to track (cookies etc.) :id=cookie-consent

Start with consent mode of "consent not yet given", with the value `pending`, then update when the user gives or denies
consent by setting the `consent` value on the Demos with either `granted` : `denied`.

> Typically, Product Demos fall into the **Functional** category.

```html
<iframe class="chmln-demo" loading="lazy" src="https://fast.chameleon.io/edit/demos/:id#consent=granted" style="width: 100%; height: 100%" allow="fullscreen"></iframe>
```

Once the consent screen is dismissed

```javascript
//
// All Demos start with consent mode 'pending' by default; Set to 'granted' or 'denied' after the user decides about tracking
//
const srcWithData = (url, data) => `${url.split('#')[0] || url}#${Object.entries({ ...Object.fromEntries(new URLSearchParams(url.split('#')[1])), ...data }).map(([k, v]) => `${encodeURIComponent(k)}=${encodeURIComponent(v)}`).join('&')}`;

const demoElements = [...document.querySelectorAll('.chmln-demo')];
const trackingAllowed = true; // Note: Use your method to check for this true/false value
const consent = trackingAllowed ? 'granted' : 'denied';

demoElements.forEach(demoEl => demoEl.src = srcWithData(demoEl.src, { consent }));
```


### Schema of properties :id=schema

These control different aspects of the Product Demo including identity, use of cookies, prefilled data, etc.
The data is passed to the iframe via the hash parameters and objects like `profile` and `options` should be JSON encoded first before being handed to `srcWithData`
Sending the `profile` is **highly recommended** as a method of connecting the dots from
engagement with Product Demos into the other experiences that Chameleon offers such as [Tours](apis/tours.md)),
[Microsurveys](apis/surveys.md), and [HelpBar](apis/search.md). 


| Property                  | Values                         | Description                                                                                                                 |
|---------------------------|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `consent`                 | `granted`, `denied` , `pending`| Whether or not consent has been given. Defaults to `granted`. Change this when the user gives or denies consent             |
| `profile`                  | {"uid":"5a17d4", ...}          | A JSON object of data about the current user (encode as JSON before passing to `srcWithData`)                               |
| `options.session_timeout` | `0`, `1`, `15`, `30`...        | The duration (in minutes) before the user's session expires automatically. Set to 0 to disable session persistence entirely.|


## JavaScript API :id=js-api

The iframe uses `window.parent.postMessage` to communicate information back to the parent page. Chameleon also communicates to the Chameleon
JavaScript [installation](https://help.chameleon.io/en/articles/1161793-installing-directly-using-javascript). Below are the messages you can expect from the iframe at the relevant times in the Demo. Message are described below as being sent but this just
means that any listener to `window.addEventListener('message', message => ...)` will be called.

The `message` parameter to the callback function is a [MessageEvent](https://developer.mozilla.org/en-US/docs/Web/API/MessageEvent) where `message.data` is the object sent
from inside the iframe, akin to webhooks (but on the client side).

### Message event kinds :id=schema-kinds


| Event kind                     | Event name                       | Description                                                                                          |
|--------------------------------|----------------------------------|------------------------------------------------------------------------------------------------------|
| `chmln:demo:started`           | Chameleon Demo Started           | When the user clicks on the first step                                                                |
| `chmln:demo:completed`         | Chameleon Demo Completed         | When the last step of the demo is reached. This can happen directly or via branching                 |
| `chmln:demo:restarted`         | Chameleon Demo Restarted         | When the user clicks of any call to action that results in restarting from the beginning             |
| `chmln:demo:step:started`      | Chameleon Demo Step Started      | When a Step is displayed to the user; typically because of clicking on the previous step             |
| `chmln:demo:step:completed`    | Chameleon Demo Step Completed    | When a Step is displayed to the user; typically because of clicking on the previous step             |
| `chmln:demo:step:previous`     | Chameleon Demo Step Completed    | When a Step is displayed to the user; typically because of clicking on the previous step             |
| `chmln:demo:component:clicked` | Chameleon Demo Component Clicked | When a Hotspot, Tooltip, etc. is clicked                                                             |
| `chmln:demo:button:clicked`    | Chameleon Demo Button Clicked    | When a Button is clicked. Buttons appear in many different places including Tooltips, Chapters, etc. |
| `chmln:demo:form:submitted`    | Chameleon Demo Form Submitted    | When a form is submitted such as adding an email address and clicking "Learn more"                   |


### Examples

The example code using `analytics.track` should be adapted for how you track analytics in your product. This can also be completely omitted from your
implementation and Demos will run just fine. _Consider this optional_.

#### Generic analytics tracking :id=example0

```javascript
window.addEventListener('message', message => {
  const { data: { kind, eventName, event = {} } = {} } = message;

  if(/^chmln:demo:/.test(kind)) {
    // TODO: Replace this block with your event tracking call (e.g. mixpanel.track(eventName, event); etc.)

    // Segment.com / Rudderstack
    analytics.track(eventName, event);

    // Adds this event into your data warehouse or other backend system
    sendEventToSnowflake(eventName, event);
  }
});
```

#### Analytics tracking :id=example1

```javascript
window.addEventListener('message', message => {
  const { data: { kind, eventName, event = {} } = {} } = message;

  if(/^chmln:demo:/.test(kind)) {
    // TODO: Replace this block with your event tracking call (e.g. mixpanel.track(eventName, event); etc.)
    // Below are a quick reference to the various tracking calls -- let us know if we're missing something here

    // Segment.com / Rudderstack
    analytics.track(eventName, event);

    // Freshpaint
    freshpaint.track(eventName, event);

    // Heap
    heap.track(eventName, event, 'chameleon'); // 'chameleon' as the third argument is for data grouping within Heap

    // Customer.io
    _cio.track(eventName, event)

    // Intercom
    Intercom('trackEvent', eventName, event)

    // Fullstory
    FS.event(eventName, event);

    // Google Analytics
    window.gtag('event', eventName, { ...event, event_category: 'Demo', event_label: event.demo_name });
  }
})
```

#### Custom handling of individual events :id=example2

```javascript
window.addEventListener('message', message => {
  const { data: { kind, demo, event = {} } = {} } = message;
  // `kind` is one of the value in the following table
  // `demo` is the full demo object
  // `event` will hold a nicely formatted object that can be passed to Segment, Mixpnel, Amplitude, etc. and you can expect at least the following 
  //   `event.demo_id`: the ID of the demo
  //   `event.demo_name`
  //   `event.tag_names`: The names of the tags set in the Chameleon dashboard
  //   `event.step_id`: the ID of the demo step
  //   `event.elapsed` : the time since the demo started
  //   ...others

  if (kind === 'chmln:demo:started') {
    //
    // The starting chapter or the first demo interaction was clicked
    //
    analytics.track('Chameleon Demo Started', event);

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
    analytics.track('Chameleon Demo Step Started', event);
    //
  } else if (kind === 'chmln:demo:component:clicked') {
    //
    // `event` will have component-specfiic data
    //   - `event.component_id`
    //   - `event.component_kind`: values such as hotspot, tooltip, sticker, etc.
    //   - `event.component_title`: the text/title of this component
    //   - `event.component_body`: the body/description of this component
    //
    analytics.track('Chameleon Demo Component Clicked', event);
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
**It is very important to us that your Product Demos load and run very quickly**, do not count against your lighthouse score, etc.

If you know the max height and width that a Product Demo is given, change the iframe embed code to specify the height and width in
absolute terms or use CSS to give it a fixed size. This will help with [Cumulative Layout Shift (CLS)](https://web.dev/articles/cls).

Another important metric is [First Contentful Paint (FCP)](https://web.dev/articles/fcp) for which the above-the-fold content is
expected to render very quickly. The Product Demo page, that loads in the iframe, is cached with `Cache-Control: max-age=31556952, public, no-cache` which
means the page is stored in the user's browser and only re-downloaded if the Demo is changed. This page is typically less than 20KB depending
on the length and complexity of the Demo. This page (and all other assets within the iframe) are cached and served from the global CDN edge nodes of [Fastly](https://fastly.com/).
Typically without need to return to the origin server. Response times for iframe are typically less than 100ms, often 40ms, and almost always below 400ms.
The rest of the contents of the iframe load only when needed and only as progress through the Demo occurs.