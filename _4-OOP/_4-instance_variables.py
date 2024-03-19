"""
Instance Variables
------------------
Once you create an object, Python allows you to add new properties or remove existing ones
	• use dot notion to add a new property
	• del to delete existing properties
Note: 
	• Be aware that different objects of the same class can have different properties
	• Each object has its own set of properties with its own values. 
		○ Instance Variables= The properties of one object don't interfere with the properties of another object. They are unique to their respective object
		○ Instance = another name of an object

Object created in Python are automatically given a few properties and methods, here is one:
	• __dict__ = double under score dict double under score. 
		○ It's an instance variable that shows all the currently available properties of its object
		○ It changes when we add and delete properties
		○ The instance variable to available with any object, Python automatically adds this for you

Name Mangling = When a private variable is called from the __dict__ instance variable, it is presented in a twisted manner. 
To call a private variable outside of the class, we must use the mangled name instead of the name given in the class. Otherwise we get an `Attribute Error`
	*• Note: Making a property private is limited, it can still be called outside of the class with the mangled name Python Creates
		○ Thus, we need to use the mangled name as warning for the User not to proceed
		○ However, there is no way to stop the user to continue to user it outside the class
Note: Name Mangling only works if you use the double underscore prefix outside of the class.
If you try to add a property with a name that has the double underscore prefix outside of the class, name mangling doesn't happen, the double underscore is just two characters in the name of the property
"""

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_pet = Dog("Rex", 5)
# __dict__ example
print(my_pet.__dict__)

# We just added a propertry, colour, that wasn't defined in the __init__ method
my_pet.colour = "brown"
print(my_pet.__dict__)

# del example 
del my_pet.name
print(my_pet.__dict__)

#* Calling Private Variables outside the class
class Dog():
    def __init__(self, name, age):
        self.__name = name
        self.age = age

my_pet2 = Dog("Rex", 5)

# Name Mangling example
print(my_pet2.__dict__)
print(my_pet2._Dog__name)