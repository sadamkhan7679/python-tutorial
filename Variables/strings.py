# Here we will focus on string data type and its methods
is_student = True
print("Is Student:", is_student)
# Strings in Python
# Strings are sequences of characters and are one of the most commonly used data types in Python. They can be created by enclosing characters in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
# Here are some examples of how to create and manipulate strings in Python:
# Creating strings
single_quote_str = "Hello, World!"
double_quote_str = "Python is awesome!"
triple_quote_str = """This is a multi-line string."""
print(single_quote_str)
print(double_quote_str)
print(triple_quote_str)
# String concatenation
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)
# String formatting
age = 25
formatted_str = f"My name is {name} and I am {age} years old."
print(formatted_str)
# String methods
sample_str = "  Hello, Python!  "
print("Original String:", sample_str)  # Output: "  Hello, Python!  "
print("Lowercase:", sample_str.lower())  # Output: "  hello, python!  "
print("Uppercase:", sample_str.upper())  # Output: "  HELLO, PYTHON!  "
print("Stripped:", sample_str.strip())  # Output: "Hello, Python!"
print("Replaced:", sample_str.replace("Python", "World"))  # Output: "  Hello, World!  "
print("Split:", sample_str.split(","))  # Output: ['  Hello', ' Python!  ']
print("Length:", len(sample_str))  # Output: 18
print("Index of 'Python':", sample_str.index("Python"))  # Output: 9
print("Count of 'o':", sample_str.count("o"))  # Output: 2
# Accessing characters in a string
first_char = sample_str[0]
last_char = sample_str[-1]
print("First Character:", first_char)  # Output: " "
print("Last Character:", last_char)  # Output: " "
# Slicing strings
substring = sample_str[2:7]
print("Substring (2 to 7):", substring)  # Output: "Hello"
# Strings are immutable, meaning you cannot change individual characters in a string. However, you can create a new string based on modifications of the original string.
# Example of immutability
original_str = "Hello"
modified_str = original_str.replace("H", "J")
print("Original String:", original_str)  # Output: "Hello"
print("Modified String:", modified_str)  # Output: "Jello"
# This is a brief overview of strings in Python and some of their common methods. Strings are versatile and powerful, making them essential for text manipulation in Python programming.
# Feel free to experiment with different string methods and operations to get a better understanding of how they work!

# ADVANCED STRING METHODS
# In addition to the basic string methods covered earlier, Python provides several advanced string methods that can be very useful for more complex string manipulations. Here are some of the advanced string methods in Python:
# 1. join(): This method is used to join elements of an iterable (like a list or tuple) into a single string, with a specified separator.
words = ["Hello", "world", "from", "Python"]
joined_str = " ".join(words)
print("Joined String:", joined_str)  # Output: "Hello world from Python"
# 2. find(): This method returns the lowest index of the substring if found in the string. If not found, it returns -1.
sample_str = "Hello, welcome to Python programming."
index = sample_str.find("Python")
print("Index of 'Python':", index)  # Output: 18
# 3. startswith() and endswith(): These methods check if a string starts or ends with a specified substring, returning True or False.
print("Starts with 'Hello':", sample_str.startswith("Hello"))  # Output: True
print("Ends with 'programming.':", sample_str.endswith("programming."))  # Output: True
# 4. isalpha(), isdigit(), isalnum(): These methods check if all characters in the string are alphabetic, numeric, or alphanumeric, respectively.
alpha_str = "Hello"
digit_str = "12345"
alnum_str = "Hello123"
print("Is Alpha:", alpha_str.isalpha())  # Output: True
print("Is Digit:", digit_str.isdigit())  # Output: True
print("Is Alphanumeric:", alnum_str.isalnum())  # Output: True
# 5. capitalize(): This method capitalizes the first character of the string and converts the rest to lowercase.
mixed_case_str = "hELLO wORLD"
capitalized_str = mixed_case_str.capitalize()
print("Capitalized String:", capitalized_str)  # Output: "Hello world"
# 6. title(): This method converts the first character of each word to uppercase and the rest to lowercase.
title_str = mixed_case_str.title()
print("Title String:", title_str)  # Output: "Hello World"
# 7. zfill(): This method pads the string on the left with zeros to fill a specified width.
num_str = "42"
padded_str = num_str.zfill(5)
print("Padded String:", padded_str)  # Output: "00042"
# 8. format(): This method allows you to format strings using placeholders.
name = "Alice"
age = 30
formatted_str = "My name is {} and I am {} years old.".format(name, age)
print(formatted_str)  # Output: "My name is Alice and I am 30 years old."
# 9. encode() and decode(): These methods are used to encode a string into bytes and decode bytes back into a string, respectively.
original_str = "Hello, World!"
encoded_str = original_str.encode("utf-8")
decoded_str = encoded_str.decode("utf-8")
print("Encoded String:", encoded_str)  # Output: b'Hello, World!'
print("Decoded String:", decoded_str)  # Output: "Hello, World!"
# These advanced string methods provide powerful tools for manipulating and working with strings in Python. Experimenting with these methods will help you become more proficient in handling text data in your Python programs.
# Feel free to explore the Python documentation for more string methods and their functionalities: https://docs.python.org/3/library/stdtypes.html#string-methods
