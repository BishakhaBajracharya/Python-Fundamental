# Todo_operations

# This is the list where we'll store all of the to-do tasks.
tasks = []

def add_task(task):
    """
    Add a new task to the to-do list.

    Parameters:
    - task (str): The task description to be added.

    The function appends the provided task to the tasks list and
    prints a confirmation message.
    """
    tasks.append(task)  # Add the new task to the end of the list
    print(f"Task '{task}' added.")  # Confirm that the task was added

def delete_task(task_number):
    """
    Delete a task from the to-do list by its number.

    Parameters:
    - task_number (int): The position (1-based) of the task in the list to delete.

    The function attempts to remove the task at the specified position.
    If the task number is invalid (e.g., too high or too low), it informs the user.
    """
    try:
        # Remove the task by converting the user-provided 1-based number to a 0-based index
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' deleted.")  # Confirm the deletion
    except IndexError:
        # If task_number is out of range, print an error message
        print("Invalid task number.")

def view_tasks():
    """
    Display all tasks currently in the to-do list.

    If there are no tasks, inform the user that the list is empty.
    Otherwise, print each task with a number so that users can identify them.
    """
    if tasks:
        print("\nYour Tasks:")
        # Enumerate over tasks to provide each task with a 1-based index
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        # Inform the user if there are no tasks to show
        print("No tasks in the list.")