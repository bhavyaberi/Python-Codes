import random
from db import db_cursor, db_connection
from datetime import date, timedelta

# List of possible roles and genders
genders = ["Male", "Female", "Other"]
roles = ["Teacher", "Staff"]


# Function to generate random employee data
def generate_random_data():
    # Generate random employee data
    name = f"Employee {random.randint(1, 1000)}"  # Simple random name pattern
    dob = date.today() - timedelta(
        days=random.randint(8000, 22000)
    )  # Random date of birth between 22-60 years old
    address = f"{random.randint(100, 999)} Street, City {random.randint(1, 100)}"
    phone = f"+91-{random.randint(1000000000, 9999999999)}"
    email = f"emp{random.randint(1, 1000)}@example.com"
    aadhar = (
        f"{random.randint(100000000000, 999999999999)}"  # Random 12-digit Aadhar number
    )
    gender = random.choice(genders)
    role = random.choice(roles)
    subjects = (
        f"Subject{random.randint(1, 5)}" if role == "Teacher" else None
    )  # Assign subjects to Teachers
    offices = f"Office-{random.randint(1, 10)}" if role != "Teacher" else None

    return (name, dob, gender, address, phone, email, aadhar, role, subjects, offices)


# Insert 6 rows into the Employee table with uniform distribution
for _ in range(6):
    name, dob, gender, address, phone, email, aadhar, role, subjects, offices = (
        generate_random_data()
    )

    query = """
    INSERT INTO Employee (name, dob, gender, address, phone, email, aadhar, role, subjects, offices)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    values = (name, dob, gender, address, phone, email, aadhar, role, subjects, offices)

    # Execute the insert query
    db_cursor.execute(query, values)

# Commit the transaction to the database
db_connection.commit()

print("6 rows inserted successfully into Employee table.")


# Insert salary data for the 6 employees for all months of 2024
for eid in range(1000, 1006):
    for month in range(1, 13):
        salary = random.randint(20000, 80000)
        dat = f"2024-{month}-01"

        query = """
        INSERT INTO Salary (eid, month, year, date, amount)
        VALUES (%s, %s, %s, %s, %s);
        """
        values = (eid, month, 2024, dat, salary)

        # Execute the insert query
        db_cursor.execute(query, values)
        db_connection.commit()