#!/usr/bin/python3

"""
Script to fetch TODO progress of an employee from a REST API.
"""

import requests
import sys


def fetch_todo_progress(emp_id):
    """
    Fetches employee TODO list progress from a JSON API and prints it.

    :param emp_id: ID of the employee whose TODO list will be fetched
    """
    employee_url = (
        f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    )
    todo_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    )

    try:
        # Fetch employee data
        employee_response = requests.get(employee_url)
        if employee_response.status_code != 200:
            print("Error fetching employee data. "
                  "Please check the employee ID.")
            return

        # Fetch TODO data
        employee_data = employee_response.json()
        todo_response = requests.get(todo_url)
        if todo_response.status_code != 200:
            print("Error fetching TODO data. "
                  "Please check the API endpoint.")
            return

        # Process and display tasks
        todo_data = todo_response.json()
        employee_name = employee_data.get('name', 'Unknown Employee')
        total_tasks = len(todo_data)

        completed_tasks = [
            task for task in todo_data if task.get('completed', False)
        ]
        num_completed_tasks = len(completed_tasks)

        print(
            f"Employee {employee_name} is done with tasks "
            f"({num_completed_tasks}/{total_tasks}):"
            )
        # Print completed task titles in two lines
        task_titles = "\n".join(
            f"\t {task['title']}" for task in completed_tasks
        )
        print(task_titles)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 {__file__} <employee_id>")
        print("Please provide an employee ID.")
        sys.exit(1)
    else:
        try:
            employee_id = int(sys.argv[1])
            fetch_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")
