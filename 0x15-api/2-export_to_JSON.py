#!/usr/bin/python3
"""export to JSON"""

import json
import requests
import sys


if __name__ == "__main__":
    userId = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{base_url}/users/{userId}").json()
    user_name = user.get('name')

    all_tasks = requests.get(f"{base_url}/todos").json()
    user_tasks = list(filter(lambda x: x.get("userId") == userId, all_tasks))

    data = list()
    for task in user_tasks:
        details = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user_name
            }
        data.append(details)

    data = {userId: data}

    with open(f"{userId}.json", "w") as f:
        json.dump(data, f)
