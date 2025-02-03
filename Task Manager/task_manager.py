import os
from datetime import datetime

#File to store tasks
FILE_NAME = "tasks.txt"

#Load tasks from file
def load_tasks():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task_id, task_name, creation_date, status = line.strip().split(" | ")
                tasks[int(task_id)] = {
                    "name": task_name,
                    "creation_date": creation_date,
                    "status": status
                }
    return tasks

#Save tasks in file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} | {task['name']} | {task['creation_date']} | {task['status']}\n")

#Adding new tasks
def add_task(tasks):
    title = input("Enter task title: ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"name": title, "creation_date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "status": "Pending"}
    print(f"Task '{title}' added successfully.")

#View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for task_id, task in tasks.items():
            print(f"Task {task_id}: {task['name']} | ({task['status']}) | created on {task['creation_date']}")

#Mark task as complete
def mark_complete(tasks):
    task_id = int(input("Enter task ID: "))
    if task_id in tasks:
        tasks[task_id]["status"] = "Completed"
        print(f"Task {task_id} marked as completed.")
    else:
        print("Task not found.")

#Delete task as complete
def delete_task(tasks):
    task_id = int(input("Enter task ID: "))
    if task_id in tasks:
        del tasks[task_id]
        print(f"Task {task_id} deleted.")
    else:
        print("Task not found.")

#main menu
def main():
    tasks = load_tasks()
    while True:
        print("1. Add new task")
        print("2. View all tasks")
        print("3. Mark task as complete")
        print("4. Delete task")
        print("5. Exit")
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            mark_complete(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            break

main()