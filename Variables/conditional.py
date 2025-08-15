"""
Here we will explore conditional statements in Python, which allow you to execute code based on certain conditions. Conditional statements are essential for controlling the flow of a program and making decisions.
# Conditional Statements in Python
# 1. If Statement: The simplest form of a conditional statement that executes a block of code if a condition is true.
# 2. If-Else Statement: An extension of the if statement that allows you to
#    execute a different block of code if the condition is false.
# 3. If-Elif-Else Statement: A more complex conditional statement that allows you
#    to check multiple conditions in sequence.
# 4. Nested If Statements: An if statement inside another if statement, allowing for more complex decision-making.
# 5. Ternary Operator: A shorthand way to write an if-else statement in a single line.
# 6. Switch Statement: A way to execute different blocks of code based on the value of a variable (not natively supported in Python, but can be simulated using dictionaries or if-elif statements).
# 7. Conditional Expressions: Expressions that evaluate to true or false, often used in list comprehensions or as part of a larger expression.
# 8. Short-Circuit Evaluation: A technique where the second condition is not evaluated if the first condition is sufficient to determine the result, improving performance and avoiding unnecessary computations.
# 9. Exception Handling: Using try-except blocks to handle exceptions and control the flow of a program when an error occurs.
# 10. Assertions: A way to test assumptions in your code, which can help catch bugs early in the development process.
# 11. Context Managers: Using the with statement to manage resources and ensure proper cleanup,
#     such as closing files or releasing locks, even in the presence of exceptions.
# 12. Boolean Logic: Using logical operators (and, or, not) to combine
#     multiple conditions in a single conditional statement.
# 13. Comparison Operators: Using operators like ==, !=, <, >, <=, and >= to compare values and make decisions based on the results.
# 14. Truthy and Falsy Values: Understanding how Python evaluates values as true or false in conditional statements, including the concept of truthy and falsy values.
# 15. Conditional Loops: Using conditional statements
#     within loops to control the flow of iteration based on certain conditions.
#     This can be useful for filtering data or breaking out of loops based on specific criteria.
# 16. Guard Clauses: Using early returns in functions to handle special cases or conditions
#     before proceeding with the main logic, improving readability and reducing nesting.
# 17. Pattern Matching: Using the match-case statement (introduced in Python 3.10)
#     to perform pattern matching on complex data structures, allowing for more expressive and readable code
#     when dealing with multiple conditions.
# 18. Conditional Imports: Importing modules or packages conditionally based on certain criteria,
#     which can help optimize performance or avoid unnecessary dependencies.
# 19. Feature Flags: Using conditional statements to enable or disable features in your code
#     based on configuration settings or environment variables, allowing for more flexible and controlled deployments.
#         print(outer_var)
"""


# 1. If Statement
def check_positive(number):
    """Check if a number is positive."""
    if number > 0:
        print(f"{number} is positive.")
    else:
        print(f"{number} is not positive.")


# Example usage
check_positive(5)  # Output: 5 is positive.


# 2. If-Else Statement
def check_even_odd(number):
    """Check if a number is even or odd."""
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")


# Example usage
check_even_odd(4)  # Output: 4 is even.


# 3. If-Elif-Else Statement
def check_grade(score):
    """Check the grade based on the score."""
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    else:
        print("Grade: D or F")


# Example usage
check_grade(85)  # Output: Grade: B


# 4. Nested If Statements
def check_age(age):
    """Check if a person is an adult or a minor."""
    if age >= 18:
        print("You are an adult.")
        if age >= 65:
            print("You are also a senior citizen.")
    else:
        print("You are a minor.")


# Example usage
check_age(20)  # Output: You are an adult. You are also a senior citizen.


# 5. Ternary Operator
def is_even(number):
    """Check if a number is even using a ternary operator."""
    return "Even" if number % 2 == 0 else "Odd"


# Example usage
print(is_even(3))  # Output: Odd


# 6. Switch Statement (Simulated using a dictionary)
def switch_case(value):
    """Simulate a switch statement using a dictionary."""
    switcher = {1: "One", 2: "Two", 3: "Three"}
    return switcher.get(value, "Invalid value")


# Example usage
print(switch_case(2))  # Output: Two


# 7. Conditional Expressions
def check_number(num):
    """Return a message based on the number."""
    return "Positive" if num > 0 else "Negative or Zero"


# Example usage
print(check_number(-5))  # Output: Negative or Zero


# 8. Short-Circuit Evaluation
def check_conditions(a, b):
    """Check conditions using short-circuit evaluation."""
    if a > 0 and b > 0:
        print("Both numbers are positive.")
    else:
        print("At least one number is not positive.")


# Example usage
check_conditions(5, -3)  # Output: At least one number is not positive


# 9. Exception Handling
def divide_numbers(num1, num2):
    """Divide two numbers with exception handling."""
    try:
        result = num1 / num2
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
divide_numbers(10, 0)  # Output: Error: Division by zero is not allowed.


# 10. Assertions
def check_positive_assertion(number):
    """Check if a number is positive using an assertion."""
    assert number > 0, "Number must be positive"
    print(f"{number} is positive.")


