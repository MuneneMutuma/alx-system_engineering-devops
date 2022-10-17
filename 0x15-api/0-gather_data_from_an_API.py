#!/usr/bin/python3
"""a Python script that, using this REST API, for a given
employee ID, returns information about his/her TODO list progress."""

import requests
import sys


def get_data():
    """get data from api"""
    userId = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{base_url}/users/?id={userId}").json()
    tasks = requests.get(f"{base_url}/todos/?userId={userId}").json()
    completed_tasks = 0
    for task in tasks:
        if task.get("completed"):
            completed_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(
                user[0].get('name'), completed_tasks, len(tasks)),
          file=sys.stdout)
    for task in tasks:
        if task["completed"]:
            print(f"\t {task.get('title')}",
                  file=sys.stdout)


if __name__ == "__main__":
    get_data()
