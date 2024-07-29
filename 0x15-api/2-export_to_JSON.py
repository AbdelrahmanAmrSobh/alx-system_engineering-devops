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
    with open(f'{id}.json', 'w') as file:
        employee = requests.get(urls[0], params={keys[0]: id}).json()[0]
        tasks = requests.get(urls[1], params={keys[1]: id}).json()
        tasks_formatted = []
        for task in tasks:
            tasks_formatted.append(dict({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": employee.get('name')
            }))
        file.write(f'{{"{id}": {tasks_formatted}}}')
