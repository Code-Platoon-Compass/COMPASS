# About the Endpoints

The bulk of endpoints are for instructors to edit the resources that are available for students. The document should help a new user find endpoints and ping them to update materials.

## Instructors

The instructors are the only ones authorized to access most POST, PUT, and DELETE endpoints, aside from student authentication and AI-generated vocabulary lists. At database setup, a main instructor is created by default with an API key. Using the API key, more instructors can be generated. Then instructors can add, edit, and remove resources for students.

### Create instructors

POST api/v1/instructor/create



POST api/v1/instructor/forgot

### Create Cohort

POST api/v1/cohorts

### Daily Links

GET api/v1/cohorts/:cohort-id/daily-links/
POST api/v1/cohorts/:cohort-id/daily-links/
PUT api/v1/cohorts/:cohort-id/daily-links/:id
DELETE api/v1/cohorts/:cohort-id/daily-links/:id

### Resource Links

GET api/v1/cohorts/:cohort-id/resource-links/
POST api/v1/cohorts/:cohort-id/resource-links/
PUT api/v1/cohorts/:cohort-id/resource-links/:id
DELETE api/v1/cohorts/:cohort-id/resource-links/:id

### Cohort Emails

GET api/v1/cohorts/:cohort-id/emails
POST api/v1/cohorts/:cohort-id/emails
PUT api/v1/cohorts/:cohort-id/emails/:id
DELETE api/v1/cohorts/:cohort-id/emails/:id

### Invite Link

GET api/v1/cohorts/:cohort-id/invite

## Student Authentication

POST api/v1/auth/create-student
POST api/v1/auth/login
POST api/v1/auth/logout

## Vocab

POST api/v1/vocab
