"""
* Try… Except with Else
*=========================
Try… except blocks can also use `else`

else block gets executed if except block does not get executed
	• Else is run when no exception is raised in the try block
		○ try is executed followed by the else block if there are no exceptions

not common, but good to know.
"""

try:
    value = int(input('Enter an int: '))
    print(1/value)
except:
    print('Something went wrong')
# else example
else:
    print('Everything is perfect')
