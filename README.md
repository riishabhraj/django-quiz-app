# Django Quiz App
A simple and interactive Django-based quiz application where users can take quizzes and view the results

## Features
User-friendly interface for taking quizzes
Multiple-choice question support

## Prerequisites
Before running this app, make sure you have the following installed on your local machine:

Python (3.1+)
Django (3.0+)
SQLite (default database)

## Installation

### 1. Clone the repository
```
git clone https://github.com/riishabhraj/django-quiz-app.git
```

### 2. Navigate to the project directory
```
cd django-quiz-app
```

### 3. Create a virtual environment (Optional but recommended)
``` 
python -m venv venv
```

### Activate the virtual environment:

On Windows:
```
venv\Scripts\activate
```

On macOS/Linux:
```
source venv/bin/activate
```

### 4. Install the required dependencies
```
pip install -r requirements.txt
```

### 5. Apply database migrations
``` 
python manage.py migrate
```

### 6. Create a superuser (for accessing the admin panel)
```
python manage.py createsuperuser
```

### 7. Run the development server
```
python manage.py runserver
```

Your application will be accessible at http://127.0.0.1:8000/.
