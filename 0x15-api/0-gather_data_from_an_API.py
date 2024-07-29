#!/usr/bin/python3
"""
Script that is used to get data from api
and display this data
"""
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    urls = ['https://jsonplaceholder.typicode.com/users',
            'https://jsonplaceholder.typicode.com/todos']
    keys = ['id', 'userId']
    employee = requests.get(urls[0], {keys[0]: id}).json()[0].get('name')
    tasks = requests.get(urls[1], params={keys[1]: id}).json()
    completed_tasks = [task for task in tasks if task.get('completed') is True]
    print(f'Employee {employee} is done with tasks', end='')
    print(f'({len(completed_tasks)}/{len(tasks)}):')
    for completed_task in completed_tasks:
        print(f'\t {completed_task.get('title')}')
