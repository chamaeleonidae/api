# Show a Launcher via JS API

**Show a particular Launcher using the JS API. Optionally open or close the Launcher.**

*To learn more about the Chameleon Launchers product, please read [this article](https://help.trychameleon.com/launchers).*

---



## Force a Launcher to show

Call `chmln.show`  with the Chameleon ID of the Launcher, and the Launcher will show (if possible) immediately. If the Launcher is anchored to an element on the page, that element is required to be present before the Launcher can show. If the Launcher is already showing, nothing will happen.
 

```
chmln.show('ID');
```

---

#### Finding the Launcher ID

![img](https://downloads.intercomcdn.com/i/o/103548306/46627b719bdb62ec08c64d63/Screen+Shot+2019-02-13+at+21.31.55.png)

To find the `ID`  of a Launcher, use the Browser Console. Right click the Launcher in question in the Sidebar and then click 'Inspect element'. 

Hover over the `<li id="chmln-list-XXXXXXXX"`  row which corresponds to the Launcher above and then use the `XXXXXXXXX`  as the `ID` .

---

With the Chameleon sidebar showing, run:

```
chmln.data.lists.each((l) => console.log(Object.values(l.pick(['id', 'name'])).join(':')))
```


You'll see a list of `ID:name` pairs.

```
5c2fe686593b2f00049fa27c:my launcher
5c4a12725296f800040b3607:launcher 2
5c4a30f2a16aef00047540f6:launcher 3
```


Find the line with the correct name, and copy the `ID`  (the part preceding the colon), and use it in your call to `chmln.show` . For example, to show 'my launcher', call:
 

```
chmln.show('5c2fe686593b2f00049fa27c');
```


Alternatively, from your list of Launchers in the Chameleon sidebar, you can use the browser dev tools to inspect the Launcher, look for the element with an `id`  like `chmln-list-ID` , and copy the `ID`  part. 



#### Optional Arguments 

`chmln.show`  can accept a second argument which is an object containing optional parameters. For example:

```
chmln.show('5c2fe686593b2f00049fa27c', { open: true });
```

This call would show the Launcher 'my Launcher' (if it isn't already shown), and then open the Launcher such that the list of Tours is visible. You can use this to open a Launcher that is already showing.

The list of allowed optional parameters is as follows:

- `open: true|false` - If `true` , opens the Launcher if it isn't already open.
- `close: true|false`  - If `true` , closes the Launcher if it isn't already closed. 
