import webbrowser
import time

def replit_link():
    try:
        webbrowser.open('https://replit.com/@bhavyaberi/queen')
        time.sleep(3.1)
        input("Press Enter to continue...")
    except Exception as e:
        print(e)
        print("Please check your internet connection")