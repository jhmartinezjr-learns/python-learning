tasks = ["Build GUI Prototype", "Review Budget Metrics"]

def view_tasks():
    print("\n--- Current Active Tasks ---")
    if not tasks:
        print("Your task list is empty!")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    print("----------------------------\n")
    
def add_task():
    new_task = input("Enter a New Task: ")
    if new_task:
        tasks.append(new_task)
        print(f"Success: '{new_task}' has been added to your task manager!\n")
    else:
        print("\nError: Task Name Cannot Be Blank!\n")
    
def delete_task():
    view_tasks()
    
def complete_task():
    view_tasks()

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