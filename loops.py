# We will learn about loops in Python. We will cover the following topics:
# 1. For Loop: Iterating over a sequence (like a list, tuple, or string) using a for loop.
# 2. While Loop: Repeating a block of code as long as a condition is true using a while loop.
# 3. Nested Loops: Using loops inside other loops to perform complex iterations.
# 4. Loop Control Statements: Using break, continue, and pass statements to control the flow of loops.
# 5. Looping through Dictionaries: Iterating over key-value pairs in a dictionary.
# # 6. Looping through Sets: Iterating over elements in a set.
# # 7. Looping through Strings: Iterating over characters in a string.
# # 8. List Comprehensions: Creating lists using a concise syntax with for loops.
# # 9. Enumerate Function: Getting both the index and value while iterating over a sequence.
# 10. Zip Function: Combining multiple sequences into tuples while iterating.
# 11. Iterators and Generators: Understanding how to create and use iterators
#     and generators for efficient looping.
# 12. Looping with Conditions: Using if statements within loops to filter elements.
# 13. Looping with Range: Using the range() function to generate a sequence of numbers for iteration.
# 14. Looping with List Methods: Using list methods like append(), extend(), and pop() within loops.
# 15. Looping with String Methods: Using string methods like split(), join(), and replace() within loops.
# 16. Looping with File I/O: Reading and writing files using loops.
# 17. Looping with Exception Handling: Using try-except blocks within loops to handle exceptions.
# 18. Looping with Context Managers: Using the with statement to manage resources while looping.


# 1. For Loop
# Iterating over a sequence (like a list, tuple, or string) using a for loop.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)  # Output: Fruit: apple, Fruit: banana, Fruit: cherry

# 2. While Loop
# Repeating a block of code as long as a condition is true using a while loop.
count = 0
while count < 5:
    print("Count:", count)  # Output: Count: 0, 1, 2, 3, 4
    count += 1

# 3. Nested Loops
# Using loops inside other loops to perform complex iterations.
for i in range(3):
    for j in range(2):
        print(
            f"i: {i}, j: {j}"
        )  # Output: i: 0, j: 0; i: 0, j: 1; i: 1, j: 0; i: 1, j: 1; i: 2, j: 0; i: 2, j: 1

# 4. Loop Control Statements
# Using break, continue, and pass statements to control the flow of loops.
for num in range(10):
    if num == 5:
        print("Breaking at 5")
        break  # Exits the loop when num is 5
    print("Number:", num)  # Output: Number: 0, 1, 2, 3, 4
for num in range(10):
    if num % 2 == 0:
        print("Skipping even number:", num)
        continue  # Skips the rest of the loop for even numbers
    print("Odd Number:", num)  # Output: Odd Number: 1, 3, 5, 7, 9
for num in range(5):
    if num == 2:
        print("Passing at 2")
        pass  # Does nothing, just passes to the next iteration
    print("Number:", num)  # Output: Number: 0, 1, 2, 3, 4

# 5. Looping through Dictionaries
# Iterating over key-value pairs in a dictionary.
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")  # Output: name: Alice, age: 30, city: New York
# 6. Looping through Sets
# Iterating over elements in a set.
unique_numbers = {1, 2, 3, 4, 5}
for number in unique_numbers:
    print(
        "Unique Number:", number
    )  # Output: Unique Number: 1, 2, 3, 4, 5 (order may vary)
# 7. Looping through Strings
# Iterating over characters in a string.
message = "Hello"
for char in message:
    print("Character:", char)  # Output: Character: H, e, l, l, o

# 8. List Comprehensions
# Creating lists using a concise syntax with for loops.
squares = [x**2 for x in range(10)]
print("Squares:", squares)  # Output: Squares: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 9. Enumerate Function
# Getting both the index and value while iterating over a sequence.
for index, fruit in enumerate(fruits):
    print(
        f"Index: {index}, Fruit: {fruit}"
    )  # Output: Index: 0, Fruit: apple; Index: 1, Fruit: banana; Index: 2, Fruit: cherry

# 10. Zip Function
# Combining multiple sequences into tuples while iterating.
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
for name, age in zip(names, ages):
    print(
        f"Name: {name}, Age: {age}"
    )  # Output: Name: Alice, Age: 30; Name: Bob, Age: 25; Name: Charlie, Age: 35


# 11. Iterators and Generators
# Understanding how to create and use iterators and generators for efficient looping.
def count_up_to(max):
    """Generator function to yield numbers up to max."""
    count = 1
    while count <= max:
        yield count
        count += 1


for number in count_up_to(5):
    print(
        "Number from generator:", number
    )  # Output: Number from generator: 1, 2, 3, 4, 5
# 12. Looping with Conditions
# Using if statements within loops to filter elements.
for num in range(10):
    if num % 2 == 0:
        print("Even Number:", num)  # Output: Even Number: 0, 2, 4, 6, 8
    else:
        print("Odd Number:", num)  # Output: Odd Number: 1, 3, 5, 7, 9
# 13. Looping with Range
# Using the range() function to generate a sequence of numbers for iteration.
for i in range(1, 10, 2):
    print("Range Value:", i)  # Output: Range Value: 1, 3, 5, 7, 9
