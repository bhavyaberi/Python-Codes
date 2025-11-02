from datetime import date
from mysql.connector import Error

from db import db_cursor, db_connection
from utils import email_checker, phone_checker, aadhar_checker


def view_profile(eid, role):
    db_cursor.execute("SELECT * FROM Employee WHERE eid=%s", (eid,))
    result = db_cursor.fetchone()
    if result:
        print("\nEmployee Profile for Employee ID", eid)
        print(f"{'Name:':<20} {result[1]}")
        print(f"{'Date of Birth:':<20} {result[2]}")
        print(f"{'Gender:':<20} {result[3]}")
        print(f"{'Address:':<20} {result[4]}")
        print(f"{'Phone:':<20} {result[5]}")
        print(f"{'Email:':<20} {result[6]}")
        print(f"{'Aadhar:':<20} {result[7]}")
        if role == "Teacher":
            print(f"{'Subjects:':<20} {result[9]}")
        else:
            print(f"{'Offices:':<20} {result[9]}")
    else:
        print(f"No profile found for Employee ID: {eid}")


def edit_profile(eid, role="teacher"):
    db_cursor.execute("SELECT * FROM Employee WHERE eid=%s", (eid,))
    result = db_cursor.fetchone()
    if not result:
        print(f"No profile found for Employee ID: {eid}")
        return

    print("\nEdit Profile for Employee ID", eid)
    print("If you don't want to change a field, leave it empty.")
    print("Enter new details below:")
    name = input(f"Name ({result[1]}): ") or result[1]
    dob = input(f"Date of Birth ({result[2]}): ") or result[2]
    while True:
        gender = input("Gender ('Male', 'Female', 'Other'): ") or result[3]
        if gender not in ("Male", "Female", "Other"):
            print("Invalid entry. Please try again.")
        else:
            break

    address = input(f"Address ({result[4]}): ") or result[4]

    while True:
        phone = input(f"Phone ({result[5]}): ") or result[5]
        if phone_checker(phone):
            break
        print("Invalid phone number. Please try again.")

    while True:
        email = input(f"Email ({result[6]}): ") or result[6]
        if email_checker(email):
            break
        print("Invalid email. Please try again.")

    aadhar = result[7]
    subjects, offices = result[9], result[10]
    if role.lower() == "admin":
        while True:
            aadhar = input(f"Aadhar ({result[7]}): ") or result[7]
            if aadhar == result[7]:
                break
            if aadhar_checker(aadhar):
                break
            print("Invalid Aadhar number. Please try again.")

        if role == "Teacher":
            subjects = input(f"Subjects ({result[9]}): ") or result[9]
        else:
            offices = input(f"Offices ({result[10]}): ") or result[10]

    edit_query = """
    UPDATE Employee
    SET name = %s,
        dob = %s,
        gender = %s,
        address = %s,
        phone = %s,
        email = %s,
        aadhar = %s,
        %s = %s
    WHERE eid = %s
    """

    try:
        db_cursor.execute(
            edit_query,
            (
                name,
                dob,
                gender,
                address,
                phone,
                email,
                aadhar,
                "subjects" if role == "Teacher" else "offices",
                subjects if role == "Teacher" else offices,
                eid,
            ),
        )
        db_connection.commit()
        print(f"Profile updated successfully for Employee ID {eid}.")
        return True
    except Error as e:
        print(f"An error occurred while updating the profile: {e}")
        print("Please contact the administrator if the issue persists.")
        return False


def view_salary(eid):
    db_cursor.execute("SELECT * FROM Employee WHERE eid=%s", (eid,))
    result = db_cursor.fetchone()
    if not result:
        print(f"No profile found for Employee ID: {eid}")
        return

    month = int(input("Enter month: "))
    year = int(input("Enter year: "))

    # Check if it is less than the current month and year
    curr_date = date.today()
    if year > curr_date.year or (year == curr_date.year and month > curr_date.month):
        print("Salary for future months cannot be viewed.")
        return

    db_cursor.execute(
        "SELECT * FROM Salary WHERE eid=%s AND month=%s AND year=%s", (eid, month, year)
    )
    result = db_cursor.fetchone()

    if result:
        print(f"Salary for Employee ID {eid} for {month}/{year}")
        print(f"{'Amount:':<20} {result[3]}")
        print(f"{'Date:':<20} {result[4]}")
    else:
        print(f"No salary found for Employee ID {eid} for {month}/{year}")


def add_employee():
    print("\nAdd Employee =>")
    name = input("Name: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")

    while True:
        gender = input("Gender ('Male', 'Female', 'Other'): ")
        if gender not in ("Male", "Female", "Other"):
            print("Invalid entry. Please try again.")
        else:
            break

    address = input("Address: ")

    while True:
        phone = input("Phone: ")
        if phone_checker(phone):
            break
        print("Invalid phone number. Please try again.")
    while True:
        email = input("Email: ")
        if email_checker(email):
            break
        print("Invalid email. Please try again.")
    while True:
        aadhar = input("Aadhar Number: ")
        if aadhar_checker(aadhar):
            break
        print("Invalid Aadhar number. Please try again.")

    while True:
        role = input("Role ('Teacher', 'Staff'): ")
        if role not in ("Teacher", "Staff"):
            print("Invalid entry. Please try again.")
        else:
            break

    subjects, offices = None, None
    if role == "Teacher":
        subjects = input("Subjects (comma separated): ")
    else:
        offices = input("Offices (comma separated): ")

    add_query = """
    INSERT INTO Employee
    (name, dob, gender, address, phone, email, aadhar, role, %s)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    try:
        db_cursor.execute(
            add_query % ("subjects" if role == "Teacher" else "offices"),
            (
                name,
                dob,
                gender,
                address,
                phone,
                email,
                aadhar,
                role,
                subjects if role == "Teacher" else offices,
            ),
        )
        db_connection.commit()

        # Get the employee ID by email
        db_cursor.execute("SELECT eid FROM Employee WHERE email=%s", (email,))
        result = db_cursor.fetchone()
        print(f"Employee added successfully with Employee ID {result[0]}.")
    except Error as e:
        print(f"An error occurred while adding the employee: {e}")
        print("Please contact the administrator if the issue persists.")
        return False

def pay_salary(eid):
    db_cursor.execute("SELECT * FROM Employee WHERE eid=%s", (eid,))
    result = db_cursor.fetchone()
    if not result:
        print(f"No profile found for Employee ID: {eid}")
        return

    month = int(input("Enter month: "))
    year = int(input("Enter year: "))
    amount = float(input("Enter amount: "))
    date_paid = date.today()

    pay_query = """
    INSERT INTO Salary
    (eid, month, year, amount, date)
    VALUES (%s, %s, %s, %s, %s)
    """

    try:
        db_cursor.execute(pay_query, (eid, month, year, amount, date_paid))
        db_connection.commit()
        print(f"Salary paid successfully for Employee ID {eid} for {month}/{year}.")
        return True
    except Error as e:
        print(f"An error occurred while paying the salary: {e}")
        print("Please contact the administrator if the issue persists.")
        return False