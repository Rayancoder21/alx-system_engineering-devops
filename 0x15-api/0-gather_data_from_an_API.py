#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import requests
import sys


if __name__ ==" __main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id))
    name = user.json().get('name')
    todos = requests.get(url + "todos")
    totalTasks = 0
    completed = 0

    for task in todos.json():
        if task.get('userId') == int(userId):
            totalTasks += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('employee_id') == int(employee_id) and task.get('completed')]))