# 14. Looping with List Methods
# Using list methods like append(), extend(), and pop() within loops.
numbers = []
for i in range(5):
    numbers.append(i)
    print(
        "List after append:", numbers
    )  # Output: List after append: [0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4]
for i in range(3):
    numbers.extend([i + 5])
    print(
        "List after extend:", numbers
    )  # Output: List after extend: [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6, 7]
for _ in range(2):
    popped_value = numbers.pop()
    print("Popped Value:", popped_value)  # Output: Popped Value: 7, 6
    print("List after pop:", numbers)  # Output: List after pop: [0, 1, 2, 3, 4, 5]
# 15. Looping with String Methods
# Using string methods like split(), join(), and replace() within loops.
sentence = "Hello World"
words = sentence.split()  # Splitting the string into words
for word in words:
    print("Word:", word)  # Output: Word: Hello, Word: World
new_sentence = " ".join(words)  # Joining the words back into a string
print("Joined Sentence:", new_sentence)  # Output: Joined Sentence: Hello World
replaced_sentence = sentence.replace(
    "World", "Python"
)  # Replacing a word in the string
print(
    "Replaced Sentence:", replaced_sentence
)  # Output: Replaced Sentence: Hello Python
# 16. Looping with File I/O
# Reading and writing files using loops.
with open("example.txt", "w") as file:
    for i in range(5):
        file.write(f"Line {i + 1}\n")  # Writing lines to the file
with open("example.txt", "r") as file:
    for line in file:
        print(
            "File Line:", line.strip()
        )  # Output: File Line: Line 1, File Line: Line 2, File Line: Line 3, File Line: Line 4, File Line: Line 5
# 17. Looping with Exception Handling
# Using try-except blocks within loops to handle exceptions.
numbers = [1, 2, 0, 4]
for num in numbers:
    try:
        result = 10 / num
        print("Result:", result)  # Output: Result: 10.0, 5.0, (skips division by zero)
    except ZeroDivisionError:
        print("Cannot divide by zero")  # Output: Cannot divide by zero
# 18. Looping with Context Managers
# Using the with statement to manage resources while looping.
with open("example.txt", "r") as file:
    for line in file:
        print(
            "File Line with Context Manager:", line.strip()
        )  # Output: File Line with Context Manager: Line 1, File Line with Context Manager: Line 2, ...# 19. Looping with List Comprehensions
# Creating lists using a concise syntax with for loops.
squares = [x**2 for x in range(10)]
print(
    "Squares with List Comprehension:", squares
)  # Output: Squares with List Comprehension: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 20. Looping with Conditional Expressions
# Using conditional expressions within loops to filter elements.
filtered_numbers = [x for x in range(10) if x % 2 == 0]
print(
    "Filtered Even Numbers:", filtered_numbers
)  # Output: Filtered Even Numbers: [0, 2, 4, 6, 8]
# 21. Looping with Multiple Iterables
# Using the zip() function to iterate over multiple iterables simultaneously.
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
for name, age in zip(names, ages):
    print(
        f"Name: {name}, Age: {age}"
    )  # Output: Name: Alice, Age: 30; Name: Bob, Age: 25; Name: Charlie, Age: 35


# 22. Looping with Iterators
# Understanding how to create and use iterators for efficient looping.
class Counter:
    """A simple iterator that counts up to a specified number."""

    def __init__(self, max_count):
        self.max_count = max_count
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max_count:
            self.current += 1
            return self.current
        else:
            raise StopIteration


for count in Counter(5):
    print("Count from Iterator:", count)  # Output: Count from Iterator: 1, 2, 3, 4, 5


# 23. Looping with Generators
# Understanding how to create and use generators for efficient looping.
def fibonacci(n):
    """Generator function to yield Fibonacci numbers up to n."""
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


for num in fibonacci(10):
    print("Fibonacci Number:", num)  # Output: Fibonacci Number: 0, 1, 1, 2, 3, 5, 8
# 24. Looping with Comprehensions
# Using comprehensions to create lists, sets, or dictionaries in a concise way.
squares_set = {x**2 for x in range(10)}
print(
    "Squares Set:", squares_set
)  # Output: Squares Set: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
squares_dict = {x: x**2 for x in range(10)}
print(
    "Squares Dictionary:", squares_dict
)  # Output: Squares Dictionary: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# 25. Looping with Conditional Logic
# Using conditional logic within loops to perform different actions based on conditions.
for i in range(10):
    if i % 2 == 0:
        print(
            f"{i} is even"
        )  # Output: 0 is even, 2 is even, 4 is even, 6 is even, 8 is even
    else:
        print(f"{i} is odd")  # Output: 1 is odd, 3 is odd, 5 is odd, 7 is odd, 9 is odd


# 26. Looping with Functions
# Using functions to encapsulate loop logic and improve code organization.
def print_numbers(n):
    """Function to print numbers from 0 to n."""
    for i in range(n):
        print("Number:", i)  # Output: Number: 0, 1, 2, ..., n-1


print_numbers(5)  # Calling the function to print numbers from 0 to 4
