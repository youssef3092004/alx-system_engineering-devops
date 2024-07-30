#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import json
import requests
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    url = "https://jsonplaceholder.typicode.com/todos/"
    todo = requests.get(url=url).json()
    user = requests.get(url=f"https://jsonplaceholder.typicode.com/users/{id}")
    user = user.json().get('username')
    data = {}
    datalist = []
    for toodo in todo:
        if str(toodo.get("userId")) == id:
            data["task"] = toodo.get("title")
            data["completed"] = toodo.get("completed")
            data["username"] = user
            datalist.append(dict(data))
    final = {f"{id}": datalist}
    with open(f"{id}.json", 'w') as jsonf:
        json.dump(final, jsonf)
