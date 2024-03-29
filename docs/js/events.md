# Send Events via JS API

**Track custom Events into Chameleon from you client-side JavaScript.** Looking for the [REST API](webhooks/events.md)?

---

Sending Event data to Chameleon can be valuable for:

- Targeting users with Tours based on what they have done.
- Tracking Conversion Goals for Tours.



## Tracking user action data

If you have implemented Chameleon directly via the JavaScript snippet (and have not used Segment.com) then you may wish to supplement your user attribute data with user action data. This will be powerful for showing Tours in response to what users do.
To use the **JavaScript API**, using our `chmln.track` method:

```
chmln.track(EVENT_NAME);  // The name of the event (e.g. "Subscribed to Plan", "Imported leads")
```

> *Note: Chameleon ignores Events from admins, so they don't clog up your analytics. In order to test whether the track method on your page is working, you'll need to be logged out of the browser you're testing on, or use Chameleon's [Test Mode](https://help.chameleon.io/en/articles/1201812-how-can-i-test-my-chameleon-experience#test-mode).*

