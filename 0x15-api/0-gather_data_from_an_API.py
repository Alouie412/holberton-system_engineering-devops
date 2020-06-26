#!/usr/bin/python3
"""
This script extracts information from the given API and prints out the list of
completed tasks by employee ID
"""
import requests
from sys import argv


if __name__ == "__main__":
    completed = 0
    total_tasks = 0

    req = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                       format(argv[1]))
    employee_name = req.json().get('name')

    req = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                       format(argv[1]))
    data = req.json()

    for task in data:
        total_tasks += 1
        if task.get('completed') is True:
            completed += 1

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          completed,
                                                          total_tasks))
    for task in data:
        if task.get('completed') is True:
            print("\t {}".format(task.get('title')))
