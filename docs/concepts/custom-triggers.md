# Custom Triggers

**Custom Triggers introduces a powerful mechanism for triggering and displaying steps using short code snippets. By providing a function or a promise as the trigger, it can dynamically evaluate any desired logic or asynchronous operations to determine whether the step should be triggered and shown.**

---

Custom Triggers are available for Tours, Microsurveys and Tooltips as an on-page trigger in the Display Rules section.

#### Examples

The following request will resolve to a boolean, true in this case, the step will be displayed

```
fetch('https://jsonplaceholder.typicode.com/todos/1')
.then(data => data.json())
.then(data => data.id > 0);
```

The result is false, the step won't be displayed.

```
fetch('https://jsonplaceholder.typicode.com/todos/1')
.then(data => data.json())
.then(data => data.id === 0);
```

A non-empty response is considered a truthy value, the step will be displayed.

```
fetch('https://jsonplaceholder.typicode.com/todos/1')
```

The step will be displayed accordingly if the condition is true

```
const input = document.getElementByName('user-age');
const age = parseInt(input) || 0;
return age > 18;
```

The step will be displayed once the promise is resolved, after 5 seconds

```
const promise = new Promise(function(resolve, reject) {
  setTimeout(function(){ resolve("Display"); }, 5000);
});
promise
```

The step won't be displayed as the promise will be rejected, no matter the value.

```
const promise = new Promise(function(resolve, reject) {
  setTimeout(function(){ reject(true); }, 5000);
});
promise
```
