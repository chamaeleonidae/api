# Custom Triggers

**Custom triggers allow users to create highly customizable and responsive experiences by using custom logic or leveraging promises to perform complex operations and dynamically control the visibility of experiences based on real-time data, or user interactions.**

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
fetch('https://jsonplaceholder.typicode.com/todos/not-an-id')
```

The step will be displayed accordingly if the condition is true

```
const input = document.getElementById('user-age');
const age = parseInt(input.value) || 0;

age > 18
```

The step will be displayed once the promise is resolved, after 5 seconds

```
new Promise((resolve, reject) => {
  setTimeout(() => { resolve("Display"); }, 5000);
});
```

The step won't be displayed as the promise will be rejected, no matter the value.

```
new Promise((resolve, reject) => {
  setTimeout(() => { reject(true); }, 5000);
});
```

The step will display if the browser being used is Chrome

```
const { userAgent, vendor } = navigator;
/chrome/i.test(userAgent) && /google inc/i.test(vendor);
```

The step will display if macOS (Mac OS X) is being used:

```
/Mac/.test(navigator.platform);
```

Using data from user profile, the step will display if the user is in a premium plan and is located in the US:

```
chmln.data.profile.get('plan') === 'premium' && chmln.data.profile.get('country') === 'US';
```
