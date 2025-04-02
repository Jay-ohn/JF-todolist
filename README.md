# JF-TodoList

## Project Overview

T'is a simple web application built with Flask that allows users to manage their tasks efficiently. It includes features such as user authentication (signup, login, logout), a dashboard to view tasks, and a responsive design styled with Bootstrap. The app is designed to demonstrate the integration of Flask with MySQL.

---

## Features

- User authentication (Signup, Login, Logout)
- Secure password storage using hashing
- Responsive design with Bootstrap
- AJAX-based form submission validated using request.form for better user experience
- MySQL database integration with stored procedures

---

## Installation and Setup

### Prerequisites

- Python 3.7 or higher
- MySQL Server
- A virtual environment (optional but recommended)

### Steps to Set Up the Project

1. **Clone the Repository**
    ```bash
    git clone https://github.com/your-repo/jf-todolist.git
    cd jf-todolist
    ```

2. **Set Up a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**
    Install the required Python packages using `pip`:
    ```bash
    pip install -r requirements.txt
    ```
    The `requirements.txt` file should include:
    - Flask
    - Flask-MySQLdb
    - Werkzeug

4. **Set Up the Database**
    - Open the `mySQLdbsetup.sql` file and execute the SQL commands in your MySQL client to create the database and tables:
      ```sql
      CREATE DATABASE IF NOT EXISTS JF_todolist_app;
      USE JF_todolist_app;
      ```
    - This script also creates a stored procedure `sp_createUser` for user registration.

5. **Configure the Application**
    - Update the MySQL credentials in `app.py`:
      ```python
      app.config['MYSQL_HOST'] = 'localhost'
      app.config['MYSQL_USER'] = 'your_mysql_user'
      app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
      app.config['MYSQL_DB'] = 'jf_todolist_app'
      ```

6. **Run the Application**
    Start the Flask development server:
    ```bash
    python app.py
    ```
    The app will be available at `http://127.0.0.1:5000`.

---

## Code Walkthrough

### 1. **Flask Application Setup**
    - The `app.py` file initializes the Flask app and configures MySQL integration using `Flask-MySQLdb`.
    - Routes are defined for user authentication (`/signup`, `/login`, `/logout`), the dashboard (`/dashboard`), and the home page (`/`).

### 2. **Database Integration**
    - The MySQL database is used to store user credentials securely.
    - A stored procedure `sp_createUser` ensures that usernames are unique and handles user registration.

### 3. **Secure Password Handling**
    - Passwords are hashed using `generate_password_hash` from `Werkzeug` before storing them in the database.
    - During login, `check_password_hash` is used to verify the password.

### 4. **Frontend with Bootstrap**
    - All HTML templates (`index.html`, `login.html`, `signup.html`, `dashboard.html`) are styled using Bootstrap for a responsive and modern UI.
    - Navigation bars, forms, and buttons are built with Bootstrap components.

### 5. **AJAX for Signup**
    - The `ajax.js` file handles the signup form submission using the Fetch API.
    - It sends form data validated using request.form to the server asynchronously and displays success or error messages dynamically.

### 6. **Dynamic Content with Jinja2**
    - Jinja2 templates are used to render dynamic content, such as error messages and user-specific data.
    - Flash messages are displayed for feedback on user actions.

---

## Folder Structure

```
JF-TodoList/
├── app.py                 # Main Flask application
├── templates/             # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
├── static/                # Static files (JS only)
│   ├── main.js
│   ├── ajax.js
├── mySQLdbsetup.sql       # SQL script for database setup
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## Future Enhancements

- Add task management features (CRUD operations for tasks).
- Implement user-specific task filtering and sorting.

---

## Notes

- Ensure MySQL is running before launching the app. you can setup a local server for this using Xampp.
- If you encounter database issues, verify the mySQLdbsetup.sql script was executed properly.

## License

This project is for educational purposes. Feel free to modify and expand it!

## Author

John FA - 2025
