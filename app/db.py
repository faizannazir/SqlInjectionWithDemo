import sqlite3

# Connect to the database
conn = sqlite3.connect('users.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE users
                 (name TEXT, email TEXT, password TEXT, id INTEGER Primarykey,
                 phone_number TEXT, address TEXT)''')

# Insert some data into the table
cursor.execute("INSERT INTO users VALUES ('John Doe', 'jdoe@example.com', 'password123', 1, '555-555-5555', '123 Main St')")
cursor.execute("INSERT INTO users VALUES ('Jane Smith', 'jsmith@example.com', 'password456', 2, '555-555-5555', '456 Elm St')")
cursor.execute("INSERT INTO users VALUES ('John Cena', 'john@example.com', 'password45633', 3, '555-555-5555', '456 Elm St')")
cursor.execute("INSERT INTO users VALUES ('James smith', 'jsmith123@example.com', 'password41123', 4, '555-555-5555', '456 Elm St')")

# Commit the changes
conn.commit()

# Close the connection
conn.close()
