
# 📋 Smart To-Do List Web App

---

## 📖 Description, Purpose, and Value

The **Smart To-Do List** is a Django-powered web application that helps users efficiently manage their daily tasks.  
Key features include:

- User registration, login, and logout system.
- Add, edit, delete, and view tasks.
- Sort tasks by due date, priority, or creation time.
- View today's tasks and upcoming tasks easily.
- Email reminders for tasks due soon.
- Light and dark mode toggle for better user experience.
- Profile settings to update name, username and email securely.
- Clean, responsive UI using Bootstrap.

> **Purpose:**  
To provide a personal task management solution that is simple, intuitive, and accessible.

> **Value:**  
Boosts productivity by organizing tasks, offering reminders, and ensuring users never miss important deadlines.

---

## 💻 Technologies Used

- **Python 3.12**
- **Django 5.1.6**
- **SQLite3** (default Django database)
- **Bootstrap 5** (for frontend design)
- **HTML/CSS/JavaScript**
- **Gmail SMTP** (for sending task reminder emails)

---

## 🛠️ Setup Instructions

Follow these steps to clone and run the project locally:

1. **Install Python**

   Make sure Python 3.x is installed on your machine.  
   [Download Python](https://www.python.org/downloads/)

2. **Clone the Repository**

   ```bash
   git clone https://github.com/bishan20/Smart-To-Do.git
   cd Smart-To-Do/src
   ```

3. **Create a Virtual Environment (Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate    # On Mac/Linux
   venv\Scripts\activate     # On Windows
   ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up the Database**

   Run migrations to create necessary tables:

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser (Optional)**

   If you want to access Django Admin:

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

8. **Open the App**

   Open your browser and visit:

   ```
   http://127.0.0.1:8000/register
   ```

9. **Set Up Email for Task Reminders (Optional)**

   To enable email task reminders:

   - In `settings.py`, configure your Gmail SMTP settings:

     ```python
     EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
     EMAIL_HOST = 'smtp.gmail.com'
     EMAIL_PORT = 587
     EMAIL_USE_TLS = True
     EMAIL_HOST_USER = 'your-email@gmail.com'
     EMAIL_HOST_PASSWORD = 'your-app-password'
     DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
     ```

   > 💡 Tip: If you have 2FA enabled, generate an [App Password](https://support.google.com/accounts/answer/185833) from Google.

10. **Testing Email Reminders**

    - After running the server, create a new task **due tomorrow**.
    - Then run the custom management command manually:

      ```bash
      python manage.py send_task_reminders
      ```

    - If everything is set up correctly, an email reminder will be sent to your registered email address.

---

## 🎬 YouTube Video Link

👉 [Watch the demo video here]https://www.youtube.com/watch?v=1RSsYasEaW8

---

## ✅ Project Runs Successfully

- Clone the repository ✅
- Follow README instructions ✅
- No issues launching or using the app ✅
- Tested user registration, login, task creation, filtering, and email reminders ✅
- Light and Dark mode working ✅

---

# 🚀 Notes

- The project is built using **Django's built-in authentication system**.
- User data is safely stored and email notifications are handled securely.
- The UI is responsive for desktop and mobile browsers.
- All templates are organized inside `tasks/templates/tasks/` and `tasks/templates/users/` folders.
- Static files (CSS/JS) are located inside `tasks/static/`.

---
