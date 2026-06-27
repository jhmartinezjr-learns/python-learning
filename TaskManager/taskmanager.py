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
    new_task = input("Enter a New Task: ").strip()
    if new_task:
        tasks.append(new_task)
        print(f"\nSuccess: '{new_task}' has been added to your task manager!\n")
    else:
        print("\nError: Task Name Cannot Be Blank!\n")
    
    
def complete_task():
    if not tasks:
        print("\nThere are no tasks to complete.")
        return
    
    view_tasks()
    
    try:
        task_number = int(input("Enter the task number to complete: "))
    except ValueError:
        print("Please enter a valid task number")
    
    if 1 <= task_number <= len(tasks):
        task_number = tasks.pop(task_number - 1)
        print(f"\nSuccess: '{task_number}' has been completed and removed from your task manager!\n")
    else:
        print("\nError: Please select a valid task number.\n")
        return
    
def delete_task():
    if not tasks:
        print("\nThere are no tasks to delete.")
        return
    
    view_tasks()
    
    try:
        task_number = int(input("Enter the task number to complete: "))
    except ValueError:
        print("Please enter a valid task number")
    
    if 1 <= task_number <= len(tasks):
        task_number = tasks.pop(task_number - 1)
        print(f"\nSuccess: '{task_number}' has been removed from your task manager!\n")
    else:
        print("\nError: Please select a valid task number.\n")
        return
 

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