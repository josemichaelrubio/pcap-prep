"""
* Methods
-------
Method is a function inside a class
Each method must have one parameter
	• this parameter can have any name, but should be named self by convention
	• Self parameter identifies the object for which the method is invoked
		○ self allows you to access properties and methods of the same object
When you invoke a method outside the class, you should never provide any argument for the self parameter, Python does that automatically 
If you need other parameters in your method, you need to place them after the self parameter in the function definition.
	• NOTE: Remember to skip first parameter since its self
Constructors had a special name: __init__
	• it is activated automatically for when ever you create a new instance
	• Return statements can be used in parameters
		○ NOTE: constructors returns objects automatically 
Parameters for the constructor can have default values
Methods can be private: add double underscore
	• `__method`
	• Name mangling occurs when accessing a private methods outside of the class
		○ use mangled name to access that private method
Using __dict__  on the class name, you will find the methods and properties

When we use the print() function for an object, the output will be an internal object identifier, it will be different for each object on each machine
	• __str__ = double underscore str double underscore
		○ How to get the properties of an object
		○ NOTE:
			§ must be named __str__ in the class definition
			§ must have one parameter = self
			§ must return a single value
"""

class Doctor():
    def __init__(self, first_name = 'John', last_name = 'Doe'):
        self.first_name = first_name
        self.last_name = last_name
        self.__formal_names()
    
    def __formal_names(self):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()

    def introduce(self):
        print(f'Hello, my name is {self.first_name} {self.last_name}.')
    
    def complete_name(self, name_to_compare):
        if self.first_name == name_to_compare:
            print('You are the same person.')
        else:
            print('You are not the same person.')
    
    def get_first_last_name_together(self):
        return f'{self.first_name} {self.last_name}'
    
    #* __str__ is a special method that is called when you use print() on an object
    def __str__(self):
        return f'Doctor: {self.first_name} {self.last_name}'

doc_alex = Doctor('AleXandeR', 'SMith')
doc_alex.introduce()
doc_alex.complete_name('John')
print(doc_alex.__dict__)
print(Doctor.__dict__)

# Getting the properties of an object using __str__ method and print()
print(doc_alex)