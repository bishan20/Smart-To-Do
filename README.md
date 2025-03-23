# Smart To-Do List Web Application

## Project Name
Smart To-Do 

## Description
The Smart To-Do List web application helps users efficiently manage their tasks by providing an intuitive interface for adding, editing, and deleting tasks. It integrates user authentication, enabling personalized task management for each user. The app allows users to categorize their tasks, set priorities, and view their tasks in a list format.

## Purpose
The main purpose of the Smart To-Do List is to help individuals organize their tasks and stay on top of their daily responsibilities. The application provides a clean, user-friendly interface for managing tasks, making it easy for users to add, modify, and delete tasks, as well as track their progress.

## Value
This app brings value by simplifying task management and helping users prioritize their work. It allows users to:
- Create personalized task lists
- Edit and delete tasks as needed
- Stay organized by categorizing tasks
- Use authentication for secure, personalized task management

## Technologies Used
- **Django**: Web framework for backend development.
- **HTML**: For structuring web pages.
- **CSS**: For styling and creating responsive layouts.
- **JavaScript**: For any dynamic functionality.
- **SQLite** (or other databases): For storing user data and tasks.
- **Bootstrap** (optional): For a responsive and clean user interface.

## Features
- User registration and login
- Task management (create, edit, delete tasks)
- Task categorization (optional)
- User-specific task list (authenticated users)
- Secure login/logout functionality

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/bishan20/Smart-To-Do.git
    cd Smart-To-Do
    ```

2. **Install dependencies**:

    Ensure you have `Django` installed. If not, you can install it using:

    ```bash
    pip install django
    ```

3. **Run the server**:

    ```bash
    python manage.py runserver
    ```

4. **Access the app**:

    Open a web browser and go to `http://127.0.0.1:8000` to use the app.

## How to Use

1. **User Registration**: 
    - Navigate to the registration page to create an account.
    - Provide a username, email, and password to sign up.

2. **Login**: 
    - After registration, you can log in with your username and password.

3. **Task Management**: 
    - After logging in, you will be redirected to your task list page.
    - You can add, edit, and delete tasks from the list.
    - Tasks are displayed in a simple list format, with options to modify or remove them.

## Future Enhancements
- Add task prioritization (e.g., high, medium, low).
- Allow users to set due dates and reminders for tasks.
- Implement additional features like notifications and recurring tasks.
- Support for task categories or labels.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Django for providing the powerful framework.
- Bootstrap for the clean and responsive UI.
- Thanks to all the contributors who helped make this project possible.

