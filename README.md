# Job Search Helper (Backend)
## Overview
This MVP was created to join Chingu Voyage!  
It helps users keep track of jobs they are interested in.  
The backend provides APIs for basic operations on the company entity as per the Chingu Solo Project requirements and includes user authentication.

## Features
- User Authentication: Sign up, log in, and log out
- Token Authorization for API calls
- CRUD operations for Companies

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
gunicorn==23.0.0 (for deployment on Render)  
psycopg2-binary==2.9.10 (for deployment on Render)  
whitenoise==6.9.0 (for deployment on Render)

## Possible Improvements
- Add password reset and email verification
- Improve error responses and messages
- Aggregate ratings and return the list in descending order

## Licence
This project is released under the MIT License. See the [LICENSE](./LICENSE) file for full details.
