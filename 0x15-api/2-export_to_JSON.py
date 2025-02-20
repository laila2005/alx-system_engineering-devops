#!/usr/bin/python3
"""Fetch employee TODO list progress and export to JSON."""
import json
import requests
import sys


def export_to_json(employee_id):
    """Export employee's TODO list data to a JSON file."""
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos"
        f"?userId={employee_id}"
    )

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200:
        print("Employee not found")
        sys.exit(1)

    user = user_response.json()
    todos = todos_response.json()

    username = user.get("username")
    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        for task in todos
    ]

    filename = f"{employee_id}.json"
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump({employee_id: tasks}, file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./1-export_to_JSON.py <employee_id>")
        sys.exit(1)

    export_to_json(int(sys.argv[1]))
