# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Create a dictionary to map operators to functions
operations = {
    '1': add,
    '2': subtract,
    '3': multiply,
    '4': divide
}

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take input from the user
choice = input("Enter choice (1/2/3/4):")

# Check if the choice is valid
if choice not in operations:
    print("Invalid Input")
else:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = operations[choice](num1, num2)
    print("Result:", result)