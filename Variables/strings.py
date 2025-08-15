# Here we will focus on string data type and its methods
is_student = True
print("Is Student:", is_student)
# Strings in Python
# Strings are sequences of characters and are one of the most commonly used data types in Python. They can be created by enclosing characters in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
# Here are some examples of how to create and manipulate strings in Python:
# Creating strings
single_quote_str = "Hello, World!"
double_quote_str = "Python is awesome!"
triple_quote_str = (
    """This is a multi-line string."""  # This is also a multi-line string
)

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
first_char = sample_str[0]  # First character of the string , Output: " "
last_char = sample_str[-1]  # Last character of the string, Output: " "
print("First Character:", first_char)  # Output: " "
print("Last Character:", last_char)  # Output: " "
# Slicing strings
substring = sample_str[2:7]  # Extracting a substring from index 2 to 7
# Note: The end index is exclusive, so it will not include the character at index 7.
# If we don't specify the start index, it defaults to 0, and if we don't specify the end index, it defaults to the length of the string.
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

# 10. splitlines(): This method splits a string into a list of lines, breaking at line boundaries.
multiline_str = "Line 1\nLine 2\nLine 3"
lines = multiline_str.splitlines()
print("Lines:", lines)  # Output: ['Line 1', 'Line 2', 'Line 3']

# 11. swapcase(): This method swaps the case of all characters in the string (uppercase to lowercase and vice versa).
swapcase_str = "Hello, World!"
swapped_str = swapcase_str.swapcase()
print("Swapped Case String:", swapped_str)  # Output: "hELLO, wORLD!"

# 12. count(): This method counts the occurrences of a substring in the string.
count_str = "Hello, Hello, Hello!"
substring_count = count_str.count("Hello")
print("Count of 'Hello':", substring_count)  # Output: 3

# 13. rfind(): This method returns the highest index of the substring if found in the string. If not found, it returns -1.
rindex_str = "Hello, welcome to Python programming. Python is great."
rindex = rindex_str.rfind("Python")
print("Last Index of 'Python':", rindex)  # Output: 30

# 14. rstrip() and lstrip(): These methods remove trailing and leading whitespace characters from the string, respectively.
rstrip_str = "   Hello, World!   "
print("Right Stripped String:", rstrip_str.rstrip())  # Output: "   Hello, World!"
print("Left Stripped String:", rstrip_str.lstrip())  # Output: "Hello, World!   "

# 15. casefold(): This method is similar to lower(), but it is more aggressive in converting characters to lowercase, making it suitable for case-insensitive comparisons.
casefold_str = "HELLO, WORLD!"
print("Casefolded String:", casefold_str.casefold())  # Output: "hello, world!"

# 16. format_map(): This method is similar to format(), but it takes a mapping (like a dictionary) instead of positional arguments.
data = {"name": "Alice", "age": 30}
formatted_map_str = "My name is {name} and I am {age} years old.".format_map(data)
print(formatted_map_str)  # Output: "My name is Alice and I am 30 years old."

# 17. Escape sequences: Strings can contain escape sequences, which are special characters that represent certain actions or formatting. For example, "\n" represents a newline, "\t" represents a tab, and "\\" represents a backslash.
escaped_str = "Hello,\nWorld!\tThis is a backslash: \\"
print("Escaped String:\n", escaped_str)

# 18. Dynamic string creation: You can create dynamic strings using f-strings (formatted string literals) introduced in Python 3.6. They allow you to embed expressions inside string literals, making it easier to create formatted strings.
dynamic_name = "Bob"
dynamic_age = 28
dynamic_str = f"My name is {dynamic_name} and I am {dynamic_age} years old."
print(dynamic_str)  # Output: "My name is Bob and I am 28 years old."

# 19. Template strings: Python's `string` module provides a `Template` class that allows you to create strings with placeholders that can be substituted with values. This is useful for creating templates for text generation.
from string import Template

template_str = Template("Hello, $name! You are $age years old.")
template_filled = template_str.substitute(name="Charlie", age=35)
print(
    "Template Filled String:", template_filled
)  # Output: "Hello, Charlie! You are 35 years old."

# 20. in and not in: These operators can be used to check if a substring exists within a string or not.
check_str = "Hello, World!"
print("Is 'World' in check_str?", "World" in check_str)  # Output: True
print("Is 'Python' not in check_str?", "Python" not in check_str)  # Output: True

# 21. isspace(): This method checks if all characters in the string are whitespace characters (spaces, tabs, newlines).
whitespace_str = "   \t\n"
print("Is whitespace_str all whitespace?", whitespace_str.isspace())  # Output: True

# 22. isprintable(): This method checks if all characters in the string are printable (not control characters).
printable_str = "Hello, World!"
non_printable_str = "Hello,\x00World!"  # Contains a null character
print("Is printable_str printable?", printable_str.isprintable())  # Output: True
print(
    "Is non_printable_str printable?", non_printable_str.isprintable()
)  # Output: False


# These advanced string methods provide powerful tools for manipulating and working with strings in Python. Experimenting with these methods will help you become more proficient in handling text data in your Python programs.
# Feel free to explore the Python documentation for more string methods and their functionalities: https://docs.python.org/3/library/stdtypes.html#string-methods
