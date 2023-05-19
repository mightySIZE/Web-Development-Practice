import sqlite3

conn = sqlite3.connect('OOPS.sqlite3')
cursor = conn.cursor()

# Create table
table_query = '''CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    salary FLOAT
    );'''
cursor.execute(table_query)

# Create class Employee
class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def print_details(self):
        print('ID: {}, Name: {}, Salary: {}'.format(self.id, self.name, self.salary))

employee = Employee(1, 'John', 10000.0)
employee2 = Employee(2, 'Jane', 20000.0)

# Insert employee
insert_query = '''INSERT INTO employee (id, name, salary) VALUES ({}, '{}', {});'''.format(employee.id, employee.name, employee.salary)
cursor.execute(insert_query)

# Insert employee2
insert_query = '''INSERT INTO employee (id, name, salary) VALUES ({}, '{}', {});'''.format(employee2.id, employee2.name, employee2.salary)
cursor.execute(insert_query)

# Commit the changes
conn.commit()

# Fetch data
cursor.execute("SELECT * FROM employee;")
print(cursor.fetchall())
print(employee.print_details())

# Close the connection
conn.close()