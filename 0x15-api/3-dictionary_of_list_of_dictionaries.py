#!/usr/bin/python3
"""
This script fetches information about the TODO list progress of an employee
using the JSONPlaceholder REST API and displays it to the standard output.
"""


import json
import requests
import sys


def fetch_todo_list_progress():
    """Fetch and print the TODO list progress for all employees"""

    # Endpoints for user information
    user_url = f"https://jsonplaceholder.typicode.com/users"

    # Fetch the user information
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"User with ID {employee_id} not found.")
        return

    # Extract the JSON content
    user_data = user_response.json()

    all_users_tasks = {}

    for user in user_data:
        employee_id = user['id']
        employee_username = user['username']
        todos_url = (
                f"https://jsonplaceholder.typicode.com/todos"
                f"?userId={employee_id}"
        )
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()
        # Process and export the data in the required format
        tasks = [
            {
                "username": employee_username,
                "task": task['title'],
                "completed": task['completed'],
            } for task in todos_data
        ]
        all_users_tasks[employee_id] = tasks

    # Export to json
    json_filename = f"todo_all_employees.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(all_users_tasks, json_file)


def main():
    """
    Main function that parses command line argument
    and calls the fetching function.
    """
    fetch_todo_list_progress()


if __name__ == "__main__":
    main()
