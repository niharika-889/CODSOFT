
import json
import os

Filename="tasks.json"

def load_tasks():
    if os.path.exists(Filename):
        with open(Filename,"r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(Filename,"w") as file:
        json.dump(tasks,file,indent=4)

def view_tasks(tasks):
    if not tasks:
        print("\n No tasks yet!")
    else:
        print("\n Your tasks")
        for i,task in enumerate(tasks,start=1):
             status="Done" if task['done'] else  "not done"
             print(f"{i}.{task['title']} [{status}]")


def add_task(tasks):
    title = input("Enter task title: ")
    task = {"title": title, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")
def mark_done(tasks):
    view_tasks(tasks)
    try:
        index=int(input("\n Enter task number to mark as done:"))
        if 1<= index <=len(tasks):
            tasks[index-1]['done']=True
            save_tasks(tasks)
            print("Task marked as done!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        index=int(input("Enter task number to delete"))
        if 1<= index <= len(tasks):
            removed=tasks.pop(index-1)
            save_tasks(tasks)
            print(f"deleted: '{removed['title']}'")
        else:
            print("Invalid task number:")
    except ValueError:
        print("Please enter a valid number!")

def show_menu():
    print("\n TO-DO LIST MENU:")
    print("1.View tasks")
    print("2.Add task")
    print("3.mark task as done")
    print("4.Delete task")
    print("5.Exit")

def main():
    tasks=load_tasks()
    while True:
        show_menu()
        choice=input("Enter your choice(1-5):")
        if choice=='1':
            view_tasks(tasks)
        elif choice=='2':
            add_task(tasks)
        elif choice=='3':
            mark_done(tasks)
        elif choice=='4':
            delete_task(tasks)
        elif choice=='5':
            print("Tasks saved successfully")
            break
        else:
            print("Invalid choice!")

if __name__=="__main__":
    main()

