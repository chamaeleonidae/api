# Overview

**Chameleon's REST API allows you to interact with information in Chameleon to integrate it with your own systems. It's meant to be flexible and adapt to your own use cases.**

------


Currently, our REST API supports the following endpoints:

| Model + details                                              | List URL                 | Show URL                     |
| ------------------------------------------------------------ | ------------------------ | ---------------------------- |
| [User Profiles](apis/profiles.md) | `GET /v3/analyze/profiles`| `GET v3/analyze/profiles/:id` |
| [Companies](apis/companies.md) | `GET /v3/analyze/companies`| `GET v3/analyze/companies/:id` |
| [Segments](apis/segments.md) | `GET /v3/edit/segments`  | `GET /v3/edit/segments/:id`  |
| [Tours](apis/tours.md)    | `GET /v3/edit/tours`     | `GET /v3/edit/tours/:id`     |
| [Tour Interactions](apis/tour-interactions.md) | `GET /v3/analyze/interactions` | `GET /v3/analyze/interactions/:id` |
| [Microsurveys](apis/surveys.md) | `GET /v3/edit/surveys`   | `GET /v3/edit/surveys/:id`   |
| [Microsurvey Responses](apis/survey-responses.md) | `GET /v3/analyze/responses`   | -   |
| [Experience Deliveries](apis/deliveries.md) | `GET /v3/edit/deliveries`   | `GET /v3/edit/delivery/:id`   |
| [BETA - Rate Limit Groups](apis/limit-groups.md) | `GET /v3/edit/limit_groups`| `GET v3/edit/limit_groups/:id` |
| [Launchers](apis/launchers.md) | `GET /v3/edit/launchers` | `GET /v3/edit/launchers/:id` |
| [Tooltips](apis/tooltips.md) | `GET /v3/edit/tooltips`  | `GET /v3/edit/tooltips/:id`  |
| [Webhooks](apis/webhooks.md) | `GET /v3/edit/webhooks`| `GET v3/edit/webhooks/:id` |
| [Domains](apis/urls.md)   | `GET /v3/edit/urls`      | `GET /v3/edit/urls/:id`      |
| [Tags](apis/tags.md) | `GET /v3/edit/tags`| `GET v3/edit/tags/:id` |
| [Data Properties](apis/properties.md)   | `GET /v3/edit/properties`      | `GET /v3/edit/properties/:id`      |



## Ideas for how you can use this API

Chameleon's REST API is made to be adaptable to your own custom use cases. Nevertheless, there are some cases where you might want to use it:

- Register a **[Webhook](apis/webhooks.md)** to receive realtime notifications of **[Microsurvey Responses](apis/survey-responses.md)**.
- Use the **[Microsurveys Endpoint](apis/surveys.md)** to download **[Microsurvey Response](apis/survey-responses.md)** data periodically.
- Get a list of all the User data being sent to Chameleon and manipulate it (delete, update, etc.) through the **[User Profiles Endpoint](apis/profiles.md)**.
- Use the **[Tours Endpoint](apis/tours.md)** to have an alert when an experience isn't completed in a specific amount of time.
- Monitor the Experiences assigned to your **[BETA - Rate Limit Groups](apis/limit-groups.md)**.


> If there is any use case where you'd like to use our API but you're not sure how, feel free to [Contact us](https://app.trychameleon.com/help).
