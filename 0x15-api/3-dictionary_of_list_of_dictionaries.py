#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import json
import requests
from sys import argv


def user():
    """get all users then call user todos to check
    if the user have todos then return the todos
    then the user function will format it to write in json file
    """
    users = requests.get("https://jsonplaceholder.typicode.com/users/")
    users = users.json()
    data = {}
    for user in users:
        id = user['id']
        username = user['username']
        todos = user_todos(id, username)
        if todos:
            data[id] = todos
    return data


def user_todos(user_id, name):
    """
    get all the todos of specific user
    """
    todos = requests.get("https://jsonplaceholder.typicode.com/todos/")
    todos = todos.json()
    data = []
    for todo in todos:
        if todo['userId'] == user_id:
            data.append(
                {
                    "username": name, "task": todo['title'],
                    "completed": todo['completed']
                    }
                )
    return data


def jsonf():
    """
    serilize data to json file
    """
    data = user()
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    jsonf()
