import math

# how to print all the entities in a module
for name in dir(math):
    print(name, end='\t')
"""
For the PCAP, you should know the following functions: 
    ceil() - returns the smallest integer not less than x
    floor() - returns the largest integer not greater than x 
    trunc() - returns the integer part of x (remove the decimal part) 
    factorial() - returns the factorial of x= multiplication of all integers less than or equal to x 
    sqrt() - returns the square root of x. If x is negative, it returns a ValueError. Note that the result is a float 
    hypot() - returns the length of the hypotenuse of a right-angled triangle with the legs of length x and y
"""
# math.ceil(x) - returns the smallest integer not less than x
print(math.ceil(3.14)) # =4
print(math.ceil(-3.14)) # =-3

# math.floor(x) - returns the largest integer not greater than x
print(math.floor(3.14)) # =3
print(math.floor(-3.14)) # =-4

# math.trunc(x) - returns the integer part of x (remove the decimal part)
print(math.trunc(3.14)) # =3
print(math.trunc(-3.14)) # =-3

# math.factorial(x) - returns the factorial of x= multiplication of all integers less than or equal to x
print(math.factorial(5)) # =120

# math.sqrt(x) - returns the square root of x. If x is negative, it returns a ValueError. Note that the result is a float
print(math.sqrt(16)) # =4.0

# math.hypot(x, y) - returns the length of the hypotenuse of a right-angled triangle with the legs of length x and y
print(math.hypot(3, 4)) # =5.0


