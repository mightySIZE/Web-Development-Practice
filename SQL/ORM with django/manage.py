from django.db import models, connection

# Define the table schema
class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.FloatField()

    class Meta:
        db_table = 'employee'

# Create a new Employee instance
employee = Employee(name='John', salary=10000.0)

# Add the Employee instance to the database and commit the transaction
employee.save()

# Query the database and print the results
with connection.cursor() as cursor:
    cursor.execute('SELECT * FROM employee')
    for row in cursor.fetchall():
        print(row)

# Delete the Employee instance from the database
employee.delete()
