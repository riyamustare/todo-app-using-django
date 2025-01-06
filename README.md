A user-friendly Todo app built with Django and PostgreSQL, featuring Google OAuth and Django's built-in authentication system.

https://github.com/user-attachments/assets/4551fd4a-2773-46c3-b609-ee14ca862636

## Features

- **User Authentication**
  - Google OAuth login and registration.
  - Django built-in authentication for secure login and logout using password.

- **Task Management**
  - Add tasks with a due date.
  - Automatically repeat tasks daily if marked.
  - Complete or delete tasks.
  - Separate views for today's tasks and scheduled tasks.

- **Frontend**
  - Clean and intuitive user interface.

---

## Installation

### Prerequisites
- Python (>= 3.8)
- PostgreSQL
- pip (Python package manager)
- Google OAuth credentials (Client ID and Secret)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/riyamustare/todo-app-using-django.git
   cd todo-app
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up PostgreSQL Database**

   - Create a PostgreSQL database:
     ```sql
     CREATE DATABASE todo_app;
     ```
   - Update the `DATABASES` configuration in `settings.py`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'your_db_name',
             'USER': 'your_db_user',
             'PASSWORD': 'your_db_password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

4. **Set Up Google OAuth**

   - Obtain Google OAuth credentials from the [Google Cloud Console](https://console.cloud.google.com/).
   - Add the credentials to `settings.py`:
     ```python
     SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'your-client-id'
     SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'your-client-secret'
     ```

5. **Run Migrations**

   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

6. **Run the Development Server**

   ```bash
   python3 manage.py runserver
   ```

7. **Access the App**

   Open your browser and go to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Usage

1. **Register/Login**
   - Register a new account or log in using Google OAuth.

2. **Manage Tasks**
   - Add tasks with a title and due date.
   - Mark tasks as complete.
   - Delete tasks when no longer needed.

3. **Automatic Task Creation**
   - Enable the daily repeat option to recreate tasks automatically for the next day.

---

## Future Enhancements

- Add notifications for due tasks.
- Maintain a history of completed tasks and provide users with insights into their productivity trends.
