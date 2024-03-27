"""
* Introduction to Exceptions
*===========================*
Exceptions = an event which occurs during the execution of a program that disrupts the normal flow of the program instructions.

Syntax Errors like IndentationError
Value Errors

Python does not know what to do with exceptions, thus it raises an exception and stops the program

To handle exceptions, we use a try, exception structure

Gather exceptions that will occur, then add them to the exception blocks below the try
	• None of the exceptions can be repeated in the except blocks
	• If none of the exceptions covers the error that occurred, the program will stop
		○ Default Exception = must use the last general except block for all other exceptions not named in the blocks above that

"""

try: 
    # Where the error might occur
    value = int(input("Enter an integer:"))
    value = 1/value
    print(value)
except ValueError:
    # What to do if the error occurs
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    # Second exception block
    print("Cannot divide by zero.")
except:
    # Default exception
    print("An unknown error occurred.")

