"""
* Multiple Inheritance
*======================
Multiple Inheritance = when a class has more than one superclass
	• A class inherits from more than one class
Syntax: provide all the subclasses separated by commas

Method Resolution Order (MRO) = explains how a given programming language tries to find the method that is currently needed
	• NOTE: Python looks for a method with a specific name in the following order:
		a. In the object itself
		b. In the super classes from left to right
		c. If not found, Raises an error

NOTE: General rule, avoid using multiple inheritance at all.
	• It gets very complicated
	• Many programming languages don't allow it
	• Use Single inheritance
Treat multiple inheritance as a last resort
"""

class Vehicle():
    def go(self):
        print('Going')
    
    def introduce(self):
        print('I am a Vehicle')

class Flyable():
    def fly(self):
        print('Flying!')
    
    def introduce(self):
        print('I am a Flyable')

# Inherits from two separate Superclasses
#* Also, example of MRO, 2nd step (left to right)
class Airplane(Vehicle, Flyable):
    pass

my_plane = Airplane()
my_plane.go()
my_plane.fly()
#* Method Resolution Order (MRO)
my_plane.introduce()