# JF ToDoList App

Project Overview

JF ToDoList App is a simple Flask-based web application that allows users to sign up and manage their tasks efficiently. The project demonstrates key web development concepts including form validation, AJAX-based form submission, MySQL database integration, password hashing, and stored procedures.

Features

User signup with password hashing

AJAX-powered form submission without page reload

MySQL database integration using Flask-MySQL

Server-side form validation with request.form

Stored procedure for secure user registration

Installation & Setup

Prerequisites

Ensure you have the following installed:

Python 3.x

MySQL Server

Flask & required dependencies

Step 1: Clone the Repository

 git clone https://github.com/your-repo/jf-todolist.git
 cd jf-todolist

Step 2: Install Required Python Packages

Create a virtual environment (optional but recommended) and install dependencies:

 python -m venv venv
 source venv/bin/activate  # On Windows use `venv\Scripts\activate`
 pip install -r requirements.txt

Step 3: Set Up the Database

Start MySQL and create the database by running:

 mysql -u root -p < create_table.sql

Update database credentials in app.py if needed.

Step 4: Run the Flask App

 python app.py

Go to http://localhost:5000/ to access the app.

File Structure

JF-ToDoList-App/
│── app.py              # Flask backend
│── create_table.sql    # Database schema setup
│── templates/
│   │── index.html      # Homepage
│   │── signup.html     # Signup page
│── static/
│   │── css/
│   │   │── style.css   # General styles
│   │   │── signup.css  # Signup page styles
│   │── js/
│   │   │── signup.js   # AJAX handling
│── README.md           # Project documentation

Notes

Ensure MySQL is running before launching the app.

Use Developer Tools (F12) to debug AJAX requests if needed.

If you encounter database issues, verify the create_table.sql script was executed properly.

License

This project is for educational purposes. Feel free to modify and expand it!

Author

Your Name - 2025

