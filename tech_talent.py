import sqlite3

connection = sqlite3.connect('tech_talent.db')
cursor = connection.cursor()

# Drop tables if they exist
cursor.execute("DROP TABLE IF EXISTS companies;")
cursor.execute("DROP TABLE IF EXISTS candidates;")

# Code from previous weeks code along
cursor.execute('''CREATE TABLE companies (
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name STRING,
    industry STRING,
    location STRING
    );
''')

cursor.execute('''CREATE TABLE candidates (
    candidate_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name STRING,
    last_name STRING,
    email STRING,
    years_experience INTEGER,
    primary_skill STRING
    );
''')

cursor.execute('''INSERT INTO companies (company_name, industry, location) VALUES
    ('TechCorp', 'Software', 'San Francisco'),
    ('DataDynamics', 'Data Analytics', 'Boston'),
    ('CloudNine', 'Cloud Computing', 'Seattle');
''')

cursor.execute('''INSERT INTO candidates (first_name, last_name, email, years_experience, primary_skill) VALUES
    ('John', 'Smith', 'john.smith@email.com', 5, 'Python'),
    ('Sarah', 'Johnson', 'sarah.j@email.com', 3, 'Data Science'),
    ('Michael', 'Lee', 'michael.lee@email.com', 7, 'Cloud Architecture'),
    ('Emma', 'Wilson', 'emma.w@email.com', 2, 'Frontend Development'),
    ('James', 'Brown', 'james.b@email.com', 4, 'Python');
''')
# End of code from previous weeks code along

# Start your code here


















# DON'T EDIT BELOW THIS LINE. Commit and close the connection
connection.commit()
connection.close()