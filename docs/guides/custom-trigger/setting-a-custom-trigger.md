# Setting a custom trigger on a Step

When using the 'custom trigger' option for on-page triggers, you have the ability to input JavaScript code that can either return a truthy/falsy value or a promise. When a truthy value is returned, the Step will be triggered.

If the code you provide is synchronous (makes no API requests), the final resulting line will be evaluated. However, if the code is asynchronous, the returned promise will be internally evaluated, and the resulting truthy/falsy value will be extracted from the resolved promise.
