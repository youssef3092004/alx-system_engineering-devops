#!/usr/bin/python3
"""
Export employee TODO list data in CSV format.
"""

import csv
import requests
import sys


def export_to_csv(employee_id):
    """
    Fetches TODO list data for a specified employee and exports it to a CSV
    file.

    Args:
        employee_id (int): The ID of the employee whose TODO list data is to
        be fetched.

    Returns:
        None
    """
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(f"{url}users/{employee_id}")
    todos_response = requests.get(f"{url}todos?userId={employee_id}")

    user_data = user_response.json()
    todos_data = todos_response.json()

    username = user_data.get('username')
    with open(f"{employee_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([employee_id, username, task.get('completed'),
                             task.get('title')])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_to_csv(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
