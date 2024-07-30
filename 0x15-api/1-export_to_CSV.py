#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    url = "https://jsonplaceholder.typicode.com/todos/"
    todo = requests.get(url=url).json()
    user = requests.get(url=f"https://jsonplaceholder.typicode.com/users/{id}")
    user = user.json().get('username')
    data = []
    for toodo in todo:
        if str(toodo.get("userId")) == id:
            data.append((toodo.get("completed"), toodo.get("title")))

    for comp, title in data:
        with open(f"{id}.csv", 'a') as csvf:
            data = f'"{id}","{user}","{comp}","{title}"\n'
            csvf.write(data)
