# Utils

import os

def clear_screen():
    """
    Clear the console screen.
    
    This function checks the operating system to run the correct command for clearing the screen.
    """
    # Use 'cls' for Windows and 'clear' for other systems (e.g., MacOS, Linux)
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input(prompt):
    """
    Get input from the user with a custom prompt.
    
    Parameters:
    - prompt (str): The message shown to the user to guide input.

    Returns:
    - str: The user's input as a string.
    """
    return input(prompt)  # Prompt the user and return their input