from flask import Flask, request, redirect, render_template, session
import sqlite3
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if the email and password are valid using the SQLite database
        # Implement prevention against SQL injection here
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        # cur.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        cur.execute(f"SELECT * FROM users WHERE email='{email}' AND password='{password}'")
        user = cur.fetchone()
        con.close()

        if user is not None:
            # Set the user session and redirect to the dashboard
            print(user[3])
            session['user_id'] = user[3]
            return redirect('/dashboard')
        else:
            # Show an error message if the login credentials are invalid
            error = "Invalid login credentials. Please try again."
            return render_template('login.html', error=error)
    else:
        # Render the login page
        return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # Check if the user is authenticated by checking the session
    if 'user_id' in session:
        # Get the user information from the database
        con = sqlite3.connect('users.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE id=?", (session['user_id'],))
        user = cur.fetchone()
        con.close()

        # Render the dashboard page with the user information
        return render_template('dashboard.html', user=user)
    else:
        # Redirect to the login page if the user is not authenticated
        return redirect('/')

@app.route('/logout')
def logout():
    # Clear the user session and redirect to the login page
    session.pop('user_id', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)


# ' ''
# ' union select * from users--
# ' or 1=1--

# py sqlmap/sqlmap-dev/sqlmap.py -u http://127.0.0.1:5000/ --data "email=jdoe@example.com&password=password123" --dbs
# py sqlmap/sqlmap-dev/sqlmap.py -u http://127.0.0.1:5000/ --data "email=jdoe@example.com&password=password123" -D dbname --tables --dump