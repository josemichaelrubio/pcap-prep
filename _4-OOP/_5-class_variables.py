'''
Class Variables
----------------
Class Variable = a property that exists in just one copy.
	• It is stored in the class itself but outside any object
	• It exists even if no objects are instantiated of that class
	• they are created outside of the constructor and within the class
	• Inside the class, To make a reference to a class variable inside the class, you need to use the class name then dot notation
	• Outside the class, you can reference a class variable like an instance variable
	• The value is same across all objects, if one instance changes the value, it changes the value of all

__dict__ will not display class variables because it only shows instance variables
Thus, to see the class variables, take a look at the class definition itself by using an existing object to print the class variable
If there are no instances of a class, you can still access the class variable using the name of the class
Note: there is a class variable with the same name as __dict__, it contains more info than the instance variable __dict__

Class Variables can be private, the effects are the same as instance variables. 
Thus to access a private class variable, you must use the mangled name

hasattr() = a way to determine if an object contains a specific instance or class variable
	• It cannot access instance variables, thus it cannot know if it's there or not

__name__ = returns the name of a class. It is a built in property.
	• Use case: combining name property and type function, the type of the function returns the type of an instance variable

__module__ = returns the name of the module that contains the definition of the class. 
	• It can be used for both objects and classes, the result will be the same
Note: If the class is defined in the same file, you will just see __main__
'''

class Dog():
    # Class variable
    counter = 0
    # Private class variable
    __private_counter = 0

    def __init__(self, name, age):
        self.__name = name
        self.age = age
        # Referencing the class variable within the class
        Dog.counter += 1
        Dog.__private_counter += 1

my_pet = Dog('Teddy', 2)
kates_pet = Dog('Foxy', 5)
adams_pet = Dog('Luna', 1)

# Accessing the class variable outside the class
print(my_pet.counter)
print(kates_pet.counter)
print(adams_pet.counter)

# Accessing the class variable using the class name
print(Dog.counter)

# Accessing the private class variable using mangled name
print(Dog._Dog__private_counter)

# __dict__ class variable
print(Dog.__dict__)

# hasattr() function: checks if an object has an instance variable
if hasattr(my_pet, 'name'):
    print('My pet has a name ', my_pet.name)
else:
    print('My pet does not have a name')

# hasattr() function: checks if an object has a class variable
if hasattr(Dog, 'counter'):
    print('Dog class has a counter variable')
else:
    print('Dog class does not have a counter variable')

# __name__ class variable with type() function
type(my_pet).__name__

# __module__ class variable
print(Dog.__module__)