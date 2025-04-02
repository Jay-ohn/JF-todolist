# JF To-Do List App

## Features

- User authentication (Signup, Login, Logout)
- Secure password storage using hashing
- Responsive design with Bootstrap
- AJAX-based form submission validated using request.form for better user experience
- MySQL database integration with stored procedures

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
SEN_311/
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

## Author

John Friday-Akwawei

## Student ID

30005191
