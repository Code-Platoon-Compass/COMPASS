# About the Instructor Endpoints

The reference is to help instructors who are editing course material using the endpoints. Every instructor gets an API key to use endpoints that require authentication.

## Seeding Database

1. Run migrations from the web server container (Django) to PostgreSQL container
2. Go to the seed_db folder in the PostgreSQL container
3. Either run seed.sh or run `psql -U $POSTGRES_USER -d $POSTGRES_DB -a -f init_instructors.sql`

## Instructor

| Method | Endpoint | Authentication | Description |
|---|---|---|---|
| `POST` | `/instructors` | API Key | Create a new instructor account (requires master instructor API key) |

Sample JSON body for POST:
```
{
    "name": "instructor_name",
    "email": "instructor_email"
}
```

## Cohorts

| Method | Endpoint | Authentication | Description |
|---|---|---|---|
| `POST` | `/cohorts` | API Key | Create a new cohort |
| `GET` | `/cohorts/:cohort-id/invite` | None | Retrieve the cohort invite code |

For the JSON body, all lists should stay as lists, even if there is only one element in the list.

### Sample JSON body for POST

```
Just a cohort, no links or emails
{
    "name": "sample_cohort"
}

Cohort with one daily link and one email
{
    "name": "sample_cohort",
    "daily_links": 
    [
        {
            "url": "http://hello.com",
            "label": "hello"
        }
    ],
    "email": ["test@example.com"]
}

Cohort with only links
{
    "name": "sample_cohort",
    "daily_links": 
    [
        {
            "url": "http://hello.com",
            "label": "hello"
        }
    ],
    "resource_links": 
    [
        {
            "url": "http://hello.com",
            "label": "hello"
        }
    ]
}

Sample JSON body adding all elements
{
    "name": "sample_cohort",
    "resource_links": 
    [
        {
            "url": "http://hello.com",
            "label": "hello"
        }, 
        {
            "url": "http://cool.com",
            "label": "cool"
        }
    ],
    "daily_links": 
    [
        {
            "url": "http://hello.com",
            "label": "hello"
        }, 
        {
            "url": "http://cool.com",
            "label": "cool"
        }
    ],
    "email": ["test@example.com", "test2@example.com", "test3@example.com"]
}
```

## Valid Emails

| Method | Endpoint | Authentication | Description |
|---|---|---|---|
| `GET` | `/cohorts/:cohort-id/emails` | API Key | List approved student emails |
| `POST` | `/cohorts/:cohort-id/emails` | API Key | Add an approved email |
| `PUT` | `/cohorts/:cohort-id/emails/:id` | API Key | Update an approved email |
| `DELETE` | `/cohorts/:cohort-id/emails/:id` | API Key | Remove an approved email |

For the JSON body, all lists should stay as lists, even for one element.

### Sample JSON body for POST or PUT

```
One email:
{
    "email": ["test@example.com"]
}

Many emails:
{
    "email": ["test@example.com", "test2@example.com", "test3@example.com"]
}
```

## Daily Links

| Method | Endpoint | Authentication | Description |
|---|---|---|---|
| `GET` | `/cohorts/:cohort-id/daily-links/` | None | List daily links for a cohort |
| `POST` | `/cohorts/:cohort-id/daily-links/` | API Key | Add a list of daily links. Duplicate links are not added. |
| `PUT` | `/cohorts/:cohort-id/daily-links/:id` | API Key | Update a daily link |
| `DELETE` | `/cohorts/:cohort-id/daily-links/:id` | API Key | Remove a daily link |

### Sample JSON body for POST or PUT

```
For one daily link:
{
    "daily_links": 
    [
        {
            "url": "http://hello.com",
            "label": "hello"
        }
    ]
}

For many daily links:
{
    "daily_links": 
    [
        {
            "url": "http://hello.com",
            "label": "hello"
        }, 
        {
            "url": "http://cool.com",
            "label": "cool"
        },
        {
            "url": "https://great.com",
            "label": "great"
        }
    ]
}
```

## Resource Links

| Method | Endpoint | Autentication | Description |
|---|---|---|---|
| `GET` | `/cohorts/:cohort-id/resource-links/` | None | List resource links for a cohort |
| `POST` | `/cohorts/:cohort-id/resource-links/` | API Key | Add a list of resource links. Duplicate links are not added. |
| `PUT` | `/cohorts/:cohort-id/resource-links/:id` | API Key | Update a resource link |
| `DELETE` | `/cohorts/:cohort-id/resource-links/:id` | API Key | Remove a resource link |

### Sample JSON body for POST or PUT

```
For one resource link:
{
    "resource_links": 
    [
        {
            "url": "http://hello.com",
            "label": "hello"
        }
    ]
}

For many resource links:
{
    "resource_links": 
    [
        {
            "url": "http://hello.com",
            "label": "hello"
        }, 
        {
            "url": "http://cool.com",
            "label": "cool"
        },
        {
            "url": "https://great.com",
            "label": "great"
        }
    ]
}
```