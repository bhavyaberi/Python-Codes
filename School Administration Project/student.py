from datetime import date
from mysql.connector import Error

from db import db_cursor, db_connection
from utils import email_checker, phone_checker, aadhar_checker


def get_current_class(admDate, admClass):
    current_date = date.today()
    admission_year = admDate.year
    current_year = current_date.year

    if current_date.month < 4:
        current_year -= 1

    if admDate.month < 4:
        admission_year -= 1

    years_completed = current_year - admission_year
    current_class = admClass + years_completed

    return min(current_class, 12)


def view_profile(admNo):
    db_cursor.execute("SELECT * FROM Student WHERE admNo=%s", (admNo,))
    result = db_cursor.fetchone()
    if result:
        print("\nStudent Profile for Admission Number", admNo)
        print(f"{'Name:':<20} {result[1]}")
        print(f"{'Date of Birth:':<20} {result[2]}")
        print(f"{'Gender:':<20} {result[3]}")
        print(f"{'Address:':<20} {result[4]}")
        print(f"{'Phone:':<20} {result[5]}")
        print(f"{'Email:':<20} {result[6]}")
        print(f"{'Aadhar:':<20} {result[7]}")
        print(f"{'Father\'s Name:':<20} {result[8]}")
        print(f"{'Mother\'s Name:':<20} {result[9]}")
        print(f"{'Admission Date:':<20} {result[10]}")
        print(f"{'Admission Class:':<20} {result[11]}")
        print(f"{'Current Class:':<20} {get_current_class(result[10], result[11])}")
    else:
        print(f"No profile found for Admission Number: {admNo}")


def edit_profile(admNo, role="student"):
    db_cursor.execute("SELECT * FROM Student WHERE admNo=%s", (admNo,))
    result = db_cursor.fetchone()
    if not result:
        print(f"No profile found for Admission Number: {admNo}")
        return

    print("\nEdit Profile for Admission Number", admNo)
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
    father = input(f"Father's Name ({result[8]}): ") or result[8]
    mother = input(f"Mother's Name ({result[9]}): ") or result[9]

    while True:
        email = input(f"Email ({result[6]}): ") or result[6]
        if email == result[6]:
            break
        if len(email) >= 5 and email_checker(email):
            break
        print("Invalid email. Please enter a valid email address.")

    while True:
        phone = input(f"Phone ({result[5]}): ") or result[5]
        if phone == result[5]:
            break
        if phone_checker(phone):
            break
        print("Invalid phone number. Please enter a valid phone number.")

    aadhar = result[7]
    if role.lower() == "admin":
        while True:
            aadhar = input(f"Aadhar ({result[7]}): ") or result[7]
            if aadhar == result[7]:
                break
            if aadhar_checker(aadhar):
                break
            print("Invalid Aadhar number. Please try again.")

    edit_query = """
    UPDATE Student
    SET name = %s,
        dob = %s,
        gender = %s,
        address = %s,
        phone = %s,
        email = %s,
        father = %s,
        mother = %s,
        aadhar = %s
    WHERE admNo = %s
    """

    try:
        # Execute the UPDATE query
        db_cursor.execute(
            edit_query,
            (name, dob, gender, address, phone, email, father, mother, aadhar, admNo),
        )
        db_connection.commit()
        print(f"Profile for Admission Number {admNo} has been updated successfully.")
        return True
    except Error as e:
        print(f"An error occurred while updating the profile: {e}")
        print("Please contact the administrator if the issue persists.")
        return False


def add_student():
    print("\nAdd Student =>")
    admNo = input("Admission Number: ")
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

    father = input("Father's Name: ")
    mother = input("Mother's Name: ")
    admissionDate = date.today()
    admissionClass = int(input("Admission Class: "))

    add_query = """
    INSERT INTO Student
    (admNo, name, dob, gender, address, phone, email, aadhar, father, mother, admissionDate, admissionClass)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    try:
        db_cursor.execute(
            add_query,
            (
                admNo,
                name,
                dob,
                gender,
                address,
                phone,
                email,
                aadhar,
                father,
                mother,
                admissionDate,
                admissionClass,
            ),
        )
        db_connection.commit()
        print(f"Student with Admission Number {admNo} has been added successfully.")
        return True
    except Error as e:
        print(f"An error occurred while adding the student: {e}")
        print("Please contact the administrator if the issue persists.")
        return False


def add_fees(admNo):
    print("\nAdd Fees =>")
    month = int(input("Month (1-12): "))
    year = int(input("Year: "))
    amount = float(input("Amount: "))
    paid = "No"

    add_query = """
    INSERT INTO Fees
    (admNo, month, year, date, amount, paid)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    try:
        db_cursor.execute(
            add_query,
            (admNo, month, year, date.today(), amount, paid),
        )
        db_connection.commit()
        print(f"Fees for Admission Number {admNo} has been added successfully.")
        return True
    except Error as e:
        print(f"An error occurred while adding the fees: {e}")
        print("Please contact the administrator if the issue persists.")
        return False


def pay_fees(admNo):
    print("\nPay Fees =>")
    month = int(input("Month (1-12): "))
    year = int(input("Year: "))

    pay_query = """
    SELECT * FROM Fees WHERE admNo=%s AND month=%s AND year=%s
    """
    db_cursor.execute(pay_query, (admNo, month, year))
    result = db_cursor.fetchone()
    if not result:
        print(f"No fees found for Admission Number {admNo} for {month}/{year}.")
        return

    if result[5] == "Yes":
        print(
            f"Fees for Admission Number {admNo} for {month}/{year} has already been paid."
        )
        return

    amount = result[4]
    print(f"Amount to be paid: {amount}")
    user_input = input("Do you want to pay the fees? (Y/N): ")
    if user_input.lower() == "n":
        return

    pay_query = """
    UPDATE Fees
    SET paid = YES
    WHERE admNo = %s AND month = %s AND year = %s
    """

    try:
        db_cursor.execute(
            pay_query,
            (admNo, month, year),
        )
        db_connection.commit()
        print(
            f"Fees for Admission Number {admNo} for {month}/{year} has been paid successfully."
        )
        return True
    except Error as e:
        print(f"An error occurred while paying the fees: {e}")
        print("Please contact the administrator if the issue persists.")
        return False

def view_fees(admNo):
    print("\nView Fees =>")
    print("1. View pending fees")
    print("2. View by month")

    user_input = input("-> ")
    if user_input == "1":
        view_query = """
        SELECT * FROM Fees WHERE admNo=%s AND paid='No'
        """
        db_cursor.execute(view_query, (admNo,))
        result = db_cursor.fetchall()
        if not result:
            print(f"No pending fees found for Admission Number {admNo}.")
            return

        print(f"Pending fees for Admission Number {admNo}:")
        for row in result:
            print(f"{row[2]}/{row[3]}: {row[4]}")
    elif user_input == "2":
        month = int(input("Month (1-12): "))
        year = int(input("Year: "))
        view_query = """
        SELECT * FROM Fees WHERE admNo=%s AND month=%s AND year=%s
        """
        db_cursor.execute(view_query, (admNo, month, year))
        result = db_cursor.fetchall()
        if not result:
            print(f"No fees found for Admission Number {admNo} for {month}/{year}.")
            return

        print(f"Fees for Admission Number {admNo} for month {month}/{year}:")
        for row in result:
            print("Amount:", row[4])
            print("Paid on:", row[3])
    else:
        print("Invalid choice. Please try again.")
        return False