import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "tasks.json")


#-----------------------------
# DATA LAYER
#-----------------------------


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
        print("No Tasks Found")
        return
    
    for task in tasks:
        status = "✓" if task["status"] == "done" else "•"
        print(f"{task['id']}. [{status}] {task['taks']}")
    
    print("---------------------\n")
    
tasks = load_tasks()
    
def add_task():
    task_text = input("Enter a New Task: ").strip()
    
    if not task_text:
        print("Task Cannot Be Blank")
        return
    
    new_task = {
        "id": get_next_id(tasks),
        "task": task_text,
        "status": "pending"
    }   
    
    tasks.append(new_task)
    save_tasks(tasks)
    
    print(f"Added: {task_text}")
    
def complete_task(tasks):
    view_tasks()
    
    try:
        task_id = int(input("Enter Task ID to Complete: "))
    except ValueError:
        print("Invalid Input.")
        return
    
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            save_tasks(tasks)
            print(f"Completed: {task['task']}")
            return

    print("Task Not Found.")
    
    
def delete_task(tasks):
    view_tasks(tasks)
    
    try:
        task_id = int(input("Enter Task ID to Delete: "))
    except ValueError:
        print("Invalid Input")
        return tasks
    
    tasks = [task for task in tasks if task["id"] != task_id]
    
    save_tasks(tasks)
    print("Task Deleted")
        
        

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def main():
    tasks = load_tasks()
   
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
            view_tasks(tasks)
        elif choice == "2":
            tasks = add_task(tasks)
        elif choice == "3":
            tasks = complete_task(tasks)
        elif choice == "4":
            tasks = delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid Selection. Please Try Again.\n")
        
if __name__ == "__main__":
    main()