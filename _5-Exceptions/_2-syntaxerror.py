"""
* SyntaxErrors:
*================
If you raise a Syntax error manually, then you can catch it in the except block just fine

However, if you make a syntax error in the try block and Python automatically raises a SyntaxError for you, then you cannot catch it. 

"""

try:
    raise SyntaxError
except:
    print("Syntax Error caught")

'''
try:
    5:5 #* Syntax Error
except:
    print("Syntax Error caught") #* This will not print
'''