#!/usr/bin/python3
"""export yo CSV"""

import requests
import sys


if __name__ == "__main__":
    """get data from api"""
    userId = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{base_url}/users/{userId}").json()
    user_name = user.get('name')

    all_tasks = requests.get(f"{base_url}/todos").json()
    user_tasks = list(filter(lambda x: x.get("userId") == userId, all_tasks))

    with open(f"{userId}.csv", "w") as f:
        for task in user_tasks:
            state = task.get("completed")
            title = task.get("title")
            f.write(f'\"{userId}\",\"{user_name}\",\"{state}\",\"{title}\"\n"')
