# Employee Management REST API

A REST API for managing Departments, Designations, and Employees, built with **Django**, **Django REST Framework (DRF)**, and **SQLite**.

## Features

- Full CRUD for Departments, Designations, and Employees
- Pagination (default page size: 10, configurable via `?page_size=`)
- Search employees by first name, last name, or email
- Filter employees by department, designation, and active status
- Order employees by first name, salary, joining date, or created date
- Nested read-only department/designation details on employee responses, with plain ID-based writes
- Field validation: unique email, non-negative salary, phone number format, department/designation existence
- Django Admin panel for all three models
- Graceful handling of protected deletes (can't delete a department/designation still assigned to employees)

## Tech Stack

- Python
- Django
- Django REST Framework
- django-filter
- SQLite

## Project Structure

```
employee_management/
├── manage.py
├── db.sqlite3
├── employee_management/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── employees/
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    ├── filters.py
    ├── pagination.py
    ├── admin.py
    └── tests.py
```

## Setup

```bash
# Clone/create the project folder, then:
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

pip install django djangorestframework django-filter

python manage.py migrate
python manage.py createsuperuser   # optional, for admin panel access
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/api/`.
The admin panel will be available at `http://127.0.0.1:8000/admin/`.

## Models

### Department
| Field | Type | Notes |
|---|---|---|
| id | integer | auto |
| name | string | unique |
| description | string | optional |
| created_at | datetime | auto |
| updated_at | datetime | auto |

### Designation
| Field | Type | Notes |
|---|---|---|
| id | integer | auto |
| title | string | unique |
| description | string | optional |
| created_at | datetime | auto |
| updated_at | datetime | auto |

### Employee
| Field | Type | Notes |
|---|---|---|
| id | integer | auto |
| first_name | string | |
| last_name | string | |
| email | string | unique |
| phone | string | validated format |
| address | string | optional |
| date_of_birth | date | |
| gender | string | one of `M`, `F`, `O` |
| salary | decimal | must be ≥ 0 |
| joining_date | date | |
| department | FK → Department | must exist |
| designation | FK → Designation | must exist |
| is_active | boolean | default `true` |
| created_at | datetime | auto |
| updated_at | datetime | auto |

## API Endpoints

### Departments
| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/departments/` | List departments (paginated) |
| POST | `/api/departments/` | Create a department |
| GET | `/api/departments/{id}/` | Retrieve a department |
| PUT | `/api/departments/{id}/` | Update a department |
| DELETE | `/api/departments/{id}/` | Delete a department |

### Designations
| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/designations/` | List designations (paginated) |
| POST | `/api/designations/` | Create a designation |
| GET | `/api/designations/{id}/` | Retrieve a designation |
| PUT | `/api/designations/{id}/` | Update a designation |
| DELETE | `/api/designations/{id}/` | Delete a designation |

### Employees
| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/employees/` | List employees (paginated, filterable, searchable, orderable) |
| POST | `/api/employees/` | Create an employee |
| GET | `/api/employees/{id}/` | Retrieve an employee |
| PUT | `/api/employees/{id}/` | Update an employee |
| DELETE | `/api/employees/{id}/` | Delete an employee |

## Query Parameters (Employees list)

| Param | Example | Description |
|---|---|---|
| `page` | `?page=2` | Page number |
| `page_size` | `?page_size=20` | Items per page (max 100) |
| `search` | `?search=john` | Matches first_name, last_name, or email |
| `department` | `?department=1` | Filter by department ID |
| `designation` | `?designation=2` | Filter by designation ID |
| `is_active` | `?is_active=true` | Filter by active status |
| `ordering` | `?ordering=-salary` | Sort by first_name, salary, joining_date, or created_at (prefix `-` for descending) |

These can be combined, e.g.:
```
GET /api/employees/?department=1&is_active=true&ordering=-salary&page=1
```

## Sample Request — Create Employee

```json
POST /api/employees/
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "phone": "+919876543210",
  "address": "123 Main St, Bangalore",
  "date_of_birth": "1990-05-15",
  "gender": "M",
  "salary": "55000.00",
  "joining_date": "2024-01-10",
  "department": 1,
  "designation": 1,
  "is_active": true
}
```

Response (`201 Created`) includes nested `department_detail` and `designation_detail` objects alongside the raw `department`/`designation` IDs.

## Validation Rules

- Email must be unique across employees.
- Salary must not be negative.
- Phone must match `+999999999` style format (9–15 digits, optional leading `+` and `1`).
- Department and Designation must reference existing records.
- Deleting a Department or Designation that still has employees assigned returns a `400` with a clear error message instead of a server error.

## Testing

A Postman collection (`Employee_Management_API.postman_collection.json`) is included with pre-built requests for every endpoint, including search/filter/ordering/pagination examples and a validation-error example. Import it into Postman and set the `base_url` collection variable to match your running server (default: `http://127.0.0.1:8000/api`).

You can also use the DRF browsable API by visiting any endpoint directly in a browser, e.g. `http://127.0.0.1:8000/api/employees/`.

## Admin Panel

All three models are registered in Django Admin with search and filter support:

- **Departments** — searchable by name, filterable by creation date
- **Designations** — searchable by title, filterable by creation date
- **Employees** — searchable by first name/last name/email, filterable by department, designation, active status, and gender
