# Send user properties via JS API

**Create and update data attributes for users and companies**

---



Syncing user and company data to Chameleon account can be helpful for: 

- [Targeting users](apis/segments.md) with Tours based on who they are.
- [Personalizing content](concepts/personalizing.md) within Experiences (merge tags in content).
- Better URL matching (merge tags in URLs).


## Identifying user :id=profile

**Users need to be identified with a unique ID** (`UID`) to enable them to see Tours. This can be your database ID or another stable user identifier.
We also recommend also sending `email` to maintain a user's identity across Chameleon and any integrations you enable.

Use the `chmln.identify` method, calling this as soon as the user is identifiable on page load. 

> *Note: These are example scripts, don't forget to change the PLACEHOLDERS.*

```
chmln.identify(USER.ID_IN_DB, { // Unique ID in your database
  email: USER.EMAIL,
  // Add other pertinent parameters here
});
```

You can also send other attributes associated with a user in the same manner. 

This includes any company (group) associated with the user, and related company attributes. For this to sync across your integrations, please ensure the unique company identifier (`company UID`) is the same as within your system. 

> *Note: Please confirm the attributes to be sent with your project owner.*

```
chmln.identify(USER.ID_IN_DB, {     // Unique ID in your database (e.g. 23443 or "590b80e5f433ea81b96c9bf6")
  email: USER.EMAIL,                // Put quotes around text strings (e.g. "jim@example.com")
  created: USER.SIGN_UP_DATE,       // Send dates in ISO or unix timestamp format (e.g. "2017-07-01T03:21:10Z" or 1431432000)
  name: USER.NAME,                  // We will parse this to extra first and last names (e.g. "James Doe")
  role: USER.ROLE,                  // Send properties useful for targeting types of users (e.g. "Admin")
  logins: USER.LOGIN_COUNT,         // Send any data about user engagement (e.g. 39)
  ...
  project: USER.PROJECT_ID,         // Send any unique data for a user that might appear in any page URLs (e.g. 09876 or "12a34b56")

  company: {                        // For B2B products, send company / account information here
    uid: COMPANY.ID_IN_DB,          // Unique ID of the company / account in your database (e.g. 9832 or "590b80e5f433ea81b96c9bf7")
    created: COMPANY.SIGN_UP_DATE,  // To enable targeting all users based on this company property
    name: COMPANY.NAME,             // Send any data that appears within URLs, such as subdomains (e.g. "airbnb")
    trial_ends: COMPANY.TRIAL_ENDS, // Send data about key milestones (e.g. "2017-08-01T03:21:10Z")
    version: COMPANY.VERSION,       // If your software varies by version then this will help show the correct guidance (e.g. "1.56")
    plan: COMPANY.PLAN,             // Send null when no value exists (e.g. "Gold", "Advanced")
    ...
    spend: COMPANY.CLV              // Send other properties that will help in targeting users (e.g. sales rep, source, stage)
  },
});
```

**What is necessary for a UID?**

A UID simply needs to be a stable, unique string that identifies the current user.
No user will share a UID one with another user, and stable meaning it won't change between servers, logins, or browsers.


## Identifying companies/accounts :id=company

Simply include a company key in the call to identify

```
chmln.identify(USER.ID_IN_DB, {
  company: {
    uid: COMPANY.ID_IN_DB,
    ...
  },
});
```

## Seeing existing user properties

To view the user properties associated with the **current user**, you can use the following command within the JS console:

```
chmln.data.profile.attributes
```

To see **all** the user properties currently being sent, you can run some code in your local browser. Open the JavaScript console, under Developer Tools and paste the following code and hit Enter:

```
chmln.data.segment_properties.where({kind: 'profile', source: 'chmln'}).map(function(p) { return p.get('prop') })
```

