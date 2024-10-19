#!/usr/bin/python3
"""
Script to export TODO tasks of an employee to a JSON file.
"""

import json
import requests
import sys


def export_todo_to_json(employee_id):
    """Export TODO tasks of a specific employee to a JSON file."""
    employee_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    todo_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )

    try:
        employee_response = requests.get(employee_url)
        if employee_response.status_code != 200:
            print("Error fetching employee data.")
            return
        employee_data = employee_response.json()

        todo_response = requests.get(todo_url)
        if todo_response.status_code != 200:
            print("Error fetching TODO data.")
            return
        todo_data = todo_response.json()

        employee_username = employee_data.get('username', 'Unknown User')
        tasks = [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": employee_username
            } for task in todo_data
        ]

        json_filename = f"{employee_id}.json"
        with open(json_filename, mode='w') as json_file:
            json.dump({employee_id: tasks}, json_file)

        print(f"Data has been exported to {json_filename}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            export_todo_to_json(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")
