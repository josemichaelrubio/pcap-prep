"""
* map() and filter() with Lambdas 
// ================================================
Two functions that accept Lambdas
	• map()
	• filter()

* map(function(), <sequence>) 
	• Typically takes two arguments: a function and a sequence with some elements
	• map() applies the function to all the elements in the sequence
	• Creates a structure called an iterator
		○ iterator = an object that allows you to retrieve the elements one by one in a loop to convert them to a list
		○ printing the iterator identifies where it is in memory
next() =output is the first element of the iterator, and it removes it from the iterator
	• if used subsequently, we get the following element
	• if a loop is used after the next() function to print the elements, the loop continues where the last next() left off.
list() = output from the iterator is saved into a list
	• If list() is used on a iterator that was previously iterated by next() or a loop, the output of the list are the left over from them or an empty list. 

* filter(<sequence>) 
	• filters the elements of a sequence
	• NOTE: `filter(lambda j : j <condition>, <sequence>)`
		○ lambda is used differently here
		○ lambda contains the condition that each matching element should satisfy 
	• created a new list that contains elements that are true from the lambda condition
	
NOTE: iterating over an same iterator will result in the left over elements of the previous iteration.

"""

lambda_func = lambda x: x *2
initial_list = [1, 2, 3, 4, 5]

#* map() function

# map() function returns a map object
print(map(lambda_func, initial_list))

map_result = map(lambda_func, initial_list)

# next() function
print(next(map_result))
print(next(map_result))
# NOTE: this loop continues from the last next() function
for elem in map_result:
    print(elem)

# list() function on a used map() function
# NOTE: this will print the remaining elements in the map_result from above, thus we get an empty list
print(list(map_result))

# StopIteration Error
#! print(next(map_result))

# list() function on an untouched map() function
map_list = map(lambda_func, initial_list)
print(list(map_list))

# StopIteration Error
# ! print(next(map_list))

# single line with map() and list()
print(list(map(lambda x: x**2, [1, 2, 3, 4, 5])))


#* filter() function

# filter() function returns a filter object
print(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))

# filter() function with list(), single line
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])))

filter_result = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
print(next(filter_result))  
print(list(filter_result))
for elem in filter_result:
    print(elem)
print(list(filter_result))

# StopIteration Error
#! print(next(filter_result))

emails = [
    'frank@gmail.com',
    'bob@outlook.com',
    '123445',
    'aaaaa'
]

# a list that contains elements with only an '@'
print(list(filter(lambda x: '@' in x, emails)))
