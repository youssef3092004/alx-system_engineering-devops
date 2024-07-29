#!/usr/bin/python3
"""
Module to fetch and display employee TODO list progress using a REST API.
"""

import json
import requests
import sys


def fetch_todo_list():
    """
    Fetches TODO list progress for all employees from the JSONPlaceholder API
    and writes the data to a JSON file named 'todo_all_employees.json'.
    """
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()
    todo_all = {}

    for user in users:
        task_list = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                task_dict = {"username": user.get('username'),
                             "task": task.get('title'),
                             "completed": task.get('completed')}
                task_list.append(task_dict)
        todo_all[user.get('id')] = task_list

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todo_all, f)


if __name__ == "__main__":
    fetch_todo_list()
