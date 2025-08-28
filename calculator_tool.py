def calculate(operation: str, a: int, b: int) -> str:
    """Perform basic arithmetic based on given operation and two numbers."""

    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            return "Error: Division by zero."
        result = a / b
    else:
        return "Error: Unknown operation."

    return f"Result: {result}"