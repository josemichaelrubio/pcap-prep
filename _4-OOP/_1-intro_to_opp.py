"""
Introduction to OOP
--------------------
OOP = Object Oriented Programming
OOP was created to reflect the real world

Procedural Programming = There are procedures called functions in the Python language. We call functions that work on data.
	• An issue with Procedure Programming is that there are no restrictions. Any function can call any other function
	• It is usually used in small applications because it is quicker to write

In OOP, date and functions are kept in object.
	• Object = structure that has some data in the form of traits
		○ Traits = Data pieces inside objects inside objects called: 
			§ properties, attributes or fields
		○ Methods = functions inside of objects
	• Great for bigger programs

Class = a template for creating objects of the same type
	• The object has it's own data and function (method) defined within the class 
"""

# Procedural Approach
def calculate_area(width, height):
    return width * height
width = int(input('Enter width: '))
height = int(input('Enter height: '))
area = calculate_area(width, height)
print('Area:', area)

# Object-Oriented Approach
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
a = int(input('Enter width: '))
b = int(input('Enter height: '))
rectangle = Rectangle(a, b)
print('Area:', rectangle.calculate_area())
