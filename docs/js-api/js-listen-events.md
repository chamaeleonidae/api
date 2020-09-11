# Listen to Chameleon events

**Register a callback to certain state changes and events; useful for custom integrations with Chameleon**



*For an overview of how the Chameleon API works, please first read* [*this article*](https://help.trychameleon.com/developer-docs/api-basics)*.*

------



You can send data automatically collected by Chameleon to your database or any other tools, using the methods below. 

Have an overview of the data Chameleon collects for analysis, by reading [this article](https://help.trychameleon.com/en/articles/1226450-what-analytics-does-chameleon-provide).

## List of supported events

- `load` - when the `chmln` JavaScript has been loaded onto the page (but before any other processing is done).

- `after:account` - After the account data is present on the page.
- `after:profile` - After the user loads from the Chameleon backend API, now all of the profile data is loaded.

- `chmln:event` - All Survey, Tooltip, Tour, and Launcher events. For more information about which events Chameleon tracks, see [this doc](https://help.trychameleon.com/en/articles/1226450-what-analytics-does-chameleon-provide), or download a data schema [here](https://docs.google.com/spreadsheets/d/1qBiAojhSoUSEGLlwvzAhO5CxFLTNeutA_h2iV9gsvRk/copy).
- `tour:event`  - Only Survey and Tour events, including Started, Completed, Exited, Step Seen, Button Clicked, etc.

## Examples

- [Listen for Tour/Survey events -- send to custom integration](#Listen for Tour/Survey events -- send to custom integration)

- [Send properties](#Send properties)

- [Sending data to other tools directly](#Sending data to other tools directly)


  

#### Listen for Tour/Survey events -- send to custom integration

This might be relevant in the following instances:

- Sending data to a tool without a native Chameleon integration.
- Sending data to a tool via a backend/server-side method.

```
// Tour / Survey events only
chmln.on('tour:event', function(eventName, options) {
  $http.post(internal_event_logging_url, {
    name: eventName, 
    properties: options
  });
});

// Tour / Survey / Tooltip / Launcher etc. events
chmln.on('chmln:event', function(eventName, options) {
  $http.post(internal_event_logging_url, {
    name: eventName, 
    properties: options
  });
});
```



#### Send properties

This might be relevant in the following instances:

- Sending data to your database, to allow deeper analysis of Chameleon events.
- Sending data that is not collected by your analytics tool (e.g. "Chameleon testing ID").

```
chmln.on('after:profile', function() {
  $http.post(internal_user_update_url, {
    chameleon_testing_id: chmln.data.profile.get('percent'),
  });
});
```



#### Sending data to other tools directly

For example, you can send the Chameleon "Percentage value" to your analytics solution, using a script like the below *(with examples for Segment and Mixpanel)*:

```
chmln.on('after:profile', function() {
  // Now you have full access to chmln.data.profile
  
  var percent = chmln.data.profile.get('percent'));
  // Segment.com
  // analytics.identify({chameleon_testing_id: percent})

  // Mixpanel
  // mixpanel.people.set({chameleon_testing_id: percent})
})
```

> *Note: You can easily adapt this based on where you'd like to send this data in your system.* 
