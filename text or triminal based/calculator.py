print("This is a calculator")

# Add function
def add(x, y):
    return x + y

# Subtract function 
def subtract(x, y):
    return x - y

# Multiply function
def multiply(x, y):
    return x * y

# Divide function with error check for division by zero
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Main calculator function 
def calculator():
    while True:
        # Loop until the user inputs a valid operator
        while True:
            print("\nSelect operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")

            choice = input("Enter choice (1/2/3/4): ")

            if choice in ['1', '2', '3', '4']:
                break  # Break the loop if a valid operator is selected
            else:
                print("Invalid input! Please select a valid operation (1/2/3/4).")

        # Prompt user for numbers after valid operation selection
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
            
        next_calculation = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if next_calculation not in ['yes', 'y']:
            break

# Run the calculator
calculator()
