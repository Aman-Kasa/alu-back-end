#!/usr/bin/python3
"""
Script to export TODO progress of an employee to a CSV file.
"""

import csv
import requests
import sys


def export_todo_to_csv(employee_id):
    """
    Fetches TODO list for a given employee ID and exports it to a CSV file.

    :param employee_id: ID of the employee whose TODO list will be fetched.
    """
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
        employee_username = (
            employee_data.get('username', 'Unknown User')
        )
        csv_filename = f"{employee_id}.csv"

        with open(csv_filename, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for task in todo_data:
                writer.writerow([
                    employee_id,
                    employee_username,
                    task.get('completed', False),  # Use .get() for safety
                    task.get('title', 'No Title')   # Use .get() for safety
                ])

        print(f"Data has been exported to {csv_filename}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            export_todo_to_csv(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")
