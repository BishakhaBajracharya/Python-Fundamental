def classify_number():
    while True:
        # Prompt the user to enter a number or type 'exit' to quit
        input_value = input("Enter a number to classify (or type 'exit' to quit): ")
        
        # Check if the user typed 'exit'
        if input_value.lower() == 'exit':
            print("Exiting the classification tool.")
            break  # Exit the loop and end the function
        
        try:
            # Convert the user input to a float number
            num = float(input_value)
            
            # Use if-elif-else statements to classify the number
            if num > 0:
                print(f"{num} is positive.")
            elif num < 0:
                print(f"{num} is negative.")
            else:
                print(f"{num} is zero.")
        
        except ValueError:
            # Handle invalid input (non-numeric input)
            print("Invalid input. Please enter a valid number.")

# Call the function to start the program
# classify_number() 