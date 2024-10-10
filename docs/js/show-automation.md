# Start an Automation via JS API

**Typically based on a user action (such as "Show me", "Do it"), start an Automation to do it for them via JS API.**

*To learn more about the Chameleon Automations product, please read [this article](https://help.chameleon.io/en/articles/9556244-understanding-automations).*

---



## Start an Automation

Call `chmln.show`  with the Chameleon ID of the Automation (part of the Automation URL, or copyable from the dashboard slideout)
 

```
chmln.show('AUTOMATION ID', { kind: 'automation' });
```

