# Overview

**Chameleon's REST API allows you to interact with information in Chameleon to integrate it with your own systems. It's meant to be flexible and adapt to your own use cases.**

------



Currently, it supports the following endpoints:

| Model + details                                              | List URL                 | Show URL                     |
| ------------------------------------------------------------ | ------------------------ | ---------------------------- |
| [Segments](https://developers.trychameleon.com/#/apis/segments) | `GET /v3/edit/segments`  | `GET /v3/edit/segments/:id`  |
| [Tours](https://developers.trychameleon.com/#/apis/tours)    | `GET /v3/edit/tours`     | `GET /v3/edit/tours/:id`     |
| [Microsurveys](https://developers.trychameleon.com/#/apis/surveys) | `GET /v3/edit/surveys`   | `GET /v3/edit/surveys/:id`   |
| [Launchers](https://developers.trychameleon.com/#/apis/launchers) | `GET /v3/edit/launchers` | `GET /v3/edit/launchers/:id` |
| [Tooltips](https://developers.trychameleon.com/#/apis/tooltips) | `GET /v3/edit/tooltips`  | `GET /v3/edit/tooltips/:id`  |
| [Domains](https://developers.trychameleon.com/#/apis/urls)   | `GET /v3/edit/urls`      | `GET /v3/edit/urls/:id`      |



## Ideas for how you can use this API

Chameleon's REST API is made to be adaptable to your own custom use cases. Nevertheless, there are some cases where you might want to use it:

- Use the **[Microsurveys Endpoint](https://developers.trychameleon.com/#/apis/surveys)** to download microsurvey response data periodically.
- Get a list of all the user data being sent to Chameleon and manipulate it (delete, update, etc.) through the **[User Profiles Endpoint](https://developers.trychameleon.com/#/apis/profiles)**.
- Use the **[Tours Endpoint](https://developers.trychameleon.com/#/apis/tours)** to have an alert when an experience isn't completed in a specific amount of time.


> If there is any use case where you'd like to use our API but you're not sure how, feel free to [reach us](mailto:hello@trychameleon.com?subject=API+Use+Case).
