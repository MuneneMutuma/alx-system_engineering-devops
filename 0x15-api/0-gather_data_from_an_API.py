#!/usr/bin/python3
"""a Python script that, using this REST API, for a given
employee ID, returns information about his/her TODO list progress."""

import json
import requests
import sys


def get_data():
    """get data from api"""
    userId = sys.argv[1]
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/\
                          ?id={userId}").json()
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos/\
                          ?userId={}".format(userId)).json()
    completed_tasks = 0
    for task in tasks:
        if task["completed"]:
            completed_tasks += 1

    print(f"Employee {user[0]['name']} is done with tasks\
            ({completed_tasks}/{len(tasks)}):")
    for task in tasks:
        if task["completed"]:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    get_data()
