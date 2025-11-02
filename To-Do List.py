import datetime
import csv

welcome_str = """Welcome to my To-Do list  📃
Stay organized, boost productivity, and never miss a task! Here is a simple platform that allows you to save your task with an ease...
"""

to_do_menu_str = """---------------------------------------------------------------To-Do List Menu---------------------------------------------------------
Select Choice:
1. Add Task
2. Remove Task
3. Display All Tasks
4. Display Overdue Tasks
5. Mark Task as Completed
6. Save and Exit
7. Show Average Rating"""


class Task:

    def __init__(self, title, description, deadline, completed=False):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = completed

    def completion(self):
        self.completed = True

    def overdue(self):
        due_date = datetime.datetime.strptime(self.deadline, "%Y-%m-%d")
        current = datetime.datetime.now()
        return current > due_date and not self.completed

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"\tTask: {self.title}\n\tDescription: {self.description}\n\tDeadline: {self.deadline}\n\tStatus: {status}"


class Todolist:
    csv_header = ['Title', 'Description', 'Deadline', 'Completed']

    def __init__(self):
        self.tasks = []

    def add(self, title, description, deadline):
        task = Task(title, description, deadline)
        self.tasks.append(task)
        print(f"Task '{title}' added to your list \n \n")

    def remove_input(self):
        if not self.tasks:
            print("No task/s found in your list \n \n")
            return

        title = input("Enter task title to remove: ")
        self.remove(title)

    def remove(self, title):
        if not self.tasks:
            print("No task/s found in your list \n \n")
            return
        
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.title != title]
        if len(self.tasks) == initial_count:
            print("No such task found\n\n")
        else:
            print(f"Task '{title}' removed from your to-do list. \n\n")

    def display_all(self):
        if not self.tasks:
            print("No task/s found in your list \n \n")
            return
        
        for i, task in enumerate(self.tasks):
            print(i+1, ". ", task, sep="")
            print()

    def display_overdue(self):
        if not self.tasks:
            print("No task/s found in your list \n \n")
            return

        overdue_tasks = [task for task in self.tasks if task.overdue()]
        if not overdue_tasks:
            print("No overdue task in your list \n \n")
        else:
            for i, task in enumerate(overdue_tasks):
                print(i+1, ". ", task, sep="")
                print()

    def mark_completed_input(self):
        if not self.tasks:
            print("No task/s found in your list \n \n")
            return

        title = input("Enter task title to mark as completed: ")
        self.mark_completed(title)

    def mark_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.completion()
                print(f"Task '{title}' marked as completed.\n\n")
                return
        
        print("No such task found\n\n")

    def save(self, filename='todo.csv'):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.csv_header)
            for task in self.tasks:
                writer.writerow([task.title, task.description, task.deadline, task.completed])


    def load(self, filename='todo.csv'):
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader, None)
                
                for row in reader:
                    title, description, deadline, completed_str = row
                    completed = completed_str == 'True'
                    task = Task(title, description, deadline, completed)
                    self.tasks.append(task)
        except FileNotFoundError:
            print("No previous tasks found, starting fresh.\n\n")

class Ratings:
    csv_header = ['Rating', 'Suggestion', 'Time']
    
    def __init__(self, filename='ratings.csv'):
        self.filename = filename
        self.ratings = []

    def add_rating(self, rating, suggestion=""):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.ratings.append((rating, suggestion, current_time))

    def get_average_rating(self):
        if not self.ratings:
            return 0, 0
        total = sum(rating[0] for rating in self.ratings)
        count = len(self.ratings)
        average = total / count
        return average, count
    
    def display_average_rating(self):
        average, count = self.get_average_rating()
        if count > 0:
            print(f"Average Rating: {average:.2f}/5 (Based on {count} rating{'s' if count != 1 else ''})\n\n")
        else:
            print("No ratings available yet.\n\n")

    def save(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.csv_header)
            for rating in self.ratings:
                writer.writerow([rating[0], rating[1], rating[2]])

    def load(self):
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader, None)
                
                for row in reader:
                    rating, suggestion, time = row
                    self.ratings.append((int(rating), suggestion, time))
        except FileNotFoundError:
            pass

def main():
    todolist = Todolist()
    todolist.load()

    ratings = Ratings()
    ratings.load()

    print(welcome_str)

    try:
        while True:
            print(to_do_menu_str)

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.\n\n")
                continue

            if choice == 1:
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                deadline = input("Enter task deadline (YYYY-MM-DD): ")
                todolist.add(title, description, deadline)

            elif choice == 2:
                todolist.remove_input()

            elif choice == 3:
                todolist.display_all()

            elif choice == 4:
                todolist.display_overdue()

            elif choice == 5:
                todolist.mark_completed_input()

            elif choice == 6:
                todolist.save()
                print("Exiting the To-Do List interface\n\n")
                print("||||| Thank you for using |||||")
                rate = -1

                while rate < 1 or rate > 5:
                    rate = int(input("Please rate us from 1 to 5: "))
                    if rate == 5:
                        print("Have a beautiful day!")
                    elif 3 <= rate < 5:
                        print("We will improve. Have a good day!")
                    elif 0 < rate < 3:
                        print("Kindly give suggestions for improvement...")
                        suggest = input()
                        print("We will work on it. Have a good day!")
                    else:
                        print("Invalid rating. Please enter a number between 1 and 5.")
                
                ratings.add_rating(rate, suggest if rate < 3 else "")
                ratings.save()
                break

            elif choice == 7:
                ratings.display_average_rating()

            else:
                print("Invalid option. Please choose a valid option.")
    except KeyboardInterrupt:
        print("\n\nKeyboard interrupt detected! Saving your tasks before exiting...")
        todolist.save()
        print("Tasks saved successfully.")
        print("Exiting the To-Do List interface\n")
        print("""||||| Thank you for using |||||""")


# Run the program
if __name__ == "__main__":
    main()
