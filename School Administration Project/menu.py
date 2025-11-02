from student import (
    view_profile as student_view_profile,
    edit_profile as student_edit_profile,
    add_student,
    add_fees,
    view_fees,
    pay_fees,
)

from employee import (
    view_profile as employee_view_profile,
    edit_profile as employee_edit_profile,
    view_salary,
    add_employee,
    pay_salary,
)

from prints import about


def student_menu(admNo):
    print("\nStudent Menu =>")
    print("1. View Profile")
    print("2. Edit Profile")
    print("3. View Fees")
    print("4. Pay Fees")
    print("0. Logout")
    print("A. About the Project")
    user_input = input("-> ")

    if user_input == "0":
        return False
    elif user_input == "A":
        about()
    elif user_input == "1":
        student_view_profile(admNo)
    elif user_input == "2":
        student_edit_profile(admNo)
    elif user_input == "3":
        view_fees(admNo)
    elif user_input == "4":
        pay_fees(admNo)

    return True


def employee_menu(eid, role):
    print("\nEmployee Menu =>")
    print("1. View Profile")
    print("2. Edit Profile")
    print("3. View Salary")
    print("0. Logout")
    print("A. About the Project")
    user_input = input("-> ")

    if user_input == "0":
        return False
    elif user_input == "A":
        about()
    elif user_input == "1":
        employee_view_profile(eid, role)
    elif user_input == "2":
        employee_edit_profile(eid)
    elif user_input == "3":
        view_salary(eid)


def admin_menu():
    print("\nAdmin Menu =>")
    print("1. Add Student")
    print("2. Add Employee")
    print("3. Edit Student")
    print("4. Edit Employee")
    print("5. Add Fees")
    print("6. View Fees")
    print("7. View Salary")
    print("8. Pay Salary")
    print("0. Logout")
    print("A. About the Project")
    user_input = input("-> ")

    if user_input == "0":
        return False
    elif user_input == "A":
        about()
    elif user_input == "1":
        add_student()
    elif user_input == "2":
        add_employee()
    elif user_input == "3":
        admNo = input("Enter Admission Number: ")
        student_edit_profile(admNo, "admin")
    elif user_input == "4":
        eid = input("Enter Employee ID: ")
        employee_edit_profile(eid, "admin")
    elif user_input == "5":
        admNo = input("Enter Admission Number: ")
        add_fees(admNo)
    elif user_input == "6":
        admNo = input("Enter Admission Number: ")
        view_fees(admNo)
    elif user_input == "7":
        eid = input("Enter Employee ID: ")
        view_salary(eid)
    elif user_input == "8":
        eid = input("Enter Employee ID: ")
        pay_salary(eid)

    return True
