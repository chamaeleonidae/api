# Personalizing

**Personalizing is the way to adjust Experience content to match the User who is viewing an Chameleon Experience.**

---

| Helper name                | -                                                              | description                                                                           |
|----------------------------|----------------------------------------------------------------|---------------------------------------------------------------------------------------|
| `property`                 | [examples ↓](concepts/personalizing.md?id=examples-property)   | The default used when a unquoted string is found at the beginning                     |
| `global`                   | [examples ↓](concepts/personalizing.md?id=examples-global)     | Pull a value from the window object, useful for extra-advanced conditional formatting |
| `pluralize`                | [examples ↓](concepts/personalizing.md?id=examples-plural)     | Given a specific number and a word produces a phrase with the correct tense           |
| `time_difference_in_words` | [examples ↓](concepts/personalizing.md?id=examples-time-diff)  | Given a specific date/time produces a time offset                                     |
| `time_ago`                 | [examples ↓](concepts/personalizing.md?id=examples-time-ago)   | Calculates the offset from now in `seconds`,`minutes`,`hours`,`days`,`weeks`,`years`  |
| `time_local`               | [examples ↓](concepts/personalizing.md?id=examples-time-local) | Given a specific date/time uses toLocalString() to generate a human readable string   |
| `delivery`                 | [examples ↓](concepts/personalizing.md?id=examples-delivery)   | Personalize with content explicitly sent via a [Delivery](apis/deliveries.md)         |
| `html`                     | [examples ↓](concepts/personalizing.md?id=examples-html)       | Output html based on given options                                                    |
| `filter`                   | [examples ↓](concepts/personalizing.md?id=examples-filter)     | Use filter to evaluate [Segmentation filter expressions](concepts/filters.md)         |                                  |
| `if` (content logic)       | [examples ↓](concepts/personalizing.md?id=examples-logic-if)   | Output html based on given options                                                    |


## Examples :id=examples

Current reference time is `2029-04-04T12:00:00Z` -- this is "now" for the purpose of date-based examples below.

##### Example user data :id=example-user-data

```json
{
  "first_name": "Alice",
  "role": "Product manager",
  "created": "2027-03-04T12:02:00Z",
  "created_at": "2028-03-04T12:02:00Z",
  "time_z": "Europe/Brussels",
  "plan": {
    "name": "Growth",
    "spend": 734,
    "started_on": "2029-01-02T09:13:00Z",
    "upgrade_on": "2029-04-08T13:31:00Z",
    "features": ["unlimited_widgets", "coffee"],
    "upgrade_spend": 893
  },
  "credits": {
    "used": 19,
    "remaining": 1
  },
  "account_info": {
    "csm_name": "Aria Jones",
    "csm_calendly": "https://calendly.com/acme-aria-j/30-min"
  }
}
```


### Greeting with a User's name | `property` helper :id=examples-property

```text
Hey {{first_name}} 👋!
# Hey Alice 👋!

Hey {{property "first_name"}} 👋!
# Hey Alice 👋!
```

### Greeting with a User's name + gentle fallback | `property` helper

```text
Hey {{first_name fallback="there"}}!
# Hey Alice!

Hey {{name fallback="there"}}!
# Hey there!

Hey {{property 'name' fallback='there'}}!
# Hey there!
```


### Using nested data | `property` helper

```text
You're subscribed to the {{plan.name}} plan.
# You're subscribed to the Growth plan.

You're subscribed to the {{property 'plan.name'}} plan.
# You're subscribed to the Growth plan.
```

### Use a relative offset time | `time_difference_in_words` helper :id=examples-time-diff

```text
You signed up {{time_difference_in_words created}}.
# You signed up 2 years ago.

You were first seen by Chameleon {{time_difference_in_words created_at}}.
# You were first seen by Chameleon 1 year ago.

You signed up {{time_difference_in_words created tense="in yonder past"}}.
# You signed up 2 years in yonder past.

Thanks for being a customer for {{time_difference_in_words created tense=''}}!
# Thanks for being a customer for 2 years!

Thanks for being a identified to Chameleon for {{time_difference_in_words created_at tense=''}}!
# Thanks for being a identified to Chameleon for 1 year!
```

### Calculate differences between dates | `time_ago` helper :id=examples-time-ago

This calculation is best used as a nested helper in an `if` block | [examples ↓](concepts/personalizing.md?id=examples-logic-if)

