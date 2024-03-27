"""
* The raise Keyword
*=================
Python raises exceptions automatically for us, however, we can also raise exceptions on our own.
Used for:
	• Writes tests to verify how a piece of code will behave
	• Make another part of the program handle responsible for handling the exception
		○ useful for large applications
`raise name_of_exception:`
`raise`

"""

def return_bigger(a,b):
    if not isinstance(a, int) or not isinstance(b, int):
        # manually raise an error
        raise ValueError
    if b > a:
        return b
    else:
        return a
    
def return_reverse(x):
    try:
        return 1/x
    except:
        print('something went wrong')
        # only want handle exception partically, and then you raise the exception again so that the other part of the code finishes the exception handling
        raise
