#!/usr/bin/python3
"""export to JSON"""

import json
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    all_tasks = requests.get(f"{base_url}/todos").json()
    all_emp = dict()

    for task in all_tasks:
        resp = requests.get(f"{base_url}/users/{task.get('userId')}")
        username = resp.json().get("username")
        print(username)
        details = {
            "username": username,
            "task": task.get("title"),
            "completed": task.get("completed"),
            }
        user = task.get("userId")

        tmp = all_emp.get(f"{user}", list())
        tmp.append(details)

        all_emp[f"{user}"] = tmp
        print(all_emp)

    with open(f"todo_all_employees.json", "w") as f:
        json.dump(all_emp, f)
