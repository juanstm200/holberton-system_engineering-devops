#!/usr/bin/python3
''' for an employee ID, gives its information. '''


import json
from urllib import request


if __name__ == "__main__":
    url_user = "https://jsonplaceholder.typicode.com/users"
    with request.urlopen(url_user) as response:
        users = json.loads(response.read().decode())
        data = {}
        for user in users:
            url_task = "https://jsonplaceholder.typicode.com/users/{}/todos"\
                    .format(user.get("id"))
            with request.urlopen(url_task) as response:
                tasks = json.loads(response.read().decode())
                with open("todo_all_employees.json", "w") as file:
                    list_task = []
                    for t in tasks:
                        list_task.append({
                            "username": user.get("username"),
                            "completed": t.get("completed"),
                            "task": t.get("title")
                        })
                    data[user.get("id")] = list_task
                    json.dump(data, file)
