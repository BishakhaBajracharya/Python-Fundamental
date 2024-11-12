def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def calculator():
    while True:
        # Display available operations
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
         # Get the user's choice of operation
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        # If the user chooses addition
        if choice == '1':
            # Ask for two numbers to add
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            # Perform addition and display the result
            print(f"The sum of {x} and {y} is {add(x, y)}")

        # If the user chooses subtraction
        elif choice == '2':
            # Ask for two numbers to subtract
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            # Perform subtraction and display the result
            print(f"The difference when {y} is subtracted from {x} is {subtract(x, y)}")

        # If the user chooses multiplication
        elif choice == '3':
            # Ask for two numbers to multiply
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            # Perform multiplication and display the result
            print(f"The product of {x} and {y} is {multiply(x, y)}")

        # If the user chooses division
        elif choice == '4':
            # Ask for two numbers to divide
            x = float(input("Enter the numerator: "))
            y = float(input("Enter the denominator: "))
            # Perform division and display the result
            print(f"The result of dividing {x} by {y} is {divide(x, y)}")

        # If the user wants to classify a number as positive, negative, or zero
        elif choice == '5':
            while True:
                # Ask the user to enter a number to classify, or type 'exit' to return to the main menu
                number = input("Enter a number to classify (or type 'exit' to go back): ")
                
                # If the user types 'exit', break out of the classification loop and return to the main menu
                if number.lower() == 'exit':
                    break
                
                try:
                    # Convert the input to a float number
                    num = float(number)
                    
                    # Check if the number is positive, negative, or zero and print the result
                    if num > 0:
                        print(f"{num} is positive.")
                    elif num < 0:
                        print(f"{num} is negative.")
                    else:
                        print(f"{num} is zero.")
                except ValueError:
                    # Handle invalid input (if the user doesn't enter a valid number)
                    print("Invalid input, please enter a valid number.")
        
        # If the user chooses to exit the program
        elif choice == '6':
            print("Exiting the calculator. Goodbye!")
            break
        
        # If the user enters an invalid choice that doesn't correspond to any operation
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4/5/6).")

# Arithmetic functions (unchanged)
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # Handle division by zero
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

# Call the calculator function to start the program
calculator()