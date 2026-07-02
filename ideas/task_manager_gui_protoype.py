import tkinter as tk
from tkinter import ttk

class TaskManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Task Manager")
        self.root.geometry("450x550")
        
        # Heading
        header = tk.Label(root, text="Task Manager Menu", font=("Arial", 16, "bold"), pady=10)
        header.pack()
        
        # Track which option is currently expanded
        self.current_expanded = None
        self.frames = {}
        
        # Define the 5 options and their expanded descriptions
        self.options = {
            "1. View Active Tasks": "📝 [Task 1] Fix Python format specifier\n📝 [Task 2] Build GUI Prototype\n\nStatus: 2 Tasks Pending",
            "2. Add New Task": "➕ Enter Task Name:\n[ ____________________ ]\n\n[ Save Task Button ]",
            "3. Complete/Archive Task": "✅ Select a task to archive:\n- Fix Python format specifier\n\n[ Move to Archive ]",
            "4. View Performance Metrics": "📊 Budget Percentage Used: 50.0%\n📊 Total Billable Hours: 12 hrs\n📊 Monthly Efficiency: 94%",
            "5. System Settings": "⚙️ Notifications: ON\n⚙️ Theme: Dark Mode\n⚙️ Auto-Save: Enabled"
        }
        
        # Build the menu
        for title, details in self.options.items():
            self.create_accordion_item(title, details)

    def create_accordion_item(self, title, details):
        # Container frame for the header + detail section
        item_frame = tk.Frame(self.root, bd=1, relief="groove", pady=2)
        item_frame.pack(fill="x", padx=15, pady=5)
        
        # Clickable Header Button
        btn = tk.Button(
            item_frame, 
            text=f"▶  {title}", 
            font=("Arial", 11, "bold"), 
            anchor="w", 
            bg="#f0f0f0",
            relief="flat",
            command=lambda t=title: self.toggle_section(t)
        )
        btn.pack(fill="x")
        
        # Hidden Content Frame (Expands when clicked)
        content_frame = tk.Frame(item_frame, bg="white", padx=10, pady=10)
        lbl = tk.Label(content_frame, text=details, justify="left", bg="white", font=("Arial", 10))
        lbl.pack(anchor="w")
        
        # Save references to manipulate later
        self.frames[title] = {"frame": content_frame, "button": btn}

    def toggle_section(self, title):
        # If the clicked section is already open, collapse it
        if self.current_expanded == title:
            self.frames[title]["frame"].pack_forget()
            self.frames[title]["button"].config(text=f"▶  {title}", bg="#f0f0f0")
            self.current_expanded = None
        else:
            # Collapse the previously opened section if it exists
            if self.current_expanded:
                prev = self.current_expanded
                self.frames[prev]["frame"].pack_forget()
                self.frames[prev]["button"].config(text=f"▶  {prev}", bg="#f0f0f0")
            
            # Expand the newly clicked section
            self.frames[title]["frame"].pack(fill="x")
            self.frames[title]["button"].config(text=f"▼  {title}", bg="#e0e0e0")
            self.current_expanded = title

# Start the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerGUI(root)
    root.mainloop()