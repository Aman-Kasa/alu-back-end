#!/usr/bin/python3
"""Script to export employee tasks to a CSV file."""

import csv
import requests
import sys

def export_to_csv(employee_id):
    """Export employee tasks to CSV."""
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data from API")
        return

    todos = response.json()

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print("Error fetching user data from API")
        return

    user = user_response.json()
    username = user.get('username')

    filename = f"{employee_id}.csv"
    
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            csv_writer.writerow([
                employee_id,
                username,
                todo['completed'],
                todo['title']
            ])

    print(f"Data exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py employee_id(int)")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_to_csv(employee_id)
    except ValueError:
        print("Invalid employee ID. It must be an integer.")
