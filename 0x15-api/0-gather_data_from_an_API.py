#!/usr/bin/python3
'''  for a given employee ID, returns information about list progress. '''


if __name__ == '__main__':
    import requests
    import sys

    employee_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'
    url_user = base_url + 'users/{}'.format(employee_id)
    url_todo = base_url + 'todos'
    info_user = requests.get(url_user).json()
    all_todo = requests.get(url_todo).json()

    name = info_user.get('name')
    total_todo = 0
    done = 0
    tasks = []

    for todo in all_todo:
        if todo.get('userId') == int(employee_id):
            total_todo += 1
            if todo.get('completed') is True:
                done += 1
                tasks.append(todo.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format(
        name,
        done,
        total_todo))
    for task in tasks:
        print('\t', task)
