#!/usr/bin/python3
'''
extend your Python script to export data in the JSON format
'''

import json
import requests
import sys


def fetch_user_data():
    '''
    Records all tasks from all employees
    '''
    url = "https://jsonplaceholder.typicode.com/"

    user_request = requests.get(url + "users")
    users = user_request.json()

    data_to_export = {}

    for user in users:
        user_id = user["id"]

        todos_request = requests.get(url + f"todos?userId={user_id}")
        todos = todos_request.json()

        data_to_export[user_id] = []

        for todo in todos:
            user_info = {
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": user.get("username")
            }
            data_to_export[user_id].append(user_info)

    return data_to_export


if __name__ == "__main__":
    data_to_export = fetch_user_data()

    with open("todo_all_employees.json", "w") as filejson:
        json.dump(data_to_export, filejson, indent=4)
