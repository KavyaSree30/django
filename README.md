# Django Blog Project

This is a full-stack web application built using Django framework for managing a blog. It includes features such as user authentication, blog post management, comments, and search functionality.

## Features

- **User Authentication**: Secure login and registration system for users.
- **Blog Post Management**: CRUD operations (Create, Read, Update, Delete) for blog posts.
- **Comments**: Users can leave comments on blog posts.
- **Search**: Search functionality to find specific blog posts.

## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- Python 3.x
- Django framework (`pip install django`)
- Virtual environment (optional but recommended)

## Installation and Setup

1. **Clone the repository:**

   
   git clone https://github.com/KavyaSree30/django.git
   cd django

Set up virtual environment (optional):
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate

Install dependencies:


pip install -r requirements.txt

Apply migrations:


python manage.py migrate

Create a superuser:

python manage.py createsuperuser

Run the development server:


python manage.py runserver

Access the application:

Open your web browser and go to http://127.0.0.1:8000/ to view the blog application.
