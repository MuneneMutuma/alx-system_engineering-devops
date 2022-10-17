#!/usr/bin/python3
"""a Python script that, using this REST API, for a given
employee ID, returns information about his/her TODO list progress."""

import requests
import sys


if __name__ == "__main__":
    """get data from api"""
    userId = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{base_url}/users/{userId}").json()
    all_tasks = requests.get(f"{base_url}/todos").json()

    user_tasks = list(filter(lambda x: x.get("userId") == userId, all_tasks))
    completed = list(filter(lambda x: x.get("completed"), user_tasks))

    user_name = user.get('name')
    print("Employee {} is done with tasks({}/{}):".format(
            user_name, len(completed), len(user_tasks)),
          file=sys.stdout)
    for task in completed:
        print(f"\t {task.get('title')}", file=sys.stdout)
