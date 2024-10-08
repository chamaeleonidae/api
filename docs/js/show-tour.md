# Show a Tour via JS API

**Use this JS API method to show a Tour using custom criteria**

*To learn more about the Chameleon Tours product, please visit [this section](https://help.chameleon.io/en/collections/74747-tours) in our Help Center.*

---


## Force a Tour to show

Call `chmln.show`  with the Chameleon ID of the Tour and the Tour will redirect to the right page (if necessary) and start the Tour from the beginning.

```
chmln.show('TOUR ID');
```


## Triggers, Elements and Delays

By default, any click/hover/delay triggers are ignored in order for the Tour to show right away when calling `chmln.show`. This default can be changed with the `deepLinked`  option listed below.



## Options and changes to the default behavior

With options this API can be called with a second argument.


#### Examples :id=examples

Show **now** for users in the segment who have noe seen this Tour before

```javascript
chmln.show('TOUR ID', { use_segmentation: true, once: true });
```

Allow this Tour to be **triggered** normally (assuming this Tour is triggered when the user clicks on a specific element etc.)

```javascript
chmln.show('TOUR ID', { skip_triggers: false });
```

#### Options :id=options

| Option       | default              | Example value | description                                                  |
| -------------- | ------------------- | ------------- | ------------------------------------------------------------ |
| `use_segmentation` | `false` | `true`, `false` | Whether or not to first apply the Audience (Segmentation) to determine if the Tour show display to the user. | 
| `once`             | `false` | `true`, `false` | Whether or not to check if the user has seen this Tour before, `false` means for the Tour to display. |
| `redirect`         | `true`  | `true`, `false` | Whether or not to redirect to the "page the Tour starts on". This redirect loads the "Tour link" that can be copied from "Additional sharing options". |
| `skip_triggers`    | `true`  | `true`, `false` | Whether or not to bypass the triggers, elements and delays on the first step to "force" it to show right away. |
| `skip_url_match`   | `true`  | `true`, `false` | Whether or not to bypass the first step URL match to "force" it to show right away. |

