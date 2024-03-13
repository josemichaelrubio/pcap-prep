"""
Comparing Strings
-----------------
Comparing numbers:
	• ==
	• !=
	• >
	• >=
	• <
	• <=
"""

# Two strings are equal if and only if they are identical, case sensitive. 
print('Python' == 'Python')  # True
print('Python' == 'python')  # False
print('Python' != 'python')  # True
print('Python' == 'Java')  # False

# Python compares to characters at the same indexes based on their Unicode code points.
# When it finds two characters that are different, it compares them based on their Unicode code points.
print('Python' < 'python')  # True
print('Python' < 'java')  # True
print('Python' > 'Z')  # False

# If the two strings are identical except one is longer than the other, the longer string is considered greater.
print('Python' < 'Python3')  # True

# if your string is a number, it is still compared character by character.
print('10' < '2')  # True

# A String can never be equal to a number.
print('10' == 10)  # False
print('10' != 10)  # True

# If you try to compare a string with a number, you will get a TypeError.
print('10' < 10)  # TypeError: '<' not supported between instances of 'str' and 'int'






