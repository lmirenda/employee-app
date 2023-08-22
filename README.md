# Employee Management App

This is a Django web application that allows for easy management of employees, related
events and holidays.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-django-app.git
   
2. Access your project folder
   ``` bash
   cd your-django-app

3. Install dependencies using pipenv
    ```bash
   pipenv install
   ```
   
4. Activate the virtual environment
    ```bash
    pipenv shell
   
5. Run the migrations
    ```bash
    python manage.py migrate
   
6. Create a superuser
    ```bash
    python manage.py createsuperuser
   
7. Run the server
    ```bash
    python manage.py runserver
   
8. To register CRON jobs:
This will add all existing CRONJOBS in the core.settings file. 
    ```bash
    python manage.py crontab add


## Usage

1. Access the admin panel at `/admin` and login with your superuser credentials. 
2. Create all necessary employees.
3. All endpoints are protected by basic authentication.

## Endpoints

### Employees
Allowing for CRUD operations on employees.

`GET` `/api/employees/` - List all employees

`POST` `/api/employees/` - Create a new employee

`GET` `/api/employees/<int:pk>/` - Retrieve an employee by id

`PUT` `/api/employees/<int:pk>/` - Update an employee by id

`DELETE` `/api/employees/<int:pk>/` - Delete an employee by id

Employee request body schema:
```json
{
    "name": "string",
    "email": "string",
    "birth_date": "date YYYY-MM-DD",
    "enrollment_date": "date YYYY-MM-DD"
}
```

### Events
Allows to retrieve all employee related events, such as birthdays, work anniversaries and holidays.

It will retrieve all events for the specific time frame
#### Employee specific events
`GET` `/api/birthday/` 

`GET` `/api/anniversary/`

Params:
- `start_day` - Start date to look for events. Defaults to today.
- `day` - Days in the future to look for events. Defaults to 0.

#### Holidays
Accepts no query parameters. It will retrieve any holidays that are happening today, tomorrow or the next day.
`GET` `/api/holiday/`


## Cron jobs
The application has one cron job that is executed every morning at 8:30am. 

It will send an email with the employees that have a birthday or work anniversary on that day.