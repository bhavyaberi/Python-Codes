from db import db_cursor, db_connection
import random

# Dummy data for the Student table
students_data = [
    (
        "S1001",
        "John Doe",
        "2005-02-15",
        "Male",
        "123 Elm St, City",
        "9876543210",
        "johndoe@example.com",
        "123456789012",
        "Michael Doe",
        "Sarah Doe",
        "2020-06-01",
        "1",
    ),
    (
        "S1002",
        "Jane Smith",
        "2006-05-20",
        "Female",
        "456 Oak Ave, City",
        "9876543211",
        "janesmith@example.com",
        "234567890123",
        "Robert Smith",
        "Emily Smith",
        "2021-07-10",
        "4",
    ),
    (
        "S1003",
        "Mark Johnson",
        "2004-11-11",
        "Male",
        "789 Pine Rd, City",
        "9876543212",
        "markjohnson@example.com",
        "345678901234",
        "James Johnson",
        "Linda Johnson",
        "2019-05-15",
        "3",
    ),
    (
        "S1004",
        "Emily Davis",
        "2007-01-30",
        "Female",
        "321 Maple Dr, City",
        "9876543213",
        "emilydavis@example.com",
        "456789012345",
        "Daniel Davis",
        "Olivia Davis",
        "2022-08-20",
        "6",
    ),
    (
        "S1005",
        "Lucas Lee",
        "2005-09-25",
        "Male",
        "654 Birch Blvd, City",
        "9876543214",
        "lucaslee@example.com",
        "567890123456",
        "Chris Lee",
        "Nancy Lee",
        "2020-10-05",
        "9",
    ),
]

# Inserting data into the Student table
insert_query = """
INSERT INTO Student (admNo, name, dob, gender, address, phone, email, aadhar, father, mother, admissionDate, admissionClass)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Execute insert statements for each student in the dummy data
for student in students_data:
    db_cursor.execute(insert_query, student)

# Commit the transaction to the database
db_connection.commit()

print("Dummy data inserted successfully.")

# Insert fees data for the 5 students for months from April of 2024
for admNo in range(1001, 1006):
    for month in range(4, 13):
        amount = 10000 + admNo
        date = f"2024-{month}-{random.randint(1, 28)}"

        query = """
        INSERT INTO Fees (admNo, month, year, date, amount, paid)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            f"S{admNo}",
            month,
            2024,
            date,
            amount,
            "No" if month == 12 else "Yes",
        )

        # Execute the insert query
        db_cursor.execute(query, values)
        db_connection.commit()
