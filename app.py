from flask import Flask, render_template, request, jsonify, session, redirect, flash
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)

# Secret key for session management (used for securely signing session cookies)
app.secret_key = 'your_secret_key'

# Define the home route (renders the home page)
@app.route('/')
def home():
    return render_template('index.html')

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'jf_todolist_app'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Initialize MySQL connection
mysql = MySQL(app)

# Define the signup route (handles user registration)
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # Redirect logged-in users to the dashboard
    current_user_id = session.get('user_id')
    if current_user_id:
        return redirect('/dashboard')
    
    # Handle form submission and validation for user signup
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()

        if not username or not password:
            response = jsonify({'message': 'Username and password are required!'})
            response.status_code = 400
            return response
        
        # Hash the password for secure storage
        hashed_password = generate_password_hash(password)

        try:
            # Call stored procedure to create a new user
            cur = mysql.connection.cursor()
            cur.callproc('sp_createUser', [username, hashed_password])
            mysql.connection.commit()
            cur.close()
            response = jsonify({'message': 'User registered successfully! Login to your account.'})
            response.status_code = 200
            return response
        except Exception as e:
            # Handle database errors
            response = jsonify({'message': 'Error: {}'.format(str(e))})
            response.status_code = 500
            return response
        
     # Render the signup page   
    return render_template('signup.html')

# Define the login route (handles user authentication)
@app.route('/login', methods=['GET', 'POST'])
def login():
    
    # Redirect logged-in users to the dashboard
    current_user_id = session.get('user_id')
    if current_user_id:
        return redirect('/dashboard')
    
    # Handle form submission and validation for user login
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()

        if not username or not password:
            return render_template('login.html', error='Username and password are required!')

        try:
            # Query the database for the user
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM tbl_user WHERE username = %s", (username,))
            user = cur.fetchone()
            cur.close()

            # Verify the password and log the user in
            if user and check_password_hash(user['password'], password):
                session['user_id'] = user['id']  # Store user ID in session
                return redirect('/dashboard')
            else:
                # Invalid credentials
                return render_template('login.html', error='Invalid username or password!')
        except Exception as e:
            # Handle database errors
            return render_template('login.html', error='Error: {}'.format(str(e)))
    
    # Render the login page
    return render_template('login.html')

# Define the logout route (logs the user out)
@app.route('/logout')
def logout():
    # Remove user ID from the session
    session.pop('user_id')
    flash('You have been logged out.', 'info')
    return redirect('/login')

# Define the dashboard route (accessible only to logged-in users)
@app.route('/dashboard')
def dashboard():
    # Redirect unauthenticated users to the login page
    current_user_id = session.get('user_id')
    if not current_user_id:
        flash('Please log in first.', 'danger')
        return redirect('/login')

    # Render the dashboard page
    return render_template('dashboard.html')

# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)