**This examples assumes that the current time is `2029-04-04T12:00:00Z`**

The value of the option `in` defaults to `seconds` but can be any of `milliseconds`, `seconds`, `minutes`, `hours`, `days`, `weeks`, `years`

```text
Created {{time_ago created}} seconds ago.
# Created 65836680 seconds ago.

Created {{time_ago created in='seconds'}} seconds ago.
# Created 65836680 seconds ago.

Created {{time_ago created in='minutes'}} minutes ago.
# Created 1097278 minutes ago.

Created {{time_ago created in='hours'}} hours ago.
# Created 18287 hours ago.

Created {{time_ago created in='days'}} days ago.
# Created 761 days ago.

Created {{time_ago created in='weeks'}} weeks ago.
# Created 108 weeks ago.

Created {{time_ago created in='years'}} years ago.
# Created 2 years ago.

Created {{time_ago created in='milliseconds'}} milliseconds ago.
# Created 65836680000 milliseconds ago.
```

**As part of an `if` block** | [more examples ↓](concepts/personalizing.md?id=examples-logic-if)

```handlebars
{{if plan.spend > 500 && {time_ago started_on in="weeks"} > 12}}
To get the most out of account, [book a review]({{account_info.csm_calendly}}) with your Account manager, {{account_info.csm_name}}.
{{else}}
Check out these [additional resources](https://help.your-product.co/getting-started)
{{/if}}

# To get the most out of account, [book a review](https://calendly.com/acme-aria-j/30-min) with your Account manager, Aria Jones.
```


### Display a timestamp/date in a presentable format | `time_local` helper :id=examples-time-local

Internally this helper generates a `Date` object and then calls `toLocaleString`.

> Use for feature launches, maintenance windows, expiration dates for surveys/deals, etc.

