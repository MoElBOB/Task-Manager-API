# Task Manager API

A RESTful API built with Django REST Framework.

## Features
- JWT Authentication
- User Registration
- Tasks CRUD
- Categories
- User Profile
- Search
- Filtering
- Pagination
- Swagger API Documentation

## Technologies
- Python
- Django
- Django REST Framework
- Simple JWT
- Swagger (drf-yasg)

## API Endpoints

POST /api/register/  
POST /api/token/  

GET /api/tasks/  
POST /api/tasks/  

GET /api/categories/  
POST /api/categories/  

GET /api/profile/  
PUT /api/profile/

## Run Project

```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```