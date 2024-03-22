"""
* Inheritance: Intro
---------------------
Inheritance = when one object or class is based on another object or class
Super classes contain subclasses.
`pass` = a placeholder since Python throws an error for empty blocks
`issubclass(subclass, superclass)` = check if a subclass is a subclass for a superclass
	• Subclasses of a subclass is also subclasses of the superclass
a class is a subclass of itself
"""

# Superclass
class Vechile:
    # `pass` is used to avoid error of empty class, Python requires at least one line of code
    pass

# `class Subclass(Superclass):` is the syntax for inheritance
class LandVechile(Vechile):

    pass

# Car is a subclass of landVechile and landVechile is a subclass of Vechile
class Car(LandVechile):
    pass

# issubclass() function is used to check if a class is a subclass of another class
print(issubclass(Car, Vechile)) # True
# subclasses of a subclass is also subclasses of the superclass
print(issubclass(LandVechile, Vechile)) # True
# a class is a subclass of itself
print(issubclass(Car, Car)) # True