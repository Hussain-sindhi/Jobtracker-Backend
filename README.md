# Jobtracker Backend

Backend for **Jobtracker**, a job application tracker. Users sign up, log in with JWT, and manage their own job applications through a REST API. The project also includes simple server-rendered pages for adding, editing and deleting applications.

## Features

- User signup and JWT-based login (access and refresh tokens)
- Full CRUD API for job applications: company, role, status, applied date and notes
- Each user can only see and change their own applications through the API
- Django admin panel for managing data
- Server-rendered pages for a quick HTML view of applications (`/`, `/add/`)
- CORS support so a separate frontend can call the API

## Tech Stack

- **Language:** Python
- **Framework:** Django, Django REST Framework
- **Authentication:** JWT (`djangorestframework-simplejwt`)
- **Database:** SQLite
- **Other:** `django-cors-headers`

## Project Structure

```
Jobtracker-Backend/
├── jobtracker/          # Project settings and root URL configuration
├── tracker/             # Main app
│   ├── models.py        # Application model
│   ├── serializers.py   # ApplicationSerializer, RegisterSerializer
│   ├── views.py         # HTML views and DRF API views
│   ├── forms.py         # ModelForm for the HTML pages
│   ├── admin.py         # Admin registration
│   └── templates/       # home.html, add.html
├── manage.py
└── requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.10 or newer
- pip

### Setup

```bash
git clone https://github.com/Hussain-sindhi/Jobtracker-Backend.git
cd Jobtracker-Backend

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # optional, for the admin panel
python manage.py runserver
```

The server runs at `http://127.0.0.1:8000/`.

## API Endpoints

| Method | Endpoint | Auth | Description |
| ------ | -------- | ---- | ----------- |
| POST | `/api/signup/` | No | Register a new user (`username`, `email`, `password`) |
| POST | `/api/token/` | No | Log in and get access and refresh tokens |
| GET | `/api/applications/` | Yes | List your applications |
| POST | `/api/applications/` | Yes | Create an application |
| GET | `/api/applications/<id>/` | Yes | Get one application |
| PUT | `/api/applications/<id>/` | Yes | Update an application |
| DELETE | `/api/applications/<id>/` | Yes | Delete an application |

Send the token with each protected request:

```
Authorization: Bearer <access_token>
```

### Example

```bash
# Sign up
curl -X POST http://127.0.0.1:8000/api/signup/ \
  -H "Content-Type: application/json" \
  -d '{"username": "demo", "email": "demo@example.com", "password": "demo12345"}'

# Log in
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "demo", "password": "demo12345"}'

# Create an application
curl -X POST http://127.0.0.1:8000/api/applications/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{"company_name": "Acme", "role": "Backend Developer", "status": "Applied", "applied_date": "2026-11-20", "notes": "Referred by a friend"}'
```

## Data Model

**Application**

| Field | Type |
| ----- | ---- |
| user | ForeignKey to Django `User` (set automatically from the logged-in user) |
| company_name | CharField (max 100) |
| role | CharField (max 100) |
| status | CharField (max 50) |
| applied_date | DateField |
| notes | TextField |

## Future Improvements

- Add automated tests
- Restrict `status` to fixed choices (Applied, Interview, Offer, Rejected)
- Return proper 404 and 400 status codes from the API
- Protect the HTML pages with login and per-user data
- Move secrets to environment variables and use PostgreSQL for production

## Author

**Mohammad Hussain Sindhi**
[GitHub](https://github.com/Hussain-sindhi) | [LinkedIn](https://www.linkedin.com/in/mohammad-hussain-sindhi-007b4b255/)
