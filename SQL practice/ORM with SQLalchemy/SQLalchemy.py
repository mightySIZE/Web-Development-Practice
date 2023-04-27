from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the database engine
engine = create_engine('sqlite:///mydatabase.db', echo=True)

# Create a session factory
Session = sessionmaker(bind=engine)

# Define the table schema
Base = declarative_base()
class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    salary = Column(Float, nullable=False)

# Create the table
Base.metadata.create_all(engine)

# Create a new Employee instance
employee = Employee(name='Tom', salary=10500.0)

# Add the Employee instance to the session and commit the transaction
session = Session()
session.add(employee)
session.commit()

# Query the database and print the results
employees = session.query(Employee).all()
for e in employees:
    print(e.id, e.name, e.salary)

# Close the session
session.close()
