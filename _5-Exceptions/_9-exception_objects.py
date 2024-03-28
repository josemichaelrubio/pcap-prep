"""
* Exceptions as Objects
*=======================
In Python, Exceptions are objects
Whenever an exception is raised, an object of the given exception class is created and it goes through all the branches of the try except block to find a matching branch

`as` keyword = extends except block to get more information from the raised expectation object
By default, the exception class implements a version of the __str__ (common in all objects)

Each exception class that inherits from the BaseException had a property called args
`args` is a tuple which contains all the arguments passed to the constructor
	• Python automatically adds an argument to the constructor if there was an exception raised and some detail about it. 

In Python, expectation classes can contain arguments
	• All the arguments passed to the constructor are added to the property
	• typically for containing details on why a given exception is raised.

"""

def return_bigger(a,b):
    try:
        if a > b:
            return a
        else:
            return b
    # Exception as e is a way to catch the exception and store it in a variable
    except Exception as e: # `e` can be named anything
        print(e)
        return None

print(return_bigger(1,'b'))

try:
    raise Exception('i don not like it', 'this is the second argument')
except Exception as e:
    # Example of args
    print(e.args)

try:
    1/0
except Exception as e:
    print(e.args)

