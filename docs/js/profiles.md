# Send user properties via JS API

**Create and update data attributes for users and companies**

---



Syncing user and company data to Chameleon account can be helpful for: 

- Targeting users with tours based on who they are.
- Personalizing content within tours (merge tags in content).
- Better URL matching (merge tags in URLs).



## Identifying user :id=profile

**Users need to be identified with a unique ID** (`UID`) to enable them to see tours. We also strongly recommend sending `email` to maintain a user's identity across Chameleon and any integrations you enable. 

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

A UID simply needs to be a unique string that identifies the current user, and it needs to be consistent. Unique meaning no user will share one with another user, and consistent meaning it won't change between servers, logins, or browsers. Consistent also means you'll always have access to this attribute to send to Chameleon.


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
