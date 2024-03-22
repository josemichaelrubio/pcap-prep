"""
* Reflection and Introspection
---------------------------
Introspection = ability of a program to check the type of an object or its properties at runtime
	• Allows you to get info about a given object during program execution
		○ All the properties that are available for a given object of any type of class
	• Like:
		○ __dict__
			§ key()
		○ getattr()
		○ isinstance()
Retrospection = ability of a program to change the properties or methods of an object at runtime
	• Like: 
		○ setattr()
"""

# Task: create a function that modified all string properties of any object by turning them into empty string

def empty_strings(user_object):
    # __dict__ property is built in dictionary containing all object's attributes
        # key() method is used to get all the keys from the dictionary
    for prop_name in user_object.__dict__.keys():
        # getattr() function is used return the value of the attribute of the given object
            # takes two arguments: object and name of the property 
        prop_value = getattr(user_object, prop_name)
        # isinstance() function is used to check if the object is an instance of the class
            # takes two arguments: variable and type (or custom class name)
        if isinstance(prop_value, str):
            # setattr() function is used to set the value of the property of the object
                # takes three arguments: object, name of the property, and new value
            setattr(user_object, prop_name, "")

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
    
    def __str__(self):
        return f'Doctor: {self.first_name} {self.last_name}'

doc_alex = Doctor('Alexander', 'Smith')
doc_alex.introduce()
empty_strings(doc_alex)
doc_alex.introduce()