#!/usr/bin/python3
'''  Python script to export data in the CSV format. '''


if __name__ == '__main__':
    import requests
    import sys

    employee_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'
    url_user = base_url + 'users/{}'.format(employee_id)
    url_all = base_url + 'todos'
    info_user = requests.get(url_user).json()
    all = requests.get(url_all).json()

    username = info_user.get('username')

    with open('{}.csv'.format(employee_id), 'w+') as file:
        for todo in all:
            if todo.get('userId') == int(employee_id):
                line = ""
                line += '\"{}\"'.format(employee_id) + ","
                line += '\"{}\"'.format(username) + ","
                line += '\"{}\"'.format(todo.get('completed')) + ","
                line += '\"{}\"\n'.format(todo.get('title'))
                file.write(line)
