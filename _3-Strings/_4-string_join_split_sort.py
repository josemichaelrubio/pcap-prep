"""
Joining, Splitting, and Sorting Strings
---------------------------------------
To remember:
    - join()
    - split()
    - sorted()
    - sort()
"""

# join()
# The join() = joins multiple strings into a single string
#   - the argument is a list of strings
print(' '.join(['This', 'is', 'a', 'sentence']))

# split()
# The split() = splits a string into a list of strings
#   - the argument is a delimiter
#   - if no delimiter is specified, the default is a space, newline, or tabulator
print('This\n is a\t sentence'.split(' '))

# sorted()
# The sorted() = sorts the elements of a list
#   - the argument is a list of strings
#   - Returns a new list with the elements in sorted order.
#   - original list remains unchanged
list_one = ['This', 'is', 'a', 'sentence']
list_sorted = sorted(list_one)
print(list_sorted)

# sort()
# The sort() = sorts the elements of a list
#   - the argument is a list of strings
#   - Returns the list in sorted order, no new list is created, the original list is changed
#   - the list is sorted in place
list_sort = ['This', 'is', 'a', 'sentence']
list_sort.sort()
print(list_sorted)
