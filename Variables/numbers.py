# We will use this file to learn about numbers in Python. We will cover the following topics:
# 1. Integer (int): Represents whole numbers, both positive and negative, without decimal points.
# 2. Float (float): Represents real numbers, including decimal points.
# 3. Complex (complex): Represents complex numbers, which have a real and an imaginary part, represented as a + bj, where a is the real part and b is the imaginary part.
# 4. Arithmetic Operations: Basic operations like addition, subtraction, multiplication, and division.
# 5. Type Conversion: Converting between different numeric types.
# 6. Number Functions: Built-in functions for working with numbers, such as abs(), round(), and pow().
# 7. Number Formatting: Formatting numbers for output, including fixed-point notation and scientific notation.
# 8. Random Numbers: Generating random numbers using the random module.
# 9. Number Comparisons: Comparing numbers using comparison operators.
# 10. Number Ranges: Creating ranges of numbers using the range() function.
# 11. Number Sequences: Working with sequences of numbers, such as lists and tuples.
# 12. Number Iteration: Iterating over numbers using loops.
# 13. Number Libraries: Using libraries like NumPy for advanced numerical operations.

# 1. Integer (int)
# Represents whole numbers, both positive and negative, without decimal points.
age = 30
print("Age:", age)  # Output: Age: 30

# 2. Float (float)
# Represents real numbers, including decimal points.

height = 5.9
print("Height:", height)  # Output: Height: 5.9

# 3. Complex (complex)
# Represents complex numbers, which have a real and an imaginary part, represented as a + bj
complex_number = 3 + 4j
print("Complex Number:", complex_number)  # Output: Complex Number: (3+4j)

# 4. Arithmetic Operations
# Basic operations like addition, subtraction, multiplication, and division.
a = 10
b = 5
print("Addition:", a + b)  # Output: Addition: 15
print("Subtraction:", a - b)  # Output: Subtraction: 5
print("Multiplication:", a * b)  # Output: Multiplication: 50
print("Division:", a / b)  # Output: Division: 2.0

# 5. Type Conversion
# Converting between different numeric types.
int_value = 10
float_value = float(int_value)
print("Converted to Float:", float_value)  # Output: Converted to Float: 10.0
str_value = str(int_value)
print("Converted to String:", str_value)  # Output: Converted to String: '10'

# 6. Number Functions
# Built-in functions for working with numbers, such as abs(), round(), and pow().
print("Absolute Value:", abs(-10))  # Output: Absolute Value: 10
print("Rounded Value:", round(5.678, 2))  # Output: Rounded Value: 5.68
print("Power:", pow(2, 3))  # Output: Power: 8

# 7. Number Formatting
# Formatting numbers for output, including fixed-point notation and scientific notation.
formatted_number = "{:.2f}".format(3.14159)
print("Formatted Number:", formatted_number)  # Output: Formatted Number: 3.14
scientific_notation = "{:.2e}".format(123456789)
print(
    "Scientific Notation:", scientific_notation
)  # Output: Scientific Notation: 1.23e+08

# 8. Random Numbers
# Generating random numbers using the random module.
import random

random_integer = random.randint(1, 100)
print(
    "Random Integer:", random_integer
)  # Output: Random Integer: (some random integer between 1 and 100)
random_float = random.uniform(1.0, 10.0)
print(
    "Random Float:", random_float
)  # Output: Random Float: (some random float between 1.0 and 10.0)

# 9. Number Comparisons
# Comparing numbers using comparison operators.
x = 10
y = 20
print("Is x equal to y?", x == y)  # Output: Is x equal to y? False
print("Is x less than y?", x < y)  # Output: Is x less than y? True
print(
    "Is x greater than or equal to y?", x >= y
)  # Output: Is x greater than or equal to y? False
print("Is x not equal to y?", x != y)  # Output: Is x not equal to y? True

# 10. Number Ranges
# Creating ranges of numbers using the range() function.
for i in range(1, 10, 2):
    print("Range Value:", i)  # Output: Range Value: 1, 3, 5, 7, 9

# 11. Number Sequences
# Working with sequences of numbers, such as lists and tuples.
numbers_list = [1, 2, 3, 4, 5]
print("Numbers List:", numbers_list)  # Output: Numbers List: [1, 2, 3, 4, 5]
numbers_tuple = (6, 7, 8, 9, 10)
print("Numbers Tuple:", numbers_tuple)  # Output: Numbers Tuple: (6, 7, 8, 9, 10)

# 12. Number Iteration
# Iterating over numbers using loops.
for number in numbers_list:
    print("Iterated Number:", number)  # Output: Iterated Number: 1, 2, 3, 4, 5

# 13. Number Libraries
# Using libraries like NumPy for advanced numerical operations.
import numpy as np

# Creating a NumPy array
numpy_array = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", numpy_array)  # Output: NumPy Array: [1 2 3 4 5]
# Performing operations on NumPy arrays
numpy_sum = np.sum(numpy_array)
print("Sum of NumPy Array:", numpy_sum)  # Output: Sum of NumPy Array: 15
numpy_mean = np.mean(numpy_array)
print("Mean of NumPy Array:", numpy_mean)  # Output: Mean of NumPy Array: 3.0

# This code provides a comprehensive overview of how to work with numbers in Python, covering various numeric types, operations, and libraries.
# You can run this code in a Python environment to see the output and experiment with different numeric operations.
