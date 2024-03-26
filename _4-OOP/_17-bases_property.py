"""
* The __bases__ property
*======================
__bases__ (double underscore bases double underscore) property of a class returns a tuple with all the base classes that the given class inherits from. 
	• The direct parent of the class

Classes with no base (The superclass) return `object`
"""

class Vechicle():
    pass

class Rideable():
    pass

class PetrolVehicle(Vechicle):
    pass

class Car(PetrolVehicle, Rideable):
    pass

# returns (<class 'object'>,)
print(Vechicle.__bases__)
print(Rideable.__bases__)

# returns direct parent
print(PetrolVehicle.__bases__)

# Only returns direct parents, not the superlclasses of the parents
print(Car.__bases__)