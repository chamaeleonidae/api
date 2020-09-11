# Show a Tour via JS API

**Use this JS API method to show a Tour using custom criteria**



*For an overview of how the Chameleon API works, please first read* [*this article*](https://help.trychameleon.com/developer-docs/api-basics)*.*

------



## Force a tour to show

Call `chmln.show`  with the Chameleon ID of the Tour and the Tour will redirect to the right page (if necessary) and start the tour from the beginning.

```
chmln.show('Chameleon Tour ID');
```



#### Finding the Chameleon Tour ID

You can obtain the `Chameleon Tour ID` from the sidebar, inspect the "row of the tour", find the element with "chmln-campaign-ID" and copy the ID part as shown below. 

![img](https://downloads.intercomcdn.com/i/o/38502020/bacc2946cba493efdcbbc072/Find+tour+ID.gif)

As per the above gif, to trigger this tour you would call: `chmln.show('56998ae30036f20003000001');`



## Triggers, Elements and Delays

By default, any click/hover/delay triggers are ignored in order for the tour to show right away when calling `chmln.show`. This default can be changed with the `deepLinked`  option listed below.



## Options and changes to the default behavior

With options this API can be called with a second argument. For example: `chmln.show('ID', { option: 'value'})`

- `use_segmentation: {false,true}` - whether or not to first apply segmentation to determine if the tour show display to the user [default `false`  means disregard audience set on the tour]
- `once: {false,true}`  - whether or not to check if the user has seen this tour before [default `false`  means show the tour even if they have seen it before]
- `redirect: {true,false}` - whether or not to redirect to the "page the tour starts on". Internally we redirect/load the same "link" that can be copied from "Additional sharing options".
- `deepLinked: {true,false}` - whether or not to bypass the triggers, elements and delays on the step to "force" it to show right away. When `deepLinked: false` is specified, the tour will (for example) wait for the specified element to be clicked or will wait for the specified element to be one the page before showing the tour.