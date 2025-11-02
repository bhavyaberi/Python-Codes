import time
from web import replit_link


def print_start():
    print("Welcome to BJ International School Management System")
    print("------------------------------------------------------")
    print("""
    ____       _    _____           _                 
   |  _ \\     | |  / ____|         | |                
   | |_) |    | | | (___  _   _ ___| |_ ___ _ __ ___  
   |  _ < _   | |  \\___ \\| | | / __| __/ _ | '_ ` _ \\ 
   | |_) | |__| |  ____) | |_| \\__ | ||  __| | | | | |
   |____/ \\____/  |_____/ \\__, |___/\\__\\___|_| |_| |_|
                           __/ |                      
                          |___/                       
""")


def print_end():
    print("\nThank you for using the BJ International School Management System")
    print("------------------------------------------------------------------")

    print("\t\t   ^ ^  ")
    print("\t\t ! ` ` !")
    print("\t\t    '   ")
    print("\t\t   <->  ")

    print()
    print("Exiting...")
    time.sleep(3)
    return


def about():
    print("BJ International School Management System")
    print("Authors:")
    print("\t1. Bhavya Beri (12th C, 13668142)")
    print("\t2. Jaiveer Chaudhary (12th C, 13668156)")
    print("Open the link to view the project codebase?")
    link_open = input(" (Y/N): ")
    if link_open.lower() == "y":
        replit_link()
