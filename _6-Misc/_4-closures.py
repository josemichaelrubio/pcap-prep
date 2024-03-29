"""
* Closures
#//===========================================================================\\#
A closure is a technique for implementing lexically scoped name binding in a language with first-class functions
	• It’s a function defined inside another function that remembers the values of the outer function

Nested function = functions can be nested within other functions like loops and if statements
	• Nested functions have access to variables in the outer function
Nested functions become closures the moment it references a variable from the outer function

In Python, whenever a pair of round brackets is added after a function name, it is called
	• Without round brackets, we only return the return value of the nested function 

NOTE: closure remembers the value of text, it knows something must be invoked when though it was not called. 
	• closures can store values from the outer functions, even though these functions have finished executing

Free variables = variables that should be already destroyed but are still available in a closure

Usefulness of closures:
	• Sometimes they can replace small classes (classes with one custom method)
		○ Makes them shorter to read
	• Ability to identify closures in Python libraries and design patterns when reading someone else's code
"""

def greet(text):
    # nested function
    def say_hello():
        # Nested function is now a closure
        print(text) # text is a free variable
    # NOTE: no brackets after say_hello: we don't want to invoke it, we want to return it
    return say_hello

say_hello = greet("Hello")
say_hello()

#* Another example
def make_multiplier_closure(x):
    def multiplier(y):
        return x * y
    return multiplier

# 3 is passed to x
times3 = make_multiplier_closure(3)

# 9 is passed to y
print(times3(9))