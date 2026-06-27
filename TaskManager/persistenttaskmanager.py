import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "tasks.json")


def load_tasks():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
    

def save_tasks(tasks):
    with open(FILE_PATH, "w") as file:
        json.dump(tasks, file, indent=2)
       

def view_tasks():
    print("\n--- Current Active Tasks ---")
    if not tasks:
        print("Your task list is empty!")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    print("----------------------------\n")
    
tasks = load_tasks()
    
def add_task():
    new_task = input("Enter a New Task: ").strip()
    if new_task:
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"\nSuccess: '{new_task}' has been added to your task manager!\n")
    else:
        print("\nError: Task Name Cannot Be Blank!\n")   
    
    
def complete_task():
    if not tasks:
        print("\nThere are no tasks to complete.")
        return
    
    view_tasks()
    
    try:
        completed_task = int(input("Enter the task number to complete: "))
    except ValueError:
        print("Please enter a valid task number")
        return
    
    if 1 <= completed_task <= len(tasks):
        completed_task = tasks.pop(completed_task - 1)
        save_tasks(tasks)
        print(f"\nSuccess: '{completed_task}' has been completed and removed from your task manager!\n")
    else:
        print("\nError: Please select a valid task number.\n")

    
    
def delete_task():
    if not tasks:
        print("\nThere are no tasks to delete.")
        return
    
    view_tasks()
    
    try:
        deleted_task = int(input("Enter the task number to delete: "))
    except ValueError:
        print("Please enter a valid task number")
        return
    
    if 1 <= deleted_task <= len(tasks):
        deleted_task = tasks.pop(deleted_task - 1)
        save_tasks(tasks)
        print(f"\nSuccess: '{deleted_task}' has been removed from your task manager!\n")
    else:
        print("\nError: Please select a valid task number.\n")




def main():
   
    while True:
        print("==== TASK MANAGER ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit Program")
        print()
        
        choice = input("Select an option (1-5): ")
        
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid Selection. Please Try Again.\n")
        
if __name__ == "__main__":
    main()