"""
*Diamond Problem
*=================
..->A->B->C->D->A..
Another issue with multiple inheritance: Diamond problem
	• A situation in which, due to the class hierarchy, it is not clear which method version should be used
	• There are at least two methods for inheriting in the subclass
Different programing languages have different approaching to this problem
	• In Python, it is resolved with Method Resolution Order (MRO)
		Method Resolution Order (MRO) = explains how a given programming language tries to find the method that is currently needed
			• NOTE: Python looks for a method with a specific name in the following order:
				a. In the object itself
				*b. In the super classes from left to right
				c. If not found, Raises an error
	
"""
class Vehicle():
    def show_power_type(self):
        print('I can use power from various sources.')

class ElectricVehicle():
    def show_power_type(self):
        print('I can use power from electricity')

class PetrolVehicle():
    def show_power_type(self):
        print('I can use power from petrol')

# The order here determines which method it will inherit from.
class HybridVehicle(ElectricVehicle, PetrolVehicle):
    pass

my_toyota_yaris = HybridVehicle()
my_toyota_yaris.show_power_type()
