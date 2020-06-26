#!/usr/bin/python3
"""
This script extracts information from the given API and saves it as
a csv file
"""
import requests
import csv
from sys import argv


if __name__ == "__main__":
    completed = 0
    total_tasks = 0

    req = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                       format(argv[1]))
    employee_name = req.json().get('username')

    req = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                       format(argv[1]))
    data = req.json()

    with open('{}.csv'.format(argv[1]), mode='w') as csv_file:
        write_to_csv = csv.writer(csv_file, delimiter=',', quotechar='"',
                                  quoting=csv.QUOTE_ALL)

        for task in data:
            write_to_csv.writerow([argv[1], employee_name,
                                  task.get('completed'),
                                  task.get('title')])
