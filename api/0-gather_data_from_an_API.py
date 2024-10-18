#!/usr/bin/python3
import requests
import sys

def gather_data(employee_id):
    # Get employee data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    # Check if the requests were successful
    if user_response.status_code != 200 or todo_response.status_code != 200:
        return None

    # Get the data in JSON format
    user_data = user_response.json()
    todo_data = todo_response.json()

    employee_name = user_data.get("name")
    total_tasks = len(todo_data)
    done_tasks = [task for task in todo_data if task.get("completed")]

    # Print progress
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        gather_data(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
