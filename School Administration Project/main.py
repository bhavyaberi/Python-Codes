from db import connection_close
from prints import print_start, print_end
from login import login_main
from menu import student_menu, employee_menu


def main():
    print_start()

    # Call the login function
    login_return = login_main()
    if not login_return:
        print_end()
        return
    else:
        role, username = login_return

    while True:
        if role == "Student":
            if not student_menu(username):
                break
        elif role == "Teacher" or role == "Staff":
            if not employee_menu(username, role):
                break

    # Finally, call the print_end function
    connection_close()
    print_end()
    return


if __name__ == "__main__":
    main()