- The first argument to `toLocaleString` is the locale of the identified user
  1. If you use [Translations](https://help.chameleon.io/en/articles/5868890) then it will be the same locale you've configured.
  1. The browsers reported locale.

- The second argument is any `options` that are passed to the `time_local` helper. The examples below are non-exhaustive and you can use any/all of the `options` found in the [`toLocaleString` reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleString) or [options reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#options)


##### Examples using `created_at` from above, where the user is in Pacific time with browser language `en-US`

```text
{{time_local created_at}} # the default
# 3/4/2028, 4:02:00 AM

{{time_local created_at dateStyle="long" timeStyle="long"}} # nicer looking format
# March 4, 2028 at 4:02:00 AM PST

{{time_local created_at year="numeric" weekday="long" month="short" day="numeric"}} # without the time
# Thursday, Mar 4, 2028

{{time_local created_at year="numeric" weekday="long" month="short" day="numeric" hour="numeric" minute="numeric"}} # nicer looking format with hours
# Thursday, Mar 4, 2028, 4:00 AM

{{time_local created_at timeZoneName="short"}} # for a user in Pacific time; show the timezone
# 3/4/2028, 4:02:00 AM PST

{{time_local created_at timeZone="UTC"}} # lock to UTC
# 3/4/2028, 12:02:00 PM

{{time_local created_at timeZone=time_z}} # for a user who has a `time_z` property for Brussels (time_z without quotes since it's a user property)
# 3/4/2028, 1:02:00 PM

{{time_local created_at timeZone=time_z timeZoneName="short"}} # short Brussels
# 3/4/2028, 1:02:00 PM GMT+1

{{time_local created_at timeZone=time_z timeZoneName="long"}} # long Brussels
# 3/4/2028, 1:02:00 PM Central European Standard Time
```


##### Examples using a fixed string date value, where the user is in Pacific time with browser language `en-US`

```text
{{time_local '2026-05-01'}} # Release date (assumed midnight UTC)
4/30/2026, 5:00:00 PM

{{time_local '2026-05-01T00:00:00Z'}} # Release time in UTC
4/30/2026, 5:00:00 PM

{{time_local '2026-05-01T11:00:00 -08:00'}} # anchor to a 11am release time in Pacific time
5/1/2026, 11:00:00 AM

{{time_local '2026-05-01' year="numeric" weekday="long" month="short" day="numeric"}}
# Thursday, Apr 30, 2026
```

##### Examples where the user is in Spain with browser language `es-ES`

```text
{{time_local created_at timeZone=time_z timeZoneName="long"}}
# 3/4/2028, 1:02:00

{{time_local '2026-05-01' year="numeric" weekday="long" month="short" day="numeric"}}
# jueves, 30 de abr de 2026
```

##### Examples where the user is in France with browser language `fr`

```text
{{time_local created_at timeZone=time_z timeZoneName="long"}}
# 3/4/2028, 1:02:00 heure d’été d’Europe centrale

{{time_local '2026-05-01' year="numeric" weekday="long" month="short" day="numeric"}}
# jeudi 30 avr. 2026
```


### Pluralizing numbers | `pluralize` helper :id=examples-plural

The tense word can be singular **or** plural when it's passed in.

```text
You've used {{pluralize credits.used "credit"}} and have {{pluralize credits.remaining "credit"}} left.
# You've used 19 credits and have 1 credit left.

Your next bill is for ${{pluralize plan.spend "dollar"}}. # given singular => plural 👍
# Your next bill is for $734 dollars.

Your next bill is ${{pluralize plan.spend "dollars"}}. # given plural => plural 👍
# Your next bill is $734 dollars.
```

----------

## Examples for `global` helper :id=examples-global

```javascript
window.chameleonTheme = { background: "#1f1f24", primary: "#7856ff" };
window.chameleonContent = {
  more_help_demo_offering: {
    title: "Need a bit more help?",
    body: "We're invested in seeing you succeed",
    cta: "Book a demo",
    account_manager_calendly: "https://calendly.com/your-account-manager/book-a-demo",
  },
  ...
};
```


#### Book a demo with the User's account manager | `global` helper

```text
# title
{{global "chameleonContent.more_help_demo_offering.title"}}

# body
{{global "chameleonContent.more_help_demo_offering.body"}}

# as the text of the Primary call to action button
{{global "chameleonContent.more_help_demo_offering.cta"}}

# as the "Additional action" field for the Primary call to action button
{{global "chameleonContent.more_help_demo_offering.account_manager_calendly"}}
```

#### Call a function (show a alert modal)

> Note that this function should be added to your product's codebase to provide extended functionality. In this example we will assume you have a `performAction` function defined like this:

```javascript
//
// Example showAlert function added to your frontend codebase
//
window.performAction = (type, text, options) => {
  if(type === 'create_draft') {
    // Create the new draft and then route to the editing page
    //  Use the text as the title of the new Draft or to generate AI content
    //
    // From example [1], type='create_draft' and text='My first draft' (leaving options undefined)
    //
  } else if(type === 'create_import') {
    // Create a new data import and route to where the data import workflow starts
    //  Use the text as the input to GPT to generate the template
    //
    // From example [2], type='create_import', text='First Contacts' and options={ data_type: 'Contact', via: 'Chameleon' }
    //
  }
}
```

```text
# [1] Create a new draft with this title
{{global 'performAction' 'create_draft' 'My first draft'}}

# Create a new draft with this Prompt to your draft generator
{{global 'performAction' 'create_draft' 'Generate placeholder text relating to a list of important items to remember for publishing content'}}

# [2] Create a new data import passing the data_type and via options
{{global 'performAction' 'create_import' 'First Contacts' data_type='Contact' via='Chameleon'}}

# [3] Using user properties in function calls
# ✅ Correct - user property without quotes (gets resolved to user's value)
{{global 'performAction' 'create_draft' first_name}}

# ✅ Correct - mixing user properties and literal strings
{{global 'performAction' 'create_import' company.name data_type='Contact' via='Chameleon'}}

# ❌ Incorrect - user property with quotes becomes literal text
{{global 'performAction' 'create_draft' 'first_name'}}

# ❌ Incorrect - nested braces not supported in function arguments
{{global 'performAction' 'create_draft' {{first_name}}}}
```

> **Important**: When passing user properties to functions, use the property name **without quotes or double braces**. Quoted values (`'text'`) are passed as literal strings, while unquoted properties (`user_property`) are resolved to the user's actual property value.


## Examples using `delivery` helper :id=examples-delivery

**More information about Deliveries can be found on the [Deliveries API reference](apis/deliveries.md).**

A Delivery is a REST API for directly **triggering an Experience** for a **specific User**.

> With a Delivery you can include personalized content for that specific instance of that Delivery.
> Note that the `delivery` helper documented here only works for the specific Experience that was triggered via Delivery.
> Make sure to configure your Experience to **only** show Manually.

##### Example Delivery

```json
{
  "id": "5f3c4232c712de665632a6d4",
  "model_type": "survey",
  "model_id": "5f3c4232c712de665632a6d5",
  "options": {
    "salutation": "Good day",
    "account_manager": {
      "name": "Julia",
      "calendly": "https://calendly.com/your-account-manager-julia/book-a-demo"
    }
  }
}
```


#### Book a demo with the User's account manager | `delivery` helper

```text
{{delivery "salutation"}} {{first_name}}, we have a new product launching next month, can we show it off to you?
Good day Alice, we have a new product launching next month, can we show it off to you?

Book a demo with {{delivery "account_manager.name"}} ✨
# Book a demo with Julia ✨
```

```text
# as the "Additional action" field for the Primary call to action button
{{delivery "account_manager.calendly"}}
```

```text
# as the "Additional action" field for the Primary call to action button
{{delivery "account_manager.calendly"}}
```



### Show a custom link | `html` helper :id=examples-html

```text
{{html 'Read' tagName='a' href='/read-more' target='read-more-tab' data-read-more='link' style='color: red'}}
# <a href="/read-more" target="read-more-tab" data-read-more="link style="color: red">Read</a>
```



### Use custom logic | `if` block helper :id=examples-logic-if

When the _condition_ evaluates to truthy, the content in the `if` block is used, otherwise the `else` block is used.
A condition is a JS-like combination of a "left hand side", and "operator" and a "right hand side". If you're having
issues with this or have a use case that does not seem to be supported, please [Contact us](https://app.trychameleon.com/help). 

- Start an `if` block, use `{{if <CONDITION>}}`
- To end and `if` block use `{{/if}}`
- To add extra cases, use `{{elseif <CONDITION>}}`

Supported _condition_ operators:

| Operator                  | Description                                                                                              |
|---------------------------|----------------------------------------------------------------------------------------------------------|
| `==`                      | Equality: the values should be the same                                                                  |
| `!=`                      | Inequality: the values should **not** be the same                                                        |
| `>`, `>=`                 | Greater than + Greater than or equal: The left side should be greater than the right                     |
| `<`, `<=`                 | Less than + Less than or equal: The left side should be less than the right                              |
| `&&`                      | AND conjunction: The left side AND right side need to be true for the expression to be true              |
| <code>&#124;&#124;</code> | OR conjunction: The left side OR right side need to be true for the expression to be true                |
| `( )`                     | Grouping: use parenthesis to group expressions to capture complex cases.                                 |
| `matches`                 | Check if the left hand side                                                                              |
| `includes`                | Check if an array on the left hand side contains the value from the right hand side (same as `contains`) |
| `contains`                | Check if an array on the left hand side contains the value from the right hand side (same as `includes`) |

##### Basic examples

```handlebars
# check for "truthy", "falsey", "equality", "inequality"
{{if plan.name}}You have a plan{{/if}}
{{if !plan.name}}You have no plan{{/if}}
{{if plan.name == 'gold'}}You have a Gold plan{{/if}}
{{if plan.name != 'gold'}}You do not have a Gold plan{{/if}}

# check the comparison of the left hand to the right hand side
{{if plan.spend > 500}}You spend more than 500{{/if}}
{{if plan.spend < 500}}You spend less than 500{{/if}}
{{if plan.spend <= 500}}You spend less than or equal to 500{{/if}}
{{if plan.spend >= 500}}You spend more than or equal to 500{{/if}}

# Check if an array contains an item
{{if plan.features includes "unlimited_widgets"}}You have Unlimited widgets{{/if}}
You have {{if plan.features includes "unlimited_widgets"}}Unlimited{{else}}limited{{/if}} widgets.

# does the left hand "Regex match" the right hand
{{if plan matches "helium|neon|argon"}}You have a Noble gas plan{{/if}}
{{if plan matches "gold|silver|copper"}}You have a Transition metal plan{{/if}}

# Use && for AND, || for OR to create complex conditions
{{if plan.spend <= 500 || plan.spend >= 1000}}You do not spend 501-999{{/if}}

# group conditions to evaluate them in complicated ways
{{if credits.remaining < 10 || (plan.spend < 500 && plan.upgrade_spend == plan.spend)}}
  You should probably contact us for more credits
{{/if}}

{{if plan}}You have a plan{{/if}}


```
##### An `if` block with a `else` block

> The data says spend is 734 and it's been 13 weeks (so the content in the "if block" will be used).

```handlebars
{{if plan.spend > 500 && {time_ago started_on in="weeks"} > 12}}
  To get the most out of account, [book a review]({{account_info.csm_calendly}}) with your Account manager, {{account_info.csm_name}}.
{{else}}
  Check out these [additional resources](https://help.your-product.co/getting-started)
{{/if}}

# To get the most out of account, [book a review](https://calendly.com/acme-aria-j/30-min) with your Account manager, Aria Jones.
```

When the condition does not match, the content in the `else` case is used.

> The data says spend is 734

```handlebars
{{if plan.spend > 1000}}
To get the most out of account, [book a review]({{account_info.csm_calendly}}) with your Account manager, {{account_info.csm_name}}.
{{else}}
Check out these [additional resources](https://help.your-product.co/getting-started)
{{/if}}

# Check out these [additional resources](https://help.your-product.co/getting-started)
```

An `elseif` can be used to capture a cascading set of conditions

```handlebars
{{if !plan.spend}}
Start your free trial to use your widgets.
{{elsif plan.spend < 2050}}
Use the pre-built widget templates to work faster.
{{elsif plan.spend < 500}}
Start using your widget upgrades to widget
{{elsif plan.spend < 250}}
Upgrade to get more widgets.
{{else}}
Request a member of the Acme team to widgetize some stuff for you.
{{/if}}
```

##### To use an embedded Helper within the `if` condition, use _single curly braces_

This example assumes you have a `currentUser` variable attached to `window`
`window.currentUser = { id: '54s1', roles: { name: 'superadmin', items: ['invite_user', 'invite_admin'] } }`;

```handlebars
{{if {global 'currentUser.roles.level'} == 'admin'}}
As an admin, you're in charge of your team's permissions
{{elsif {global 'currentUser.roles.level'} == 'superadmin'}}
As the owner of your account, you're in charge of your team's admins
{{/if}}
```

```handlebars
{{if {global 'currentUser.roles.level'} includes 'invite_user'}}
Invite your teammates on the [Team page](/settings/team).
{{elsif {global 'currentUser.roles.level'} includes 'invite_admin'}}
As the owner of your account, you're in charge of your [Team's admins](/settings/admins).
{{/if}}
```

## Segmentation filter conditions | `filter` helper :id=examples-filter

Sometimes you need to do something especially complicated that can't be captured with `==` or `&&`; enter the `filter` helper.
You can use any of the [Segmentation filter expressions](concepts/filters.md) and many of the simple
conditions on user properties can be handled with `filter`.


```handlebars
{{if plan.spend > 500}}Your monthly bill is greater than 500{{/if}}

# as a filter
{{if {filter prop='plan' op='gt' value='500'}}}Your monthly bill is greater than 500{{/if}}

```


## Custom helpers :id=custom-helpers

- Your developers can define the implementation for a custom helper to fit you merge tag needs. A merge tag helper is simply a function that takes arguments (args) and options (opts) and outputs a string.
- A merge tag follows the typical "mustache syntax" like the other examples above `{{helper_name ["arg1", "arg2", ...] [option1="value1" option2="value2"]}}`
- To define a new merge tag pass the name and callback function to `chmln.lib.personalize.Mustache.addHelper`
- Please [Contact us](https://app.trychameleon.com/help) if you need any help or inspiration

This is a fully working example 🎉

```javascript
chmln.on('after:account', () => {
  chmln.lib.personalize.Mustache.addHelper('hello', (args, opts) => {
    // [1] args=['Alice'] opts={}
    // [2] args=['Alice'] opts={ prefix: '👋' }
    // [3] args=['foo'] opts={ prefix: '👋' }
    // [3] args=['Product manager'] opts={ postfix: '!!' }

    const name = args[0];

    return `${opts.prefix || 'Hey'} ${name}${opts.postfix || ''}`;
  });
});
```

Now, to use the merge tag (based on the [example data ↑](concepts/personalizing.md?id=example-user-data))

```text

{{hello first_name}} # [1]
# Hey Alice

{{hello first_name prefix="👋"}} # [2]
# 👋 Alice

{{hello 'foo' prefix="👋"}} # [3]
# 👋 foo   *Caution: using a quoted argument means a literal string is passed*

{{hello role postfix="!!"}} # [4]
# Hey Product manager!!

{{hello 'role' postfix="!!"}}
# Hey role!!   *Caution: using a quoted argument means a literal string is passed*
```