# Example usage
try:
    check_positive_assertion(-5)  # This will raise an AssertionError
except AssertionError as e:
    print(f"Assertion Error: {e}")


# 11. Context Managers
def read_file(file_path):
    """Read a file using a context manager."""
    try:
        with open(file_path, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
read_file("example.txt")  # Make sure to have a file named 'example.txt'


# 12. Boolean Logic
def check_conditions_with_logic(a, b):
    """Check conditions using boolean logic."""
    if a > 0 and (b < 10 or b > 20):
        print("Condition met.")
    else:
        print("Condition not met.")


# Example usage
check_conditions_with_logic(5, 15)  # Output: Condition met.


# 13. Comparison Operators
def compare_numbers(x, y):
    """Compare two numbers using comparison operators."""
    if x == y:
        print("Numbers are equal.")
    elif x < y:
        print("x is less than y.")
    else:
        print("x is greater than y.")


# Example usage
compare_numbers(10, 20)  # Output: x is less than y.


# 14. Truthy and Falsy Values
def check_truthy_falsy(value):
    """Check if a value is truthy or falsy."""
    if value:
        print(f"{value} is truthy.")
    else:
        print(f"{value} is falsy.")


# Example usage
check_truthy_falsy([])  # Output: [] is falsy.


# 15. Conditional Loops
def filter_positive_numbers(numbers):
    """Filter positive numbers from a list."""
    positive_numbers = []
    for number in numbers:
        if number > 0:
            positive_numbers.append(number)
    return positive_numbers


# Example usage
print(filter_positive_numbers([-1, 2, -3, 4, 5]))  # Output: [2, 4, 5]


# 16. Guard Clauses
def process_data(data):
    """Process data with guard clauses."""
    if not data:
        print("No data to process.")
        return
    if isinstance(data, list):
        print("Processing list data:", data)
    else:
        print("Unsupported data type.")


# Example usage
process_data([])  # Output: No data to process.


# 17. Pattern Matching (Python 3.10+)
def match_shape(shape):
    """Match a shape using pattern matching."""
    match shape:
        case {"type": "circle", "radius": r}:
            print(f"Circle with radius {r}")
        case {"type": "rectangle", "width": w, "height": h}:
            print(f"Rectangle with width {w} and height {h}")
        case _:
            print("Unknown shape")


# Example usage
match_shape({"type": "circle", "radius": 5})  # Output: Circle with radius 5


# 18. Conditional Imports
def conditional_import():
    """Import a module conditionally."""
    import sys

    if sys.version_info >= (3, 10):
        print("Using features available in Python 3.10 or later.")
    else:
        print("Using features available in earlier versions of Python.")


# Example usage
conditional_import()  # Output will depend on the Python version


# 19. Feature Flags
def feature_flag_example(flag):
    """Enable or disable features based on a flag."""
    if flag:
        print("Feature is enabled.")
    else:
        print("Feature is disabled.")


# Example usage
feature_flag_example(True)  # Output: Feature is enabled.

# 20. Using the main guard
if __name__ == "__main__":
    # Example usage of the functions defined above
    check_positive(10)
    check_even_odd(7)
    check_grade(92)
    check_age(70)
    print(is_even(8))
    print(switch_case(3))
    print(check_number(0))
    check_conditions(3, 4)
    divide_numbers(10, 2)
    check_positive_assertion(5)
    read_file("example.txt")
    check_conditions_with_logic(15, 25)
    compare_numbers(30, 20)
    check_truthy_falsy("Hello")
    print(filter_positive_numbers([-5, 0, 3, 8]))
    process_data([1, 2, 3])
    match_shape({"type": "rectangle", "width": 10, "height": 5})
    conditional_import()
    feature_flag_example(False)
    print("All examples executed successfully.")
# This code demonstrates various conditional statements and their usage in Python.
# You can run this code in a Python environment to see the output and understand how each conditional
# statement works. Feel free to modify the examples and experiment with different conditions!
# This code provides a comprehensive overview of how to use conditional statements in Python, covering various types
# of conditions and their applications. You can run this code in a Python environment to see the output and experiment with different conditions and scenarios.
# Conditional statements are essential for controlling the flow of a program and making decisions based on specific criteria. They allow you to execute different blocks of code depending on the conditions you define, enabling dynamic behavior in your applications.
# This code provides a comprehensive overview of how to use conditional statements in Python, covering various types of conditions and their applications. You can run this code in a Python environment to see the output and experiment with different conditions and scenarios.
# Conditional statements are essential for controlling the flow of a program and making decisions based on specific criteria. They allow you to execute different blocks of code depending on the conditions you define, enabling dynamic behavior in your applications.
# This code provides a comprehensive overview of how to use conditional statements in Python, covering various types
# of conditions and their applications. You can run this code in a Python environment to see the output and experiment with different conditions and scenarios.
# Conditional statements are essential for controlling the flow of a program and making decisions based on specific criteria. They allow you to execute different blocks of code depending on the conditions you define, enabling dynamic behavior in your applications.
# This code provides a comprehensive overview of how to use conditional statements in Python, covering various types
# of conditions and their applications. You can run this code in a Python environment to see the output and experiment with different conditions and scenarios.
