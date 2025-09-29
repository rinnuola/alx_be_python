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
    # Example usage
    result = perform_operation(10, 5, "add")
    print(result)   # should print 15
