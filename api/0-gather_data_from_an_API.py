#!/usr/bin/python3
"""Script to fetch and display TODO list progress of a given employee ID."""

import requests
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is passed
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {__file__} employee_id(int)")
        sys.exit(1)

    # API Base URL
    API_URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = sys.argv[1]

    try:
        # Fetch employee details
        user_response = requests.get(f"{API_URL}/users/{EMPLOYEE_ID}")
        user_data = user_response.json()

        # Fetch employee's TODO list
        todos_response = requests.get(f"{API_URL}/todos?userId={EMPLOYEE_ID}")
        todos_data = todos_response.json()

        # Get employee name
        employee_name = user_data.get("name")

        # Get completed tasks and all tasks
        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task["completed"]]
        total_done_tasks = len(done_tasks)

        # Print output
       print(f"Employee {employee_name} is done with tasks("
    f"{total_done_tasks}/{total_tasks}):")
        for task in done_tasks:
            print(f"\t {task['title']}")

    except Exception as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)
