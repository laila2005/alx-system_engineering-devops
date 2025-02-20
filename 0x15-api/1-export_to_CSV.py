#!/usr/bin/python3
"""
Script that exports an employee's TODO list to a CSV file.
"""

import csv
import sys
import requests


def export_to_csv(employee_id):
    """
    Fetches an employee's TODO list and saves it as a CSV file.

    Args:
        employee_id (int): The ID of the employee.
    """
    user_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200:
        print("Employee not found")
        sys.exit(1)

    user = user_response.json()
    todos = todos_response.json()

    username = user.get("username")
    filename = f"{employee_id}.csv"

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task["completed"],
                task["title"]
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./1-export_to_CSV.py  <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_csv(employee_id)
