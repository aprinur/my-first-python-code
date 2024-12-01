# * 1. print()
# The print() function outputs data to the console. You can customize the separator and end character.

# Basic print
print("My name is", "Tim", "and I am", 23, "years old.")

# Custom separator
print("My name is", "Tim", "and I am", 23, "years old.", sep=' | ')

# Custom end character
print("Hello", end=' | ')
print("World")

# Printing multiple data types
name = "Tim"
age = 23
print(f"My name is {name} and I am {age} years old.")

# Using sep and end arguments
print("Hello", "World", sep=' | ', end='; ')
print("This is on the same line.")


# * 2. help()
# The help() function displays the documentation for a specified function.

# Get help on the print function
help(print)


# Custom function with docstring
def test_func(a, b):
    """This function adds two numbers."""
    return a + b


help(test_func)


# * 3. range()
# The range() function generates a sequence of numbers, which can be used in loops.

# Basic range
for i in range(10):
    print(i)

# Range with start, stop, and step
for i in range(2, 10, 2):
    print(i)

# Negative range
for i in range(10, -1, -2):
    print(i)

# Convert range to a list
numbers_list = list(range(5, 15))
print(numbers_list)


# * 4. map()
# The map() function applies a specified function to each item in an iterable.

# Using map with a built-in function
strings = ["apple", "banana", "cherry"]
lengths = list(map(len, strings))
print(lengths)

# Using map with a lambda function
squared_numbers = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
print(squared_numbers)


# Using a custom function with map
def add_s(s):
    return s + 's'


pluralized = list(map(add_s, strings))
print(pluralized)


# * 5. filter()
# The filter() function filters items in an iterable based on a function that returns True or False.

# Filtering even numbers
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


# Using a custom filter function
def longer_than_four(s):
    return len(s) > 4


filtered_strings = list(filter(longer_than_four, strings))
print(filtered_strings)


# * 6. sum()
# The sum() function returns the sum of all items in an iterable, with an optional starting value.

# Simple sum of a list
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)

# Sum with a starting value
total_with_start = sum(numbers, 10)
print(total_with_start)

# Sum with negative values
negative_sum = sum([-1, -2, -3])
print(negative_sum)


# * 7. sorted()
# The sorted() function sorts an iterable in ascending or descending order.

# Sorting numbers
numbers = [4, 2, 9, 1]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
# Sorting in descending order
sorted_descending = sorted(numbers, reverse=True)
print(sorted_descending)

# Sorting with a key (by length of strings)
fruits = ['apple', 'kiwi', 'banana', 'pear']
sorted_fruits = sorted(fruits, key=len)
print(sorted_fruits)

# Sorting a list of dictionaries by age
people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
sorted_people = sorted(people, key=lambda x: x['age'])
print(sorted_people)


# * 8. enumerate()
# The enumerate() function adds a counter to an iterable, allowing access to both index and value during iteration.

# Iterating with index
tasks = ['task1', 'task2', 'task3']
for index, task in enumerate(tasks):
    print(f"{index + 1}: {task}")

# Starting index at 1
for index, task in enumerate(tasks, start=1):
    print(f"{index}: {task}")


# * 9. zip()
# The zip() function combines multiple iterables into tuples, handling mismatches in lengths gracefully.

# Zipping two lists
names = ['Alice', 'Bob', 'Charlie']
ages = [30, 25, 35]
combined = zip(names, ages)

for name, age in combined:
    print(f"{name} is {age} years old.")

# Zipping three lists
locations = ['USA', 'UK', 'Canada']
zipped = zip(names, ages, locations)
for name, age, loc in zipped:
    print(f"{name}, {age}, {loc}")

# Handling mismatched lengths
names = ['Alice', 'Bob', 'Charlie', 'Tim']
ages = [30, 25, 35]
combined = zip(names, ages)  # 'Tim' will be ignored
for name, age in combined:
    print(f"{name} is {age} years old.")


# * 10. open()
# The open() function is used to open files for reading or writing, with various modes available.

# Writing to a file
with open('test.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("My name is Tim.\n")

# Reading from a file
with open('test.txt', 'r') as file:
    content = file.read()
    print(content)

# Appending to a file
with open('test.txt', 'a') as file:
    file.write("Appending a new line.\n")

# Reading line by line
with open('test.txt', 'r') as file:
    for line in file:
        print(line.strip())  # Strip any extra newlines