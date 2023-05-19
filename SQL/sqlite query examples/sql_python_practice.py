import sqlite3

# Connect to database
conn = sqlite3.connect('students.sqlite3')
cursor = conn.cursor()

# Create table
create_table_query = '''CREATE TABLE IF NOT EXISTS students (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            age INTEGER(3),
                            gender TEXT,
                            major TEXT
                        );'''
cursor.execute(create_table_query)

# Insert data
insert_query = '''INSERT INTO students (name, age, gender, major) VALUES ('Mohamed', 25, 'M', 'Computer Science');'''
cursor.execute(insert_query)

# Inserting multiple rows at once
students = [('Alice', 20, 'F', 'Math'),
            ('Bob', 22, 'M', 'English'),
            ('Charlie', 19, 'M', 'History')]
insert_query_2 = '''INSERT INTO students (name, age, gender, major) VALUES (?,?,?,?);'''
cursor.executemany(insert_query_2, students)

# Updating a single row
update_query = '''UPDATE students SET major = 'Physics' WHERE name = 'Alice';'''
cursor.execute(update_query)

# Deleting a single row
delete_query = '''DELETE FROM students WHERE name = 'Charlie';'''
cursor.execute(delete_query)

# Querying a table with conditions
query = '''SELECT * FROM students WHERE age >= 20 AND gender = 'M';'''
cursor.execute(query)
print(cursor.fetchall())

# Querying multiple tables with JOIN
# Create a new table
create_table_query = '''CREATE TABLE IF NOT EXISTS courses (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            credits INTEGER,
                            instructor TEXT
                        );'''
cursor.execute(create_table_query)

# Insert data into the courses table
courses = [('Math 101', 3, 'Dr. Smith'),
            ('English 201', 4, 'Dr. Johnson'),
            ('History 301', 3, 'Dr. Lee')]
insert_query = '''INSERT INTO courses (name, credits, instructor) VALUES (?,?,?);'''
cursor.executemany(insert_query, courses)

# Join the students and courses tables on the major and name columns
query = '''SELECT students.name, students.major, courses.name, courses.instructor FROM students
           JOIN courses ON students.major = courses.name
           WHERE students.name = 'Bob';'''
cursor.execute(query)
print(cursor.fetchall())

# Save (commit) the changes
conn.commit()

# Fetch data
cursor.execute("SELECT DISTINCT * FROM students; ")
print(cursor.fetchall())

# Close the connection
conn.close()
