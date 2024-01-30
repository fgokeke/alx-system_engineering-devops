#!/usr/bin/python3
"""
This script fetches information about the TODO list progress of an employee
using the JSONPlaceholder REST API and displays it to the standard output.
"""


import csv
import requests
import sys


def fetch_todo_list_progress(employee_id):
    """Fetch and print the TODO list progress for a given employee ID."""
    # Make sure the employee ID is an integer
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        return

    # Endpoints for user information and TODOs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos"
        f"?userId={employee_id}"
    )

    # Fetch the user information
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"User with ID {employee_id} not found.")
        return

    # Fetch the TODOs
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Could not fetch TODOs for user with ID {employee_id}.")
        return

    # Extract the JSON content
    user_data = user_response.json()
    todos_data = todos_response.json()

    # Calculate TODO progress
    employee_name = user_data.get('name')
    total_tasks = len(todos_data)
    completed_tasks = len([task for task in todos_data if task['completed']])

    # Output the TODO list progress
    print(
        f"Employee {employee_name} is done with "
        f"tasks({completed_tasks}/{total_tasks}): "
    )
    for task in todos_data:
        if task['completed']:
            print(f"\t {task['title']}")

    # Export to CSV
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                employee_id,
                employee_name,
                task['completed'],
                task['title']
            ])


def main():
    """
    Main function that parses command line argument
    and calls the fetching function.
    """
    if len(sys.argv) < 2:
        return
    employee_id = sys.argv[1]
    fetch_todo_list_progress(employee_id)


if __name__ == "__main__":
    main()
