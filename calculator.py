# calculator.py
# calculator project 
# student :omnia

def add(a, b):
    """
    Addition function
    Returns the sum of two numbers 
    """
    return a + b


def subtract(a, b):
    """
    Subtraction
    Returns the difference between two numbers 
    """
    return a - b


def multiply(a, b):
    """
    Multiplication function
    Returns the product of two numbers 
    """
    return a * b


def divide(a, b):
    """
    Division function
    Returns the result of dividing the 
    First number by second number 
    """
    if b == 0:
        return "Division by zero is not allowed"
    return a / b
