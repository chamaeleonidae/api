# Chameleon Developer Hub

#### Welcome!

You can use this documentation alongside our [Product Documentation](https://help.trychameleon.com/) to do more with Chameleon.


**Our Chameleon API is subdivided essentially in three main portions:** a client-side [JavaScript API](/js/overview.md), a [REST API](/apis/overview.md) and [Webhooks](/webhooks/overview.md). With these, you can achieve more with our product and create custom integrations to fit your use cases.

#### You can interact with our API to:

- **Send data to Chameleon**: This can include letting Chameleon know when a user completes an action, or when their profile changes (e.g. they become paid.) You can remove/delete user data, opt a user out of Chameleon Experiences, and send variables for users to use within the copy of any Experience (e.g. user first names).
- **Get data from Chameleon**: You can download data from Chameleon (e.g. responses to Microsurveys) periodically or forward Chameleon-tracked events (e.g. Tour completed) in real-time to your database, data warehouse, or other tools. You can also do things like download list of all users, segments, Experiences etc. or get all the stats on a particular Experience.
- **Manage Experiences**: You can use the Chameleon API to show a Tour or Launcher, or approve many domains within your product to show Chameleon Experiences.

-------

#### By design:

- The API is straightforward, flexible, and designed with RESTful intentions.
- It is consistent in its application of parameters/options and paginates with cursors.
- Attributes may be added from time to time, please ignore anything you don't need.
- Use the appropriate `expand` parameters to limit data when the full dataset is not required.



> If you have any questions/comments/feature requests they can be submitted via the "Useful links" Launcher in the bottom-right.
