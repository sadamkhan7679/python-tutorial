# We will discuss about various operators in Python. We will cover the following topics:
# 1. Arithmetic Operators: Basic operations like addition, subtraction, multiplication, and division.
# 2. Comparison Operators: Comparing values using operators like ==, !=, <, >, <=, and >=.
# 3. Logical Operators: Combining boolean expressions using and, or, and not.
# 4. Assignment Operators: Assigning values to variables using =, +=, -=, *=, /=, //=, %=, and **=.
# 5. Ternary Operator: A shorthand way to write an if-else statement.
# 6. Bitwise Operators: Performing bit-level operations using &, |, ^, ~, <<, and >>.
# 7. Identity Operators: Checking if two variables refer to the same object using is and is not.
# 8. Membership Operators: Checking if a value is present in a sequence using in and not in.
# 9. Operator Precedence: Understanding the order of operations in expressions.
# 10. Augmented Assignment Operators: Combining assignment with arithmetic operations
# 11. Chaining Comparison Operators: Using multiple comparison operators in a single expression.
# 12. Short-Circuit Evaluation: How logical operators evaluate expressions.


# 1. Arithmetic Operators
a = 10
b = 5
print("Addition:", a + b)  # Output: Addition: 15
print("Subtraction:", a - b)  # Output: Subtraction: 5
print("Multiplication:", a * b)  # Output: Multiplication: 50
print("Division:", a / b)  # Output: Division: 2.0 floating point division
print("Floor Division:", a // b)  # Output: Floor Division: 2 integer
print("Modulus:", a % b)  # Output: Modulus: 0
print("Exponentiation:", a**b)  # Output: Exponentiation: 100
print("Square Root:", a**0.5)  # Output: Square Root: 3.1622776601683795
print("Power:", a**b)  # Output: Power: 100000

# 2. Comparison Operators
print("Equal:", a == b)  # Output: Equal: False
print("Not Equal:", a != b)  # Output: Not Equal: True
print("Greater Than:", a > b)  # Output: Greater Than: True
print("Less Than:", a < b)  # Output: Less Than: False
print("Greater Than or Equal:", a >= b)  # Output: Greater Than or Equal: True
print("Less Than or Equal:", a <= b)  # Output: Less Than or Equal: False

# 3. Logical Operators
print("Logical AND:", a > 5 and b < 10)  # Output: True
print("Logical OR:", a > 15 or b < 10)  # Output: True
print("Logical NOT:", not (a > 5))  # Output: False

# 4. Assignment Operators
a += 5
print("Augmented Addition:", a)  # Output: Augmented Addition: 15
b *= 2
print("Augmented Multiplication:", b)  # Output: Augmented Multiplication: 10
# Augmented division
a /= 2
print("Augmented Division:", a)  # Output: Augmented Division: 7.5
# Augmented floor division
b //= 3
print("Augmented Floor Division:", b)  # Output: Augmented Floor Division: 3
# Augmented modulus
a %= 3
print("Augmented Modulus:", a)  # Output: Augmented Modulus: 1.5

# 5. Ternary Operator
max_value = a if a > b else b
print("Max Value:", max_value)  # Output: Max Value: 1.5

# 6. Bitwise Operators
print("Bitwise AND:", a & b)  # Output: Bitwise AND: 1
print("Bitwise OR:", a | b)  # Output: Bitwise OR: 3
print("Bitwise XOR:", a ^ b)  # Output: Bitwise XOR: 2
print("Bitwise NOT:", ~a)  # Output: Bitwise NOT: -2
print("Left Shift:", a << 1)  # Output: Left Shift: 3
print("Right Shift:", a >> 1)  # Output: Right Shift: 0

# 7. Identity Operators
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("x is y:", x is y)  # Output: True
print("x is z:", x is z)  # Output: False
print("x is not z:", x is not z)  # Output: True


# 8. Membership Operators
my_list = [1, 2, 3, 4, 5]
print("1 in my_list:", 1 in my_list)  # Output: True
print("6 not in my_list:", 6 not in my_list)  # Output: True

# 9. Operator Precedence
result = a + b * 2 - 3 / 1
print("Operator Precedence Result:", result)  # Output: Operator Precedence Result: 10.0

# 11. Chaining Comparison Operators
x = 5
y = 10
z = 15
print("Chained Comparison:", x < y < z)  # Output: True

# 12. Short-Circuit Evaluation
# In Python, logical operators like 'and' and 'or' use short-circuit evaluation
# This means that the second operand is evaluated only if necessary.
print("Short-Circuit AND:", (x > 0) and (y < 20))  # Output: True
print("Short-Circuit OR:", (x < 0) or (y > 5))  # Output: True
