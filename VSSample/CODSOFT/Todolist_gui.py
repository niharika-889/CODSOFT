import tkinter as tk
from tkinter import messagebox
import json
import os

TASKS_FILE = "tasks.json"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.tasks_listbox = tk.Listbox(root, width=50, height=10)
        self.tasks_listbox.pack(pady=10)

        self.done_button = tk.Button(root, text="Mark as Done", command=self.mark_done)
        self.done_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            tasks = self.tasks_listbox.get(0, tk.END)
            if task in tasks:
                messagebox.showwarning("Duplicate Task", "This task already exists!")
            else:
                self.tasks_listbox.insert(tk.END, task)
                self.task_entry.delete(0, tk.END)
                self.save_tasks()
        else:
            messagebox.showwarning("Empty Task", "Please enter a task!")

    def delete_task(self):
        selected = self.tasks_listbox.curselection()
        if selected:
            self.tasks_listbox.delete(selected)
            self.save_tasks()

    def mark_done(self):
        selected = self.tasks_listbox.curselection()
        if selected:
            task = self.tasks_listbox.get(selected)
            if not task.endswith(" ✔"):
                self.tasks_listbox.delete(selected)
                self.tasks_listbox.insert(selected, task + " ✔")
                self.save_tasks()

    def save_tasks(self):
        tasks = self.tasks_listbox.get(0, tk.END)
        with open(TASKS_FILE, "w") as f:
            json.dump(tasks, f)

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as f:
                tasks = json.load(f)
                for task in tasks:
                    self.tasks_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()