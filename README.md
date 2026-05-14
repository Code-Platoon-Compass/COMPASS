# COMPASS
### Code Platoon Organized Materials: Personalized Access and Search System

<img width="512" alt="logo vertical" src="https://github.com/user-attachments/assets/2579ac58-b79a-461b-9b7a-875d38c49b1e" />

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Vite](https://img.shields.io/badge/vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
![Google Gemini](https://img.shields.io/badge/google%20gemini-8E75B2?style=for-the-badge&logo=google%20gemini&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)

## Video Demo
[<img width="512" alt="thumbnail" src="https://github.com/user-attachments/assets/92aaaab1-8a8b-4bbc-8df6-ab9578557757" />](https://example.com)

COMPASS is a personalized student resource dashboard built for Code Platoon. It centralizes every resource a student needs — daily links, curriculum materials, vocabulary help, timezone tools, and more — into a single, cohort-aware home base. No more digging through Google Drive, Slack channels, and a dozen bookmarks.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [API Reference](#api-reference)
- [Instructor Workflow](#instructor-workflow)
- [Student Workflow](#student-workflow)
- [Future Work](#future-work)
- [Team](#team)

---

## Features

**Student Dashboard**
- **Daily Links & Resources** — Instructors curate links per cohort; students see them front and center every day
- **Daily Check-In** — A quick form students complete each morning
- **Vocab Widget** — Students paste a link from their curriculum; the Gemini API reads the page and generates a list of vocabulary terms and definitions drawn directly from that content
- **Chicago Time Widget** — Always displays the current local time in Chicago, where Code Platoon is based, so remote students always know what time it is at HQ

**Instructor Controls**
- Create and manage cohorts
- Register valid student emails per cohort
- Generate invite codes for student self-registration
- Edit daily links and resource links for their cohort

**Authentication**
- Student login is handled via Google OAuth — users must have a Google account (any Google account, not necessarily Gmail)
- JWT-based auth via SimpleJWT
- Students register using a cohort invite code + a pre-approved email address; that email must be the same one they provided their instructor (used to link them to the cohort's Google Drive and Google Calendar) and must be associated with their Google account
- Instructors authenticate via a unique API key included with each request
- A master instructor account is created on first setup; that instructor can create additional instructor accounts

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React, Vite, Tailwind CSS |
| Backend | Django, Django REST Framework |
| Auth | SimpleJWT |
| Database | PostgreSQL |
| AI | Google Gemini API |
| Containerization | Docker, Docker Compose |
| Reverse Proxy | Nginx |

---

## Project Structure

```
COMPASS/
├── client/          # React frontend (Vite)
├── server/          # Django backend
├── db/              # Database init scripts
├── nginx/           # Nginx configuration
├── docker-compose.yml
├── example_env      # Template for required environment variables
└── requirements.txt
```

---

## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and Docker Compose installed
- A [Google Gemini API key](https://aistudio.google.com/app/apikey)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Code-Platoon-Compass/COMPASS.git
   cd COMPASS
   ```

2. **Create your environment files**

   In the project root:
   ```bash
   cp example_env .env
   ```

   Also create a `.env` file inside the `client/` directory:
   ```bash
   cp client/client_env_example client/.env
   ```

   Fill in the values in both files — see [Environment Variables](#environment-variables) below.

3. **Install the dependencies and build the frontend**

   In the client folder:
   ```bash
   cd client
   npm install
   npm run build
   ```

3. **Start the application**
   ```bash
   docker compose up --build
   ```

   This will spin up all services: the Django backend, PostgreSQL database, React frontend, and Nginx reverse proxy.

4. **Seeding Database**

   1. Go to the server container with the Django web server
   2. Run migrations
      ```bash
      python manage.py makemigrations cohort_app
      python manage.py migrate cohort_app
      python manage.py makemigrations auth_app
      python manage.py migrate auth_app
      python manage.py makemigrations instructor_app
      python manage.py migrate instructor_app
      python manage.py makemigrations vocab_app
      python manage.py migrate vocab_app
      ```
   4. Go to the database container
   5. Seed the database by runing the `./seed.sh` script
      ```bash
      cd seed_db
      ./seed.sh
      ```
   8. Copy the API key as this is used for instructor endpoints
      
5. **Access the app**

   Open your browser and navigate to `http://localhost`.

---

## Environment Variables

Copy `example_env` to `.env` and fill in the following:

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key — generate one at [djecrety.ir](https://djecrety.ir) or use `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| `DEBUG` | `True` for local development, `False` in production |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts (e.g. `localhost,127.0.0.1`) |
| `CORS_ALLOWED_ORIGINS` | Comma-separated list of allowed origins (e.g. `http://localhost:5173`) |
| `POSTGRES_DB` | Name for the PostgreSQL database |
| `POSTGRES_USER` | PostgreSQL username |
| `POSTGRES_PASSWORD` | PostgreSQL password |
| `DB_HOST` | Database host (use `db` when running via Docker Compose) |
| `GOOGLE_CLIENT_ID` | Google OAuth client ID — get it from the [Google Cloud Console](https://console.cloud.google.com/) |
| `GOOGLE_CLIENT_SECRET` | Google OAuth client secret — same Google Cloud Console project |
| `GEMINI_API_KEY` | Google Gemini API key — get it from [Google AI Studio](https://aistudio.google.com/app/apikey) |

> **Note:** `POSTGRES_DB`, `POSTGRES_USER`, and `POSTGRES_PASSWORD` are your choice for local development. Set `DB_HOST=db` when running with Docker Compose.

The frontend also requires its own `.env` file inside the `client/` directory:

| Variable | Description |
|---|---|
| `VITE_GOOGLE_CLIENT_ID` | Same Google OAuth client ID as above — Vite requires this to be prefixed with `VITE_` to expose it to the browser |

---

## API Reference

All endpoints are prefixed with `/api/v1/`.

A list of endpoints with explanations and examples can be found in the [wiki](https://github.com/Code-Platoon-Compass/COMPASS/wiki/How-to-use-the-Web-Server-for-Instructors)

---

## Instructor Workflow

Instructor setup is done by directly hitting the API endpoints with JSON (e.g. via Postman or curl). There is no instructor-facing UI in v1. All instructor API requests must include the instructor's unique API key for authentication.

A master instructor account is created when the project is first set up. That account can then create additional instructor accounts.

1. **Create additional instructors** (optional) — `POST /api/v1/instructors` using the master instructor's API key
2. **Create a cohort** — `POST /api/v1/cohorts`
3. **Register student emails** — `POST /api/v1/cohorts/:cohort-id/emails` for each student
4. **Get the invite code** — `GET /api/v1/cohorts/:cohort-id/invite` and share it with students
5. **Manage links** — Add, edit, or remove daily links and resource links for the cohort at any time

---

## Student Workflow

1. Receive an invite code from your instructor
2. Navigate to the registration page, enter your invite code, and sign up using the same email address you provided your instructor
3. Log in — the dashboard loads with your cohort's links, widgets, and tools ready to go

---

## Future Work

The following features were scoped and designed but deferred to a future version:

- **Teacher accounts with full admin panel**

- **Calendar widget** — A today/this week view of cohort events pulled from Google Calendar via the Google Calendar API
- **Minesweeper, personal to-do, sticky notes, and other quality-of-life widgets**
- **Quiz widget** powered by LLM
- **Teams/cohort teams page**
- **Custom drag-and-drop widget grid**
- **EC2 deployment with SSL** — Architecture is ready; deployment runbook is documented internally

---

## Team

| Name | GitHub |
|---|---|
| Kami | [@Kamivision](https://github.com/Kamivision) |
| Ericka | [@2017eerickson](https://github.com/2017eerickson) |
| Tiffany | [@wang2929](https://github.com/wang2929) |
| Elia | [@maffiemaffie](https://github.com/maffiemaffie) |
| Jakob | [@JakobPagel](https://github.com/JakobPagel) |
| Brandon | [@LVRG-creator](https://github.com/LVRG-creator) |

---

## Acknowledgements

- [Time.Now](https://time.now) — World Time API used to power the Chicago time widget. Free to use; please support them if you find this project useful.

---

**[COMPASS](https://github.com/Code-Platoon-Compass/COMPASS)** · Code Platoon Organized Materials: Personalized Access and Search System · *Built at [Code Platoon](https://www.codeplatoon.org)*


<img height="128" alt="compass lockup" src="https://github.com/user-attachments/assets/d93e446f-0592-4f0d-a7de-4032915313a3" />
