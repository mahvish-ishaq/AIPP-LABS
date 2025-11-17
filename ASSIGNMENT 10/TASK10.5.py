#TASK 5 - Code Review on Error Handling

def divide_numbers(a, b):
    """
    Divide two numbers and return the result.

    This function safely handles division by zero using a try-except block.
    If the denominator is zero, it returns an error message instead of 
    crashing the program.

    Args:
        a (float): Numerator
        b (float): Denominator

    Returns:
        float or str: Result of division, or an error message if division 
        by zero occurs.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."


# ----- Test -----
print(divide_numbers(10, 0))
