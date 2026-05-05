# Zindua School — Django Project

## Overview
A Django-based school website built with template inheritance, Django template tags and filters. Features four pages: Home, About, Contact, and Programmes.

---

## Requirements
- Python 3.x
- Django 4.x or higher

---

## Project Setup

### 1. Clone or create the project folder
```bash
mkdir zindua_school
cd zindua_school
```

### 2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/Scripts/activate       # Windows
source venv/bin/activate            # Mac/Linux
```

### 3. Install dependencies
```bash
pip install django
pip freeze > requirements.txt
```

### 4. Create Django project and app
```bash
django-admin startproject myproject .
python manage.py startapp zindua
```

---

## Project Structure

```
zindua_school/
    zindua/
        templates/
            base.html
            index.html
            about.html
            contact.html
            programmes.html
        __init__.py
        admin.py
        apps.py
        models.py
        urls.py
        views.py
    myproject/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
    venv/
    manage.py
    requirements.txt
```

---

## Configuration

### Register the app
In `myproject/settings.py` add `zindua` to `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'zindua',
]
```

### Connect URLs
In `myproject/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('zindua.urls')),
]
```

---

## Running the Project

### Apply migrations
```bash
python manage.py migrate
```

### Create a superuser
```bash
python manage.py createsuperuser
```

### Start the development server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## Pages

| Page | URL | Description |
|------|-----|-------------|
| Home | `/` | Landing page with school stats |
| About | `/about/` | Mission statement and team |
| Programmes | `/programmes/` | List of available courses |
| Contact | `/contact/` | Contact details and socials |
| Admin | `/admin/` | Django admin dashboard |

---

## Django Concepts Used

### Template Inheritance
All pages extend `base.html` which contains the navbar and footer. Child templates override the `content` block.

```html
<!-- base.html -->
{% block content %}{% endblock %}

<!-- child page -->
{% extends 'base.html' %}
{% block content %}
    Page content here
{% endblock %}
```

### Template Tags
Used for loops and conditionals across all pages.
```html
{% for programme in programmes %}
{% endfor %}

{% if user.is_authenticated %}
{% endif %}
```

### Template Filters
Used on the programmes page to count and pluralize results.
```html
{{ programmes|length }}
{{ programmes|length|pluralize }}
```

### Context Data
Data is passed from views to templates via a context dictionary.
```python
def index(request):
    context = {
        'school_name': 'Zindua School',
        'stats': [...]
    }
    return render(request, 'index.html', context)
```

---

## Admin Access
Log in at `http://127.0.0.1:8000/admin/` using the superuser credentials created during setup.

---

### Creator
Winstone Mwangi