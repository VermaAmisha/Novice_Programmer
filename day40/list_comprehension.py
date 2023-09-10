# Example 1: Creating a list of squares
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]

# Example 2: Creating a list of even numbers
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [2, 4]

# Example 3: Creating a list of strings with their lengths
words = ["apple", "banana", "cherry"]
word_lengths = [len(word) for word in words]
print(word_lengths)  # Output: [5, 6, 6]

# Example 4: Creating a list of uppercase letters from a string
text = "Hello, World!"
uppercase_letters = [char for char in text if char.isupper()]
print(uppercase_letters)  # Output: ['H', 'W']

# Example 5: Creating a list of tuples
x_values = [1, 2, 3]
y_values = [10, 20, 30]
coordinates = [(x, y) for x in x_values for y in y_values]
print(coordinates)
# Output: [(1, 10), (1, 20), (1, 30), (2, 10), (2, 20), (2, 30), (3, 10), (3, 20), (3, 30)]
