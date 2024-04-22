#!/usr/bin/python3
'''
extend your Python script to export data in the JSON format
'''

import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    user_id = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(user_id))
    user = user_response.json()
    username = user.get("username")

    params = {"userId": user_id}
    todos_response = requests.get(url + "todos", params=params)
    todos = todos_response.json()

    data_to_export = {user_id: []}

    for todo in todos:
        user_info = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
        }
        data_to_export[user_id].append(user_info)

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
