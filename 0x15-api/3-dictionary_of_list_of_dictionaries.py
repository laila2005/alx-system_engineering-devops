#!/usr/bin/python3
"""Fetch all employees' TODO list progress and export to JSON."""
import json
import requests


def export_all_to_json():
    """Export all employees' TODO list data to a JSON file."""
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    if users_response.status_code != 200 or todos_response.status_code != 200:
        print("Failed to fetch data")
        return

    users = users_response.json()
    todos = todos_response.json()

    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos if task.get("userId") == user_id
        ]
        all_tasks[user_id] = user_tasks

    filename = "todo_all_employees.json"
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(all_tasks, file, indent=4)


if __name__ == "__main__":
    export_all_to_json()
