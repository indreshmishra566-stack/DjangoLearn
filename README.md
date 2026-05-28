# Django Learn

A self-hosted Django handbook for learning Django from zero to production concepts.

The site includes theory, history, code examples, command references, admin-managed content, copyable snippets, and local progress tracking. It is designed for learners who want one place to understand how Django works from the request/response cycle all the way to deployment.

## What Visitors Can Learn

- Django history, philosophy, and MVT architecture
- Setup, project structure, settings, apps, and URL routing
- Models, migrations, QuerySets, ORM patterns, and database relationships
- Views, templates, forms, admin, authentication, sessions, and messages
- Static files, media files, security, testing, caching, performance, and deployment
- Django REST Framework basics, async Django, internationalization, and project architecture
- Custom user models, permissions, file uploads, email, pagination, search, and filtering
- Custom management commands, transactions, advanced admin, advanced class-based views, and advanced DRF
- WebSockets with Channels, Celery background tasks, Docker, CI/CD, logging, PostgreSQL, multiple databases, and Django internals

## Quick Start

```bash
git clone https://github.com/indreshmishra566-stack/DjangoLearn.git
cd django-learn
chmod +x setup.sh && ./setup.sh
source venv/bin/activate
python manage.py runserver
```

Open http://localhost:8000

## Deploy to Render

This project includes `build.sh` for Render deployment.

1. Push the latest code to GitHub.
2. Go to Render and create a new **Web Service** from the GitHub repository.
3. Use these commands:

```text
Build Command: pip install -r requirements.txt && ./build.sh
Start Command: gunicorn django_learn.wsgi:application
```

4. Add these environment variables:

```text
DJANGO_DEBUG=0
DJANGO_SECRET_KEY=replace-with-a-long-random-secret
DJANGO_ALLOWED_HOSTS=.onrender.com,your-custom-domain.com
```

5. Deploy.

The build step runs:

```bash
python3 manage.py collectstatic --noinput
python3 manage.py migrate --noinput
```

This creates the static files and the SQLite database with seeded learning content during deployment. For a larger production app, use Render PostgreSQL instead of SQLite.

## Structure

```
django-learn-site/
├── django_learn/       # Project settings, urls, wsgi
├── learn/              # Main app
│   ├── models.py       # Chapter, Section, Command
│   ├── views.py        # index + chapter views
│   ├── urls.py
│   ├── admin.py
│   ├── templates/learn/
│   │   ├── base.html
│   │   └── chapter.html
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   └── 0002_seed_data.py   ← all chapters pre-loaded
│   └── fixtures/
│       └── chapters.json
├── static/
│   ├── css/style.css
│   └── js/main.js
├── requirements.txt
├── manage.py
└── setup.sh
```

## Current Curriculum

1. What is Django?
2. Django History & Philosophy
3. Setup & Installation
4. Request & Response Cycle
5. Settings & Config
6. Project Architecture
7. URL Routing
8. Views
9. Class-Based Views Deep Dive
10. Templates
11. Models & Database
12. Advanced QuerySets
13. Migrations Deep Dive
14. Forms
15. Django Admin
16. Advanced Admin
17. Authentication
18. Custom User Model
19. Permissions & Authorization
20. Sessions & Messages
21. Static & Media Files
22. File Uploads & Storage
23. Email & Password Reset
24. Pagination, Search & Filtering
25. Middleware
26. Signals
27. Custom Management Commands
28. Transactions & Database Integrity
29. Testing Django Apps
30. Security Checklist
31. Django REST Framework
32. Advanced DRF
33. Performance & Caching
34. Async Django
35. Internationalization
36. Deployment & Production
37. Docker for Django
38. CI/CD with GitHub Actions
39. Logging & Monitoring
40. PostgreSQL Features
41. Multiple Databases
42. Celery & Background Tasks
43. WebSockets with Channels
44. Django Internals

## Adding Content

Use the admin panel at  `/admin/` — to create a superuser :

```bash
python manage.py createsuperuser
```

## Data Models

- **Chapter** — `order`, `slug`, `icon`, `title`, `color`
- **Section** — belongs to Chapter; type = `theory` | `code` | `commands`
- **Command** — belongs to a `commands`-type Section; `cmd` + `description`
