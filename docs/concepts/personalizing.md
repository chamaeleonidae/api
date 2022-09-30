# Personalizing

**Personalizing is the way to adjust Experience content to match the User who is viewing an Chameleon Experience.**

---

| Helper name                | -                                                              | description                                                                           |
|----------------------------|----------------------------------------------------------------|---------------------------------------------------------------------------------------|
| `property`                 | [examples ↓](concepts/personalizing.md?id=examples-property)   | The default used when a unquoted string is found at the beginning                     |
| `global`                   | [examples ↓](concepts/personalizing.md?id=examples-global)     | Pull a value from the window object, useful for extra-advanced conditional formatting |
| `pluralize`                | [examples ↓](concepts/personalizing.md?id=examples-plural)     | Given a specific number and a word produces a phrase with the correct tense           |
| `time_difference_in_words` | [examples ↓](concepts/personalizing.md?id=examples-time-diff)  | Given a specific date/time produces a time offset                                     |
| `time_local`               | [examples ↓](concepts/personalizing.md?id=examples-time-local) | Given a specific date/time uses toLocalString() to generate a human readable string   |
| `delivery`                 | [examples ↓](concepts/personalizing.md?id=examples-delivery)   | Personalize with content explicitly sent via a [Delivery](apis/deliveries.md)         |
| `html`                     | [examples ↓](concepts/personalizing.md?id=examples-html)       | Output html based on given options                                                    |



## Examples :id=examples

Current reference time is `2029-04-04T12:00:00Z`

##### Example user data

```json
{
  "first_name": "Alice",
  "role": "Product manager",
  "created": "2027-03-04T12:02:00Z",
  "time_z": "Europe/Brussels",
  "plan": {
    "name": "Growth",
    "spend": 734,
    "upgrade_on": "2029-04-08T13:31:00Z",
    "upgrade_spend": 893
  },
  "credits": {
    "used": 19,
    "remaining": 1
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
```


### Using nested data | `property` helper

```text
You're subscribed to the {{plan.name}} plan.
# You're subscribed to the Growth plan.
```

### Use a relative offset time | `time_difference_in_words` helper :id=examples-time-diff

```text
You signed up {{time_difference_in_words created}}.
# You signed up 2 years ago.

You signed up {{time_difference_in_words created tense="in yonder past"}}.
# You signed up 2 years in yonder past.

Thanks for being a customer for {{time_difference_in_words created tense=''}}!
# Thanks for being a customer for 2 years!
```

### Display a timestamp/date in a presentable format | `time_local` helper :id=examples-time-local

Internally this helper generates a `Date` object and then calls `toLocaleString`.

- The first argument is the locale of the identified user
  1. If you use [Translations](https://help.chameleon.io/en/articles/5868890) then it will be the same locale you've configured or falling back
  1. The browsers reported locale

- The second argument is any `options` that are passed to the `time_local` helper. The examples below are non-exhaustive and you can use any/all of the `options` found in the [`toLocaleString` reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleString) or [options reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#options)


> For the examples below, the user is in Pacific time

```text
{{time_local created}} # the default
# 3/4/2027, 4:02:00 AM

{{time_local created year="numeric" weekday="long" month="short" day="numeric"}} # nicer looking format
# Thursday, Mar 4, 2027

{{time_local created year="numeric" weekday="long" month="short" day="numeric" hour="numeric" minute="numeric"}} # nicer looking format with hours
# Thursday, Mar 4, 2027, 4:00 AM

{{time_local created timeZoneName="short"}} # for a user in Pacific time; show the timezone
# 3/4/2027, 4:02:00 AM PST

{{time_local created timeZone="UTC"}} # lock to UTC
# 3/4/2027, 12:02:00 PM

{{time_local created timeZone=time_z}} # for a who has a `time_z` property for Brussels (time_z without quotes since it's a user property)
# 3/4/2027, 1:02:00 PM

{{time_local created timeZone=time_z timeZoneName="short"}} # short Brussels
# 3/4/2027, 1:02:00 PM GMT+1

{{time_local created timeZone=time_z timeZoneName="long"}} # long Brussels
# 3/4/2027, 1:02:00 PM Central European Standard Time

```


### Pluralizing numbers | `pluralize` helper :id=examples-plural

The tense word can be singular **or** plural when it's passed in.

```text
You've used {{pluralize credits.used "credit"}} and have {{pluralize credits.remaining "credit"}} left.
# You've used 19 credits and have 1 credit left.

Your next bill is for ${{pluralize plan.spend "dollar"}}.
# Your next bill is for $734 dollars.

Your next bill is ${{pluralize plan.spend "dollars"}}.
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



#### Show a custom link | `html` helper :id=examples-

```text
{{html 'Read' tagName='a' href='/read-more' target='read-more-tab' data-read-more='link' style='color: red'}}
# <a href="/read-more" target="read-more-tab" data-read-more="link style="color: red">Read</a>
```

