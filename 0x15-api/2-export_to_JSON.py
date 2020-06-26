#!/usr/bin/python3
"""
This script extracts information from the given API and saves it as
a JSON file
"""
import requests
import json
from sys import argv


if __name__ == "__main__":
    req = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                       format(argv[1]))
    employee_name = req.json().get('username')

    req = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                       format(argv[1]))
    data = req.json()

    new_dict = {}
    new_dict['{}'.format(argv[1])] = []
    for task in data:
        new_dict['{}'.format(argv[1])].append({
                 'task': task.get('title'),
                 'completed': task.get('completed'),
                 'username': employee_name
        })

    with open('{}.json'.format(argv[1]), 'w') as output:
        json.dump(new_dict, output)
