# Main

from todo_operations import add_task, delete_task, view_tasks
from utils import clear_screen, get_user_input

def main():
    """
    Run the main loop for the to-do list application.

    The user can choose from options to add, delete, or view tasks, or to exit the app.
    """
    while True:
        # Clear the screen to keep things tidy
        clear_screen()
        
        # Display the menu
        print("Welcome to the To-Do List App!")
        print("1. View Tasks")
        print("2. Add a Task")
        print("3. Delete a Task")
        print("4. Exit")
        
        # Get the user’s choice
        choice = get_user_input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            # Show the list of tasks
            view_tasks()
            input("\nPress Enter to return to the menu...")
        
        elif choice == '2':
            # Prompt the user for the new task
            task = get_user_input("Enter the task description: ")
            add_task(task)  # Add the task to the list
            input("Press Enter to return to the menu...")
        
        elif choice == '3':
            # Show the tasks so the user knows what can be deleted
            view_tasks()
            try:
                task_number = int(get_user_input("Enter the task number to delete: "))
                delete_task(task_number)  # Attempt to delete the specified task
            except ValueError:
                # Handle non-integer input
                print("Please enter a valid number.")
            input("Press Enter to return to the menu...")
        
        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break
        
        else:
            # Inform the user of invalid input
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            input("Press Enter to return to the menu...")

# Start the app
if __name__ == "__main__":
    main()
