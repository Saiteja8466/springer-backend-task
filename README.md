# Employee Management API

A Django REST Framework based API for managing Employees, Departments, and Attendance.

---

## 📂 Project Structure

```

employee\_project/        # Main Django project
│
├── employee\_project/    # Project configuration folder
│   ├── **init**.py
│   ├── asgi.py
│   ├── settings.py      # Django settings
│   ├── urls.py          # Root URL routes
│   └── wsgi.py
│
├── employees/           # Employees app
│   ├── migrations/
│   ├── **init**.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py        # Employee and Department models
│   ├── serializers.py   # Serializers for API
│   ├── urls.py          # App specific routes
│   └── views.py         # API logic
│
├── attendance/          # Attendance app
│   ├── migrations/
│   ├── **init**.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py        # Attendance model
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── venv/                # Virtual environment
├── manage.py            # Django CLI entry point
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation

````

---

- Manage Employees and Departments  
- Track Attendance  
- RESTful API with Swagger UI Documentation  
- PostgreSQL database support  

---

## ⚙️ Installation

1. Clone the repository  
   ```bash
   git clone https://github.com/your-username/employee_project.git
   cd employee_project
````

2. Create virtual environment and install dependencies

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows

   pip install -r requirements.txt
   ```

3. Setup PostgreSQL database in `.env`

   ```env
   DEBUG=True
   SECRET_KEY=your-secret-key
   DATABASE_NAME=employee_db
   DATABASE_USER=postgres
   DATABASE_PASSWORD=postgres
   DATABASE_HOST=localhost
   DATABASE_PORT=5432
   ```

4. Run migrations

   ```bash
   python manage.py migrate
   ```

5. Create superuser

   ```bash
   python manage.py createsuperuser
   ```

6. Start server

   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

---

## 📖 API Documentation

Swagger UI available at:

```
http://127.0.0.1:8000/docs/
```

---

Cheppava? nenu ee structure directly nenu README.md lo add cheyadaniki ready ga format chesi isthana?