Here are some more examples of what you might send (in Ruby, Javascript, Ajax and PHP). More available on [our Github](https://github.com/trychameleon/snippet.js/tree/master/examples).

**Ruby:**

```
  // Add the snippet here with account id (i.e. '<%= ENV['CHAMELEON_ACCOUNT_TOKEN'] %>')
  // Assuming you have exposed `helper_method :current_user?` in your `ApplicationController`
  
  <% if current_user? %>
    chmln.identify({
      uid: '<%= current_user.id %>',
      created: '<%= current_user.created_at.iso8601 %>',
      email: '<%= current_user.email %>',
      plan: '<%= current_user.account.plan_name %>',
      spend: '<%= current_user.account.plan_cost %>'
    });
  <% end %>
```

**JavaScript:**

```javascript
// Add the snippet here with account id (i.e. config.chameleonAccountId)
// Assuming you preload your page with a current user

(() => {
  if (currentUser.id) {
    chmln.identify(currentUser.id, {
      created: currentUser.createdAt,
      email: currentUser.email,
      plan: currentUser.planName,
      spend: currentUser.planCost
    });
  }
})();
```

**Ajax:**

```javascript
// Add the snippet here with account id (i.e. config.chameleonAccountId)
// Assuming you call `currentUserLoaded` after fetching the user

(() => {
  const currentUserLoaded = (currentUser) => {
    chmln.identify(currentUser.id, {
      created: currentUser.createdAt,
      email: currentUser.email,
      plan: currentUser.planName,
      spend: currentUser.planCost
    });
  };

  // Using fetch API (modern)
  fetch('/user.json')
    .then(response => response.json())
    .then(data => {
      // Setup other aspects of the environment
      currentUserLoaded(data.user);
    })
    .catch(error => console.error('Error fetching user:', error));

  // Or using jQuery (legacy)
  // const xhr = $.get('/user.json');
  // xhr.done(data => currentUserLoaded(data.user));
})();
```

**PHP:**

```php
  // Add the snippet here with account id (i.e. <?php echo $GLOBALS['chameleonAccountId'] ?>)
  // Assuming your page has loaded the current user as the object $current_user
  
  <?php if (var_dump((bool) $current_user->present)): ?>
    chmln.identify('<?php echo $current_user->id ?>', {
      created: '<?php echo $current_user->created_at ?>',
      email: '<?php echo $current_user->email ?>',
      plan: '<?php echo $current_user->account->plan_name ?>',
      spend: '<?php echo $current_user->account->plan_cost ?>'
    });
  <?php endif; ?>
```


## Clearing / disabling the Chameleon install :id=clear

Use this function to de-identify the user and stop Chameleon from operating on the page (including showing no more Experiences).

- When the user is logged out of a single page app that does not perform a full-page refresh
- When your application enters a "mode" where automatic delivery of Chameleon Experiences should no longer happen (i.e. in full-screen mode)

```javascript
chmln.clear();
```


## Disabling Experiences for specific users :id=disable

By default, all users that match the target audience will see a Chameleon Experience when they first visit the page where that Experience automatically begins.
Users will see this Experience until they complete or exit it, and then not again. 

However you can **prevent certain users from seeing any Experiences, by adding a property to their user profile**:  `disabled: true`.


## Timestamps

Chameleon will interpret a property as a timestamp for a few reasons:

1. If the timestamp is [ISO 8601 standard](https://en.wikipedia.org/wiki/ISO_8601), Chameleon will **always** assume the value is a timestamp.
2. If the timestamp is a Unix Timestamp that falls between 1973 and 2033 and the name is either 'created', or ends in '_at' or '_time'. 

Chameleon will interpret any of these properties as a timestamps:

```json
{
  "started": "2026-09-05T15:45:39+00:00",
  "ended": "2026-09-05T15:45:39Z",
  "a_date": "2216-09-05",
  "created": 1472985601,
  "started_at": 1095292800,
  "ended_at": 1095352800
}
```


## Default properties

From the JavaScript code snippet, we collect a set of default properties that cannot be overridden, they are `browser_x`, `browser_n` and `browser_tz`. In addition, our servers add `browser_l` , `last_seen_session_count` , `last_seen_at` , and `last_last_seen_at` which cannot be permanently overridden.



## Reserved Keywords

Chameleon has some reserved keywords that are not passable in identify. They include: `id`, `user_id`, `userId`, `account_id` , `accountId` , `profile_id`, `profileId`, `company_id`, `companyId`, `company`, `created_at`, `createdAt` , `updated_at`, `updatedAt` , `options`, `at`, `last_seen_at`, `last_request_at`, `now`, `integration`, `disabled`, `chameleon_admin`, `chameleon_tag_ids` and `percent` .


## Limits and Errors

- Up to a total of 768 bytes are stored for each scalar value where each Array item and each Hash value can reach this limit.
- See the full page on [Limits](concepts/normalization.md?id=limits) for more information.
- Any data received that exceeds this limit will be truncated at the 768th byte and a warning surfaced on the data management page for [user data](https://app.chameleon.io/data/properties/profile) or for [company data](https://app.chameleon.io/data/properties/company).


