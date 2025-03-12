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
cursor.execute("DROP TABLE IF EXISTS jobs;")
cursor.execute("DROP TABLE IF EXISTS candidate_profiles;")
cursor.execute("DROP TABLE IF EXISTS candidates_jobs;")

# Create tables demonstrating different relationships
# One-to-One: Candidate and Profile
cursor.execute('''CREATE TABLE candidate_profiles (
    profile_id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_id INTEGER UNIQUE,
    resume_url STRING,
    linkedin_url STRING,
    location STRING,
    FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id)
    );
''')

cursor.execute('''INSERT INTO candidate_profiles (candidate_id, resume_url, linkedin_url, location) VALUES
    (3, 'resume.pdf', 'linkedin.com/michael', 'San Francisco'),
    (4, 'resume.docx', 'linkedin.com/emma', 'Chicago'),
    (5, 'resume.pdf', 'linkedin.com/james', 'New York'),
    (1, 'resume.pdf', 'linkedin.com/john', 'New York'),
    (2, 'resume.docx', 'linkedin.com/sarah', 'Boston');
''')

# Show that unique constraint is working by trying to add a duplicate. Comment this out when done
# cursor.execute('''INSERT INTO candidate_profiles (candidate_id, resume_url, linkedin_url, location) VALUES

# Use JOIN to get candidate profiles and their corresponding candidates
cursor.execute('''
    SELECT candidates.first_name, candidates.last_name, candidate_profiles.resume_url
    FROM candidates
    JOIN candidate_profiles ON candidates.candidate_id = candidate_profiles.candidate_id;
''')
# Print out the values
print("\nCandidates and their profiles:")
for row in cursor.fetchall():
    print(row)


# One-to-Many: Company and Jobs
cursor.execute('''
    CREATE TABLE jobs (
        job_id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_id INTEGER,
        job_title STRING,
        FOREIGN KEY (company_id) REFERENCES companies(company_id)
    );
''')

# Insert sample data into jobs table
cursor.execute('''
    INSERT INTO jobs (company_id, job_title) VALUES
    (1, 'Software Engineer'),
    (1, 'Data Analyst'),
    (2, 'Data Scientist'),
    (3, 'Cloud Engineer');
''')

# Print out company names and their corresponding jobs using JOIN
cursor.execute('''SELECT companies.company_name, jobs.job_title
    FROM companies
    JOIN jobs ON companies.company_id = jobs.company_id;
''')
# Print out the values
print("\nCompanies and their jobs:")
for row in cursor.fetchall():
    print(row)

# Many-to-Many: Candidates and Jobs (with intermediate candidate_job table)
cursor.execute('''CREATE TABLE candidates_jobs (
        job_id INTEGER,
        candidate_id INTEGER,
        PRIMARY KEY (candidate_id, job_id),
        FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id),
        FOREIGN KEY (job_id) REFERENCES jobs(job_id)
        );
''')

# Insert sample data into candidate_job table
cursor.execute('''
    INSERT INTO candidates_jobs (candidate_id, job_id) VALUES
    (1, 1),
    (1, 2),
    (2, 3),
    (3, 4);
''')

# Print out candidates and the jobs they are applying for using JOIN
cursor.execute('''SELECT candidates.first_name, candidates.last_name, jobs.job_title
    FROM candidates
    JOIN candidates_jobs ON candidates.candidate_id = candidates_jobs.candidate_id
    JOIN jobs ON candidates_jobs.job_id = jobs.job_id;
''')
# Print out the values
print("\nCandidates and their jobs:")
for row in cursor.fetchall():
    print(row)


# Print out candidates, the jobs, and the associated company they are applying for using JOIN
cursor.execute('''SELECT candidates.first_name, candidates.last_name, jobs.job_title, companies.company_name
    FROM candidates
    JOIN candidates_jobs ON candidates.candidate_id = candidates_jobs.candidate_id
    JOIN jobs ON candidates_jobs.job_id = jobs.job_id
    JOIN companies ON jobs.company_id = companies.company_id;
''')

# Print out the values
print("\nCandidates, their jobs, and the associated company:")
for row in cursor.fetchall():
    print(row)
    
# DON'T EDIT BELOW THIS LINE. Commit and close the connection
connection.commit()
connection.close()