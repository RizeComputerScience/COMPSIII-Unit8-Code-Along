import sqlite3
import os

# Test that the candidate_profiles table has been created
def test_candidate_profiles_exists():
    """Verify that the candidate_profiles table exists in the database."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Check if users table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='candidate_profiles';")
    result = cursor.fetchone()
    assert result is not None, "Candidate_profiles table does not exist"
    
    connection.close()

# Test that the candidate_profiles table has the correct columns
def test_candidate_profiles_table_columns():
    """Verify the schema of the candidate_profiles table."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Get table info
    cursor.execute("PRAGMA table_info(candidate_profiles);")
    columns = cursor.fetchall()
    
    # Expected columns and their types
    expected_columns = [
        ('profile_id', 'INTEGER', 1, None, 1),  # Primary key, autoincrement
        ('candidate_id', 'INTEGER', 0, None, 0),
        ('resume_url', 'STRING', 0, None, 0),
        ('linkedin_url', 'STRING', 0, None, 0),
        ('location', 'STRING', 0, None, 0)
    ]
    
    # Check number of columns
    assert len(columns) == 5, f"Expected 5 columns, found {len(columns)}"
    
    # Check each column's details
    for expected, actual in zip(expected_columns, columns):
        assert actual[1] == expected[0], f"Column name mismatch: expected {expected[0]}, got {actual[1]}"
        assert actual[2] == expected[1], f"Column type mismatch for {actual[1]}"
        assert actual[5] == expected[4], f"Primary key configuration mismatch for {actual[1]}"
    
    connection.close()

# Test that the foreign key constraint is set up correctly
def test_candidate_profiles_foreign_key():
    """Verify the foreign key constraint on candidate_id."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Check foreign key constraints
    cursor.execute("PRAGMA foreign_key_list(candidate_profiles);")
    foreign_keys = cursor.fetchall()
    
    assert len(foreign_keys) == 1, "Expected one foreign key constraint"
    
    foreign_key = foreign_keys[0]
    assert foreign_key[2] == 'candidates', "Foreign key should reference users table"
    assert foreign_key[3] == 'candidate_id', "Foreign key should reference user_id column"

# Test that the jobs table has been created
def test_jobs_table_exists():
    """Verify that the jobs table exists in the database."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Check if users table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='jobs';")
    result = cursor.fetchone()
    assert result is not None, "Jobs table does not exist"
    
    connection.close()

# Test that the jobs table has the correct columns
def test_jobs_table_columns():
    """Verify the schema of the jobs table."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Get table info
    cursor.execute("PRAGMA table_info(jobs);")
    columns = cursor.fetchall()
    
    # Expected columns and their types
    expected_columns = [
        ('job_id', 'INTEGER', 1, None, 1),  # Primary key, autoincrement
        ('company_id', 'INTEGER', 0, None, 0),
        ('job_title', 'STRING', 0, None, 0),
    ]

    # Check number of columns
    assert len(columns) == 3, f"Expected 3 columns, found {len(columns)}"
    
    # Check each column's details
    for expected, actual in zip(expected_columns, columns):
        assert actual[1] == expected[0], f"Column name mismatch: expected {expected[0]}, got {actual[1]}"
        assert actual[2] == expected[1], f"Column type mismatch for {actual[1]}"
        assert actual[5] == expected[4], f"Primary key configuration mismatch for {actual[1]}"
    
    connection.close()

# Test that the foreign key constraint is set up correctly for jobs
def test_jobs_foreign_key():
    """Verify the foreign key constraint on company_id."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    # Check foreign key constraints
    cursor.execute("PRAGMA foreign_key_list(jobs);")
    foreign_keys = cursor.fetchall()
    
    assert len(foreign_keys) == 1, "Expected one foreign key constraint"
    
    foreign_key = foreign_keys[0]
    assert foreign_key[2] == 'companies', "Foreign key should reference companies table"
    assert foreign_key[3] == 'company_id', "Foreign key should reference company_id column"

# Test that the candidates_jobs table has been created
def test_candidates_jobs_table_exists():
    """Verify that the user_workout table exists in the database."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='candidates_jobs';")
    result = cursor.fetchone()
    assert result is not None, "candidates_jobs table does not exist"
    
    connection.close()

# Test that the workouts table has the correct columns
def test_candidate_jobs_columns():
    """Verify the schema of the workouts table."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    cursor.execute("PRAGMA table_info(candidates_jobs);")
    columns = cursor.fetchall()
    
    expected_columns = [
        ('job_id', 'INTEGER', 1, None, 1),
        ('candidate_id', 'INTEGER', 0, None, 0),
    ]
    
    assert len(columns) == 2, f"Expected 2 columns, found {len(columns)}"
    
    for expected, actual in zip(expected_columns, columns):
        assert actual[1] == expected[0], f"Column name mismatch: expected {expected[0]}, got {actual[1]}"
        assert actual[2] == expected[1], f"Column type mismatch for {actual[1]}"

    connection.close()

# Test that the foreign key constraints are set up correctly
def test_candidates_jobs_foreign_keys():
    """Verify foreign key constraints in user_workout table."""
    db_path = os.path.join(os.path.dirname(__file__), '..', 'tech_talent.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    cursor.execute("PRAGMA foreign_key_list(candidates_jobs);")
    foreign_keys = cursor.fetchall()
    
    assert len(foreign_keys) == 2, "Expected two foreign key constraints"
    
    foreign_key_tables = {fk[2] for fk in foreign_keys}
    assert foreign_key_tables == {'candidates', 'jobs'}, "Foreign keys should reference candidates and jobs tables"
    
    connection.close()