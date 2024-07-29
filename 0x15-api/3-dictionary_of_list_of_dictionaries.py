"""
	Script that is used to get data from api
	and display this data
"""
import requests

if __name__ == "__main__":
	with open('todo_all_employees.json', 'w') as file:
		urls = ['https://jsonplaceholder.typicode.com/users',
			'https://jsonplaceholder.typicode.com/todos']
		employees = requests.get(urls[0]).json()
		employees_dict = {}
		for employee in employees:
			id = str(employee.get('id'))
			tasks = requests.get(urls[1], params={'userId': id}).json()
			tasks_formatted = []
			for task in tasks:
				tasks_formatted.append(dict({
					"username": employee.get('username'),
					"task": task.get('title'),
					"completed": task.get('completed')
				}))
			employees_dict.update({id: tasks_formatted})
		file.write(employees_dict.__str__())
			
