#!/usr/bin/python3
"""Exports data in the JSON format for all employees' TODO list progress."""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users")
    todos = requests.get(url + "todos")

    users = users.json()
    todos = todos.json()
    todo_all = {}

    for user in users:
        task_list = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                task_dict = {
                    "username": user.get('username'),
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                task_list.append(task_dict)
        todo_all[user.get('id')] = task_list

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todo_all, f)
