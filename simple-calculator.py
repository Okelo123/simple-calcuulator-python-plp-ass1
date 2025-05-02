# Ask the user for two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Ask the user for an operation
operation = input("Choose an operation (+, -, *, /): ")

# Check and convert to appropriate types
# Try converting to float; if it fails, treat as strings
try:
    num1_converted = float(num1)
    num2_converted = float(num2)
    is_number = True
except ValueError:
    is_number = False

# Perform arithmetic or string operation
if is_number:
    if operation == "+":
        result = num1_converted + num2_converted
    elif operation == "-":
        result = num1_converted - num2_converted
    elif operation == "*":
        result = num1_converted * num2_converted
    elif operation == "/":
        if num2_converted != 0:
            result = num1_converted / num2_converted
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operation!"
else:
    # If not numbers, treat as strings and only allow addition
    if operation == "+":
        result = num1 + num2
    else:
        result = "Only + operation is allowed for strings!"

# Output the result
print(f"Result: {num1} {operation} {num2} = {result}")

# Show data types
print(f"\nData type of first input: {type(num1)}")
print(f"Data type of second input: {type(num2)}")
print(f"Data type of result: {type(result)}")
