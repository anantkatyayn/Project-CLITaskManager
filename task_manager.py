import json
import os
from datetime import datetime
from tabulate import tabulate
import argparse

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    table = [
        [i + 1, task["title"], task["description"], task["due_date"], task["status"]]
        for i, task in enumerate(tasks)
    ]
    print(tabulate(table, headers=["ID", "Title", "Description", "Due Date", "Status"]))

def add_task(tasks, title, description, due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")  # Validate date
    except ValueError:
        print("Invalid date format. Task not added.")
        return
    tasks.append({"title": title, "description": description, "due_date": due_date, "status": "Pending"})
    save_tasks(tasks)
    print("Task added successfully!")

def complete_task(tasks, task_id):
    if task_id.isdigit() and 1 <= int(task_id) <= len(tasks):
        tasks[int(task_id) - 1]["status"] = "Completed"
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task ID.")

def delete_task(tasks, task_id):
    if task_id.isdigit() and 1 <= int(task_id) <= len(tasks):
        tasks.pop(int(task_id) - 1)
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task ID.")

def search_tasks(tasks, keyword):
    results = [task for task in tasks if keyword.lower() in task["title"].lower()]
    if results:
        list_tasks(results)
    else:
        print(f"No tasks found matching the keyword \"{keyword}\" ")

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    
    # Define command-line arguments
    parser.add_argument("--add", action="store_true", help="Add a new task")
    parser.add_argument("--list", action="store_true", help="List all tasks")
    parser.add_argument("--complete", type=str, help="Mark a task as complete by ID")
    parser.add_argument("--delete", type=str, help="Delete a task by ID")
    parser.add_argument("--search", type=str, help="Search tasks by keyword")
    
    # Arguments for adding a task
    parser.add_argument("--title", type=str, help="Title of the task")
    parser.add_argument("--description", type=str, help="Description of the task")
    parser.add_argument("--due_date", type=str, help="Due date of the task (YYYY-MM-DD)")

    args = parser.parse_args()
    tasks = load_tasks()

    if args.add:
        if args.title and args.description and args.due_date:
            add_task(tasks, args.title, args.description, args.due_date)
        else:
            print("To add a task, please provide --title, --description, and --due_date.")
    elif args.list:
        list_tasks(tasks)
    elif args.complete:
        complete_task(tasks, args.complete)
    elif args.delete:
        delete_task(tasks, args.delete)
    elif args.search:
        search_tasks(tasks, args.search)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
