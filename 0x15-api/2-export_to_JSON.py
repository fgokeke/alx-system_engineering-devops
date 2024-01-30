#!/usr/bin/python3
"""
This script fetches information about the TODO list progress of an employee
using the JSONPlaceholder REST API and displays it to the standard output.
"""


import json
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

    # Get employee name
    employee_name = user_data.get('name')
    employee_username = user_data.get('username')

    # Process and export the data in the required format
    tasks = [
        {
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_username,
        } for task in todos_data
    ]
    user_tasks = {employee_id: tasks}

    # Export to json
    json_filename = f"{employee_id}.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(user_tasks, json_file)


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
