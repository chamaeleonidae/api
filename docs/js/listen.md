# Listen to Chameleon events

**Register a callback to certain state changes and events. This can be useful for custom integrations with Chameleon**

This doc talks about the `chmln.on` JavaScript API method.

Common use cases include:

- Syncing the Experience interaction data (automatically collected by Chameleon) to your database/warehouse or any other tools, using the methods below.
- Getting access to the A/B testing attribute (`percent`) when the Chameleon [User Profile](apis/profiles.md?id=schema) is loaded.
- Logging Experience data to an integration that Chameleon does not yet have a native integration with
- Knowing when the [Search bar](apis/search?id=search-js-api) is opened/closed or when data is needed.

----

An overview of the data Chameleon collects for analysis, by reading [this article](https://help.chameleon.io/en/articles/1226450-what-analytics-does-chameleon-provide).


## List of supported events

- `chmln:event` - All Survey, Tooltip, Tour, and Launcher events. For more information about which events Chameleon tracks, see [this doc](https://help.chameleon.io/en/articles/1226450-what-analytics-does-chameleon-provide), or download a data schema [here](https://docs.google.com/spreadsheets/d/1qBiAojhSoUSEGLlwvzAhO5CxFLTNeutA_h2iV9gsvRk/copy).
- `tour:event`  - Only Survey and Tour events, including Started, Completed, Exited, Step Seen, Button Clicked, etc.

- `after:account` - After the account data is present on the page.
- `after:profile` - After the User Profile loads from the Chameleon backend API, now all of the profile data is loaded.

- `load` or `load:chmln` - When the Chameleon JavaScript has been loaded but before any Experiences will display/show/start.
- `identify:request` - Triggered directly before the network request associated with identifying this User Profile. The callback signature (arguments) are `options, profile` with options having yet to be added to the profile object.
- `identify:sync` - Triggered upon the completion of the network request associated with identifying this User Profile.

- `helpbar:navigate` - When the Search bar needs to navigate within the single-page app
- `helpbar:search` - When the Search bar is making a query; use to override the default behavior
- `helpbar:opened` - Know when the Search bar is opened
- `helpbar:closed` - Know when the Search bar is closed 
- `helpbar:item:action` - Know when a specific `SearchItem` is triggered
- `helpbar:item:action:error` - When a specific `SearchAction` encounters an error
- `helpbar:recent` - When the search bar needs a list of the most recently actioned `SearchItem`s; use to override the default behavior
- `helpbar:suggestions` - When the search bar needs a list of suggested `SearchItem`s; use to override the default behavior


> **Typical ordering as Chameleon boots**: `load`, `load:chmln`, `after:account`, `identify:request`, `identify:sync`, `after:profile`, `tour:event`, `chmln:event`

## Examples

#### Search bar

The [JavaScript API for Search bar](apis/search?id=search-js-api) has many examples and use cases.

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

- Sending data to your database, to allow deeper analysis of Chameleon Events.
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


