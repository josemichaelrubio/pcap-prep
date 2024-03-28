"""
* Lambda Functions
//==================================================================================================
In Python, Lambda functions are used to simplify code to make it easier to understand
Differences of Lambda functions and regular functions
	• Regular functions always have a name
	• Lambda functions  can only contain a single instruction
	• Lambda functions are shorter than Regular Functions
	• Lambda Functions do not need the `return` keyword
Usefulness of Lambda functions:
	• Can be passed around like variables
	• It can work with many different Lambda types

Lambda functions are defined using the `lambda` keyword

Lambda can be saved in a variable or used directly
	• NOTE: Directly used lambda functions are not saved anywhere here, thus it is lost and cannot be reused later on
    
Lambda functions are also called:
	• Functions without names
	• Anonymous Functions
//==================================================================================================
"""

lambda a, b: a + b

#* Typical function
def add(a, b):
    return a + b

print(add(2, 3))

#* Lambda function
add = lambda a, b: a + b
print(add(2, 3))

#* Lambda function as a parameter
def apply_func(x, func):
    for elem in x:
        print(func(elem))

# Using a lambda function from a variable
func = lambda x: x**2
apply_func([1, 2, 3], func)

# Using a lambda function directly
apply_func([1, 2, 3], lambda x: x**2)
# NOTE: lambda is not saved anywhere here, thus it is lost and cannot be reused later on
