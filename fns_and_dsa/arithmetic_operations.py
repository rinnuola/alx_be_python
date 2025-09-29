def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations.
    Args:
        num1 (float): first number
        num2 (float): second number
        operation (str): 'add', 'subtract', 'multiply', or 'divide'
    Returns:
        float or str: result of operation, or error message
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero!"
        return num1 / num2
    else:
        return "Error: Invalid operation"


if __name__ == "__main__":
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")
