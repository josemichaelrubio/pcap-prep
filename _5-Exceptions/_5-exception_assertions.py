"""
* Assertion Exceptions
*=======================
Two ways to raise exceptions for ourselves, but for the PCAP, you just need to know Assertions
Assertions = assumptions in our program that should always be true

USE Assertions:
	• Do:
		○ For debugging/ testing your code
		○ for documenting your code
	• Don't:
		○ Validate user input with assertions
		○ Handle Assertion Errors in `try…exception`

"""

def calculate_inverse(number):
    # after the `assert` keyword, we put one or more conditions inside the (condition)
    assert (number != 0), 'Got 0 as number'
    # If true, Python will move on the next line
    # If false, Python will show an error with the error message that we specify after the ,
    return 1/number