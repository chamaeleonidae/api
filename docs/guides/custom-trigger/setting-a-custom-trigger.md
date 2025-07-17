# Setting a custom trigger on a Step

When using the 'custom trigger' option for on-page triggers, you have the ability to input JavaScript code that can either return a truthy/falsy value or a promise. When a truthy value is returned, the Step will be triggered.

If the code you provide is synchronous (makes no API requests), the final resulting line will be evaluated. However, if the code is asynchronous, the returned promise will be internally evaluated, and the resulting truthy/falsy value will be extracted from the resolved promise.

## Custom trigger examples - using synchronous code

```javascript
const input = document.getElementById('my-input');
const val = parseInt(input.value) || 0;
return val + 2 === 5;
```

## Custom trigger examples - using asynchronous code

When using asynchronous code, you only need to return the promise. The resolve value of that promise will be extracted internally to check if it's a truthy or falsy value. 
We don't offer support for `async`/`await` yet, so when getting a promise from an API you can just use `fetch`.

```javascript
const promise = fetch('https://jsonplaceholder.typicode.com/todos/1');
return promise;
```
