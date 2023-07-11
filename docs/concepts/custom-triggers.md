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

The step will display if the user is using the Chrome browser.

```
const { userAgent, vendor } = navigator;
/chrome/i.test(userAgent) && /google inc/i.test(vendor);
```

The step will display if MacOS is being used:

```
/Mac/.test(navigator.platform);
```

Using data from user profile.

```
chmln.data.profile.get('plan') === 'premium' && chmln.data.profile.get('country') === 'US';
```

The following conditional statement could be used to perform certain actions based on a checkbox's checked state and the user's plan.

```
const checkbox = document.getElementById('unsubscribe-checkbox');
checkbox.checked && user.plan === 'trial';
```

This code creates a promise that asynchronously checks for the existence of an element in the DOM and resolves or rejects based on whether the element is found within a specified timeout period. This approach can be useful when dealing with asynchronous rendering or delayed content loading. It allows you to perform actions or handle the element once it becomes available.

```
new Promise((resolve, reject) => {
  const interval = setInterval(() => {
    const el = document.querySelector('#my_element');
    if (el) {
      clearInterval(interval);
      resolve('Element found');
    }
  }, 100); // Check every 100 milliseconds

  setTimeout(() => {
    clearInterval(interval);
    reject('Timeout: Element not found');
  }, 5000);
});
```

In this scenario, the promise is used in combination with a click listener on the confirm button. It allows you to control the execution flow and handle asynchronous tasks based on user interactions.

```
new Promise((resolve, reject) => {
  const confirmButton = document.getElementById('my-button');

  confirmButton.addEventListener('click', () => {
    resolve('Button clicked');
  });
});
```
