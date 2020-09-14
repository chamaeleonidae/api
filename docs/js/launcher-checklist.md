# Review a checklist status via JS API

**Query data for checklist within Launchers using the JS API**



*For an overview of how the Chameleon API works, please first read* [*this article*](https://help.trychameleon.com/developer-docs/api-basics).

*For an overview of how to find the ID of a particular Launcher, please first read* [*Show a Launcher*](http://help.trychameleon.com/developer-docs/manage-tours-and-launchers/show-a-launcher)*.*

------



With Chameleon loaded on the page, you can query for the completion status of the tours in a checklist:

```
chmln.models.List.find('ID').tourSummary();
```



For example, with a Launcher with ID `5c2fe686593b2f00049fa27c`  containing 3 tours, you'll call:

```
chmln.models.List.find('5c2fe686593b2f00049fa27c').tourSummary();
```


You'll receive an object that looks like the following:

```
{
  "completed_count": 1,
  "incomplete_count": 2,
  "tours": [
    {
      "id": "5b4631143704660004c1c83d",
      "name": "my tour",
      "published_at": "2019-01-14T19:35:50.268Z",
      "completed": true,
      "completed_at": "2019-01-22T11:28:42.268Z",
      "uid": "current-user-ID"
    },
    {
      "id": "5be0abebfc03a40004a61ec6",
      "name": "tour 2",
      "published_at": "2019-01-09T21:37:05.938Z",
      "completed": false
    },
    {
      "id": "5b84711f7218a30004dad255",
      "name": "Ben's tour 2018-08-27",
      "description": "This is my tour",
      "title": "My display title",
      "published_at": "2018-10-19T18:11:29.122Z",
      "completed": false
    },
  ]
}
```
