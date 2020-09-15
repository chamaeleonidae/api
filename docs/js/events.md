# Send events via JS API

*Track and send event data for users.*

---


Sending event data to Chameleon can be valuable for:

- Targeting users with tours based on what they have done.
- Tracking conversion goals for tours.



## Tracking user action data

If you have implemented Chameleon directly via the JavaScript snippet (and have not used Segment.com) then you may wish to supplement your user attribute data with user action data. This will be powerful for showing tours in response to what users do. 



To use the **JavaScript API**, using our `chmln.track` method:

```
chmln.track(EVENT_NAME);  // The name of the event (e.g. "Subscribed to Plan", "Imported leads")
```

> *Note: Chameleon ignores events from admins, so they don't clog up your analytics. In order to test whether the track method on your page is working, you'll need to be logged out of the browser you're testing on, or use Chameleon's [Test Mode](https://intercom.help/chameleon/becoming-a-chameleon-expert/testing-analyzing-and-iterating/how-can-i-test-my-tour#test-mode).*

