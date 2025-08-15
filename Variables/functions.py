"""
We will use this file to learn about function in Python in details. We will cover the following basic and advanced topics:
# 1. Function Definition: How to define a function using the `def` keyword.
# 2. Function Parameters: How to pass parameters to a function.
# 3. Return Values: How to return values from a function using the `return`
#    statement.
# 4. Function Scope: Understanding local and global variables within functions.
# 5. Default Parameters: How to set default values for function parameters.
# 6. Variable-Length Arguments: Using `*args` and `**kwargs` to accept variable-length arguments.
# 7. Lambda Functions: Creating anonymous functions using the `lambda`
#    keyword.
# 8. Higher-Order Functions: Functions that take other functions as arguments or return functions
#    as results.
# 9. Decorators: How to modify the behavior of a function using decorators.
# 10. Recursion: How to define and use recursive functions.
# 11. Function Annotations: Adding metadata to function parameters and return values.
# 12. Function Documentation: Writing docstrings to document functions.
# 13. Function Type Hints: Using type hints to specify the expected types of function parameters and return values.
"""


# 1. Function Definition
def greet(name):
    """Function to greet a person."""
    print(f"Hello, {name}!")


# Example usage
greet("Alice")  # Output: Hello, Alice!


# 2. Function Parameters
def add(a, b):
    """Function to add two numbers."""
    return a + b


# Example usage
result = add(5, 3)
print(f"Sum: {result}")  # Output: Sum: 8


# 3. Return Values
def multiply(a, b):
    """Function to multiply two numbers."""
    return a * b


# Example usage
product = multiply(4, 2)
print(f"Product: {product}")  # Output: Product: 8


# 4. Function Scope
def outer_function():
    """Outer function with a nested inner function."""
    outer_var = "I am from outer function"

    def inner_function():
        """Inner function accessing outer variable."""
        print(outer_var)

    inner_function()  # Call the inner function


# Example usage
outer_function()  # Output: I am from outer function


# 5. Default Parameters
def greet_with_default(name="Guest"):
    """Function to greet a person with a default name."""
    print(f"Hello, {name}!")


# Example usage
greet_with_default()  # Output: Hello, Guest!
greet_with_default("Bob")  # Output: Hello, Bob!


# 6. Variable-Length Arguments
def variable_length_args(*args):
    """Function to accept variable-length arguments."""
    print("Arguments:", args)


# Example usage
variable_length_args(1, 2, 3)  # Output: Arguments: (1, 2, 3)
variable_length_args("a", "b", "c")  # Output: Arguments: ('a', 'b', 'c')


def variable_length_kwargs(**kwargs):
    """Function to accept variable-length keyword arguments."""
    print("Keyword Arguments:", kwargs)


# Example usage
variable_length_kwargs(
    name="Alice", age=30
)  # Output: Keyword Arguments: {'name': 'Alice', 'age': 30}
variable_length_kwargs(
    city="New York", country="USA"
)  # Output: Keyword Arguments: {'city': 'New York', 'country': 'USA'}


# 7. Lambda Functions
def square(x):
    """Function to return the square of a number."""
    return x**2


# Example usage
square_result = square(5)
print(f"Square: {square_result}")  # Output: Square: 25
# Lambda function to return the square of a number
square_lambda = lambda x: x**2
# Example usage
square_lambda_result = square_lambda(5)
print(f"Square (Lambda): {square_lambda_result}")  # Output: Square (Lambda): 25


# 8. Higher-Order Functions
def apply_function(func, value):
    """Function to apply a given function to a value."""
    return func(value)


# Example usage
result = apply_function(square, 4)
print(
    f"Result of applying function: {result}"
)  # Output: Result of applying function: 16


# 9. Decorators
def decorator_function(func):
    """Decorator function to modify the behavior of another function."""

    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")

    return wrapper


# Example usage
@decorator_function
def say_hello():
    """Function to say hello."""
    print("Hello!")


# Calling the decorated function
say_hello()  # Output: Before calling the function
# Hello!
# After calling the function


# 10. Recursion
def factorial(n):
    """Recursive function to calculate the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Example usage
fact_result = factorial(5)
print(f"Factorial: {fact_result}")  # Output: Factorial: 120


# 11. Function Annotations
def add_with_annotations(a: int, b: int) -> int:
    """Function to add two numbers with type annotations."""
    return a + b


# Example usage
annotated_result = add_with_annotations(3, 4)
print(f"Annotated Result: {annotated_result}")  # Output: Annotated Result: 7


# 12. Function Documentation
def multiply_with_docstring(a, b):
    """
    Function to multiply two numbers.

    Parameters:
    a (int): First number.
    b (int): Second number.

    Returns:
    int: Product of a and b.
    """
    return a * b


# Example usage
docstring_result = multiply_with_docstring(2, 3)
print(f"Docstring Result: {docstring_result}")  # Output: Docstring Result: 6


# 13. Function Type Hints
def divide(a: float, b: float) -> float:
    """
    Function to divide two numbers with type hints.

    Parameters:
    a (float): Numerator.
    b (float): Denominator.

    Returns:
    float: Result of division.
    """
    return a / b


# Example usage
type_hinted_result = divide(10.0, 2.0)
print(f"Type Hinted Result: {type_hinted_result}")  # Output: Type Hinted Result: 5.0
