from db import db_cursor


def email_checker(email):
    # Check if "@" is in the email and not at the start or end
    if "@" not in email or email.startswith("@") or email.endswith("@"):
        return False

    parts = email.split("@")
    if len(parts) != 2:
        return False
    else:
        username, domain = parts

    # Check if the domain contains a "." and is not at the start or end
    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        return False

    # Check if username and domain are non-empty
    if not username or not domain:
        return False

    # Check if the username contains only valid characters
    for char in username:
        if not (char.isalnum() or char in "._-"):
            return False

    # Check if the domain contains only valid characters
    for char in domain:
        if not (char.isalnum() or char in ".-"):
            return False

    # Check for the email in the database, if it's already there, return False
    db_cursor.execute("SELECT * FROM Student WHERE email=%s", (email,))
    result = db_cursor.fetchone()
    if result:
        return False

    return True


def phone_checker(phone):
    if len(phone) < 10 or len(phone) > 10:
        print("\nEnter complete phone number of 10 digits\nPlease try again")
        return False
    if not phone.isdigit() and 6 <= int(phone[0]) <= 9:
        print("\nPlease enter correct phone number")
        return False

    # Check for the phone number in the database, if it's already there, return False
    db_cursor.execute("SELECT * FROM Student WHERE phone=%s", (phone,))
    result = db_cursor.fetchone()
    if result:
        return False

    return True

def aadhar_checker(number):
    if len(number) < 12 or len(number) > 12:
        print("\nEnter complete Aadhar number of 12 digits\nPlease try again")
        return False
    if not number.isdigit():
        print("\nPlease enter correct Aadhar number")
        return False

    # Check for the Aadhar number in the database, if it's already there, return False
    db_cursor.execute("SELECT * FROM Student WHERE aadhar=%s", (number,))
    result = db_cursor.fetchone()
    if result:
        return False

    return True

if __name__ == "__main__":
    # email = input("Enter email: ")
    email = "johndoe@example.com"
    print(email_checker(email))