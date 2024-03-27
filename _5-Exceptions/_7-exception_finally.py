"""
*The finally Keyword
*====================
`finally:` must be the last branch of the code intended for handling exceptions, even after else.
	• else and finally are not dependent on each other

General rule, the finally block is always executed

Typically used when working on external resources such as databases or text files

"""

def get_inverse(x):
    try:
        return 1/x
    except ZeroDivisionError:
        print ('There was an ZeroDivisionError')
    finally:
        print('I am always printed!')

print(get_inverse(5))
print(get_inverse(0))
