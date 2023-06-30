# Custom Triggers

**Custom trigger allows users to create highly customizable and responsive experiences within the system. Using custom logic or leveraging promises to perform complex operations and dynamically control the visibility of experiences based on real-time data, user interactions, or external events.**

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

The request fails, the step won't be displayed.

```
fetch('https://jsonplaceholder.typicode.com/todos/x')
```

The step will be displayed accordingly if the condition is true

```
const input = document.getElementById('user-age');
const age = parseInt(input.value) || 0;
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
