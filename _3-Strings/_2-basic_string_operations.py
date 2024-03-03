"""
Basic String Operations
-----------------------
Python strings are immutable sequences
You can use len() to get # of characters
You can also use [] to access any character in a string, first character is index 0
Slicing to get a substring
Special Characters: put \ before them 
	• Not included in string length
	• Not encoded as a character internally
Multiline strings are allowed but be aware of the syntax: start and end string with ''' ''' (triple quotes)
	• line feet = \n
Strings can be concatenated: 
	• +, combines the strings into one
	•  *, multiples the number of strings into one
Operator Overloading = the same operator can be used for different kinds of data to produce different results
Commutative= Operator order doesn't matter when its just numbers. 
Not Commutative = It starts to matter when operator start to work with strings
Can iterate over a string
immutable = once you create a given string, you can't change it. It can only be replaced with a new string
	• Cannot use del, insert, or append to a string
Can use min() because if we convert all the characters into numbers according to the ASCII encoding, it gets that lowest number that represents a character in the string.
max() too
"""
# Strings are immutable sequences of characters
print(len('Hello World')) # 11
print(len('')) # 0

# Accessing characters in a string by index
print('Hello World'[1]) # e

# Slicing
print('Hello World'[1:]) # ello World
print('Hello World'[:5]) # Hello
print('Hello World'[1:5]) # ello

# \ is used to escape characters for special characters
print('I\'m a string') # I'm a string
# Not included in string length

# returns the Unicode code point for a one-character string
ord('a') # 97

# returns a string from an integer representing a Unicode code point
chr(97) # a

multi_line_string = '''Hello
World'''
print(multi_line_string) # Hello \n World
# there is a line feet `\n` character in the string that is included in the length too
print(len(multi_line_string)) # 12

# String Concatenation
# + operator
print('Hello' + ' ' + 'World') # Hello World
# * operator
print('Hello' * 3) # HelloHelloHello

for char in 'Hello':
    print(char, end=' ') # H e l l o

print(min('Hello')) # H
print(min('Hello World')) # (space)
print(max('Hello')) # o
print(max('Hello World')) # r