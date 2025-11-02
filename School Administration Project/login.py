from captcha import captcha_generator
from getpass import getpass
from db import db_cursor


def password_entry(prompt):
    try:
        password = getpass(prompt + " (Secured entry) -> ")
    except Exception:
        password = input(prompt + " -> ")
    return password


def authenticate(username, password):
    if username == "admin":
        if password == "my_admin_password":
            return "Admin"
        else:
            return None

    # Check if student
    db_cursor.execute("SELECT * FROM Student WHERE admNo=%s", (username,))
    result = db_cursor.fetchone()
    if result:
        # Check if the password is equal to the dob in string format
        if password == str(result[2]):
            return "Student"
        else:
            return None

    # Check if employee
    db_cursor.execute("SELECT * FROM Employee WHERE eid=%s", (username,))
    result = db_cursor.fetchone()
    if result:
        # Check if the password is equal to the dob in string format
        if password == str(result[2]):
            return str(result[8])
        else:
            return None

    return None


def login():
    print("Enter Username: ", end="")
    username = input()
    password = password_entry("Enter password")

    # Generate a captcha
    captcha = captcha_generator(6)
    print("Enter Captcha: ", captcha)
    user_captcha = input("-> ")

    # if captcha != user_captcha:
    #     print("Captcha not matched")
    #     return False

    role = authenticate(username, password)

    if not role:
        print("Username or password is incorrect.")
        return False

    print("Login successful. Welcome", username)

    return (role, username)


def login_main():
    login_attempts = 5

    while True:
        try:
            print("\nTo login, press 1")
            print("To exit, press 0")
            choice = int(input("-> "))
            if choice not in [0, 1]:
                raise ValueError
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        if choice == 1:
            login_result = login()
            if login_result:
                return login_result
            else:
                login_attempts -= 1
                if login_attempts == 0:
                    print("Maximum login attempts reached. Exiting.")
                    return False
                print(f"Login failed. {login_attempts} attempts remaining.")
        elif choice == 0:
            return False


if __name__ == "__main__":
    login_main()
