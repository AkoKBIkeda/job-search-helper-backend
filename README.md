# Job Search Helper (Backend)

## Overview

This MVP was created to join Chingu Voyage!  
It helps users keep track of job they are interested in.  
The backend provides APIs for basic operations for company as per the Chingu Solo Project requirements and includes user authentication.

## Features

- User Authentication: Sign up, login, and logout
- Token Authorization for API calls
- CRUD operations for Company

## How to Run This Project

**Live version:** [Job Search Helper](https://job-search-helper-fndk.onrender.com/)  
_\*It is deployed on Render's free tier, so it may take a few minutes to get it back online!_  
_Since it requires credentials, I would recommend using Postman to test it._

**Run locally:**  
After clone my project from this repo, move to the project directory  
Create a virtual environment  
`python -m venv .venv`  
Activate it (e.g., on Windows)  
`.venv\Scripts\activate`  
Install dependencies  
`pip install -r requirements.txt`  
Create .env file in the project directory and add following  
`DJANGO_SECRET_KEY="secret_key"` (<-- Enter your secret key here)  
`DEBUG=True`  
(Without setting the database, it will use SQLite locally)  
Run migrations  
`python manage.py migrate`  
Start the dev server  
`python manage.py runserver`

## Dependencies

Django==5.2.5  
djangorestframework==3.16.1  
dj-database-url==3.0.1  
django-cors-headers==4.7.0  
packaging==25.0  
python-decouple==3.8  
sqlparse==0.5.3  
asgiref==3.9.1  
tzdata==2025.2  
gunicorn==23.0.0 (For deployment on Render)  
psycopg2-binary==2.9.10 (For deployment on Render)  
whitenoise==6.9.0 (For deployment on Render)

## Future Work

- Add password reset/email verification
- Improve error response and messages
- Add more functions e.g., sum up raing and return list descending order.  
  etc., etc., etc..

If you have any ideas for additional functionality, please feel free to reach out!
