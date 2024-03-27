"""
* Exception Hierarchy
*=====================
NOTE: Python will raise the most specific exception it can
Python has 60 built in exception types
	• Don't need to memorize all for exam
	• Only understand general exception hierarch

1: 
	• BasicException = serves as a template for other more specific types
		○ Abstract/ Obstructive Exception = template exceptions that are not concrete
2: 
	• Exception = used as a template built in and coded exceptions
		a. ArithmeticError
		b. LookupError
			i. IndexError
			ii. KeyError
		c. TypeError
		d. ValueError 
		e. …
	• SystemExit = happen when `exit` method is called. Used to terminate a program manually 
	• KeyboardInterrupt = user enters a key combo that causes an interruption in executing script
	• …

"""

import sys

user_name = input("Enter your name: ")
if user_name == "":
    print("You did not enter a name")
    # SystemExit
    sys.exit()
print("Hello", user_name)
print("How are you today?")