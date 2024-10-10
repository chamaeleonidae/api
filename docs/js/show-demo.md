# Show a Product Demo via JS API

**Typically based on a user action (such as "Show me", "Learn more"), start the Demo via JS API.**

---


## Show the Demo

Call `chmln.show`  with the Chameleon ID of the Demo (part of the Demo URL, or copyable from the dashboard slideout)


```
chmln.show('DEMO ID', { kind: 'demo' });
```