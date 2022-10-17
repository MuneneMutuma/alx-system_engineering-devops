#!/usr/bin/python3
"""get data from API
"""

import requests
import sys


if __name__ == "__main__":
    """get data from api"""
    userId = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{base_url}/users/{userId}").json()
    user_tasks = requests.get(f"{base_url}/todos/?userId={userId}").json()

    completed = list(filter(lambda x: x.get("completed"), user_tasks))

    user_name = user.get('name')
    sys.stdout.write("Employee {} is done with tasks({}/{}):\n".format(
            user_name, len(completed), len(user_tasks)))
    for task in completed:
        sys.stdout.write(f"\t {task.get('title')}\n")
