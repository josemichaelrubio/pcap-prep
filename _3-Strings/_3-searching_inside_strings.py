"""
Searching inside strings
------------------------
There are several methods that can be used to search inside strings.
The most common ones are:
    - index()
    - find()
    - rfind()
    - isalnum()
    - isalpha()
    - isdigit()
    - islower()
    - isupper()
    - isspace()
"""

#* index()
# index() - returns the index of the first occurrence of the specified value.
#   - raises an exception if the value is not found.
#   - can be used with various types of sequences (lists, tuples, strings, etc.)\
print('ilovetravelingaroundtheworld'.index('a'))

#* find()
# find() - returns the index of the first occurrence of the specified value.
#   - returns -1 if the value is not found.
#   - Only works with strings
#   - Has a one argument version, where the first argument is the value to search for.
#   - Has a two argument version, where the second argument is the index to start the search from.
#   - And a three argument version, where the third argument is the index to stop the search at.
print('ilovetravelingaroundtheworld'.find('z'))
print('ilovetravelingaroundtheworld'.find('a'))
print('ilovetravelingaroundtheworld'.find('a', 10))
print('ilovetravelingaroundtheworld'.find('a', 10, 20))

#* rfind()
# rfind() - returns the index of the last occurrence of the specified value. (short for right find)
#   - Similar to find(), but starts looking from the end of the string. 
#   - Has one, two, and three argument versions too
#       - one argument version, where the first argument is the value to search for.
#       - two argument version, where the second argument is the index to start the search from.
#       - three argument version, where the third argument is the index to stop the search at.
print('ilovetravelingaroundtheworld'.rfind('z'))
print('ilovetravelingaroundtheworld'.rfind('a'))
print('ilovetravelingaroundtheworld'.rfind('a', 10))
print('ilovetravelingaroundtheworld'.rfind('a', 10, 20))

#* isalnum()
# isalnum() - returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
print('ilovetravelingaroundtheworld'.isalnum())
print('ilovetravelingaroundtheworld123'.isalnum())
print('ilovetravelingaroundtheworld123!'.isalnum())

#* isalpha()
# isalpha() - returns True if all the characters are alphabet letters (a-z).
print('ilovetravelingaroundtheworld'.isalpha())

#* isdigit()
# isdigit() - returns True if all the characters are digits (0-9).
print('1234567890'.isdigit())

#* islower()
# islower() - returns True if all the characters are in lower case.
print('ilovetravelingaroundtheworld'.islower())

#* isupper()
# isupper() - returns True if all the characters are in upper case.
print('ILOVETRAVELINGAROUNDTHEWORLD'.isupper())

#* isspace()
# isspace() - returns True if all the characters are whitespaces.
print(' '.isspace())



