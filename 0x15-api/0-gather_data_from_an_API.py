#!/usr/bin/python3
"""
Given an employee ID, this script returns information about his/her TODO list
progress.
"""

import requests
import sys


def get_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress of a specified employee.

    Args:
        employee_id (int): The ID of the employee whose TODO list progress is
        to be fetched.

    Returns:
        None
    """
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(f"{url}users/{employee_id}")
    todos_response = requests.get(f"{url}todos?userId={employee_id}")

    user_data = user_response.json()
    todos_data = todos_response.json()

    name = user_data.get('name')
    completed_tasks = [task.get('title') for task in todos_data
                       if task.get('completed')]
    total_tasks = len(todos_data)

    print(f"Employee {name} is done with tasks({len(completed_tasks)}/"
          f"{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
