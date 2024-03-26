"""
* Overriding Properties and Methods
*==================================
Method Overriding = When we define a method with the same exact name in the superclass and the subclass, the method from the superclass overrides (hides)
	• Subclass methods with the same name as methods in the superclass gets precedent
NOTE: when accessing a property or method in an object, Python will first try to find that entity inside the object itself. If it fails, then it tries to find it in the class starting from lowest subclass to the highest superclass
OPP principles:
	• Encapsulation
	• Abstraction
	*• Polymorphism = the ability of classes to take different forms
	• Inheritance
Usually when we talk about Polymorphism, we are talking about method overriding
"""

class Animal():
    def __init__(self):
        self.species = 'Animal'
    # Overridden Method
    def produce_sound(self):
        print('General animal sound')
    
    def present(self):
        print('I can do the following sounds: ')
        # This always refers to the current instance of the class, Thus, Python will look for the produce_sound method in the current instance
        self.produce_sound()
    
class Dog(Animal):
    def __init__(self):
        self.species = 'Canis Familiaris'

    #* Method overriding
    def produce_sound(self):
        print('Bark')

my_pet = Dog()
print(my_pet.species)
my_pet.produce_sound()

# Method Overriding results: 
my_first_pet = Animal()
my_second_pet = Dog()
my_first_pet.produce_sound()
my_second_pet.produce_sound()
print()

# Even though both objects use the present method, the output is different because they were created using different classes
my_first_pet.present()
my_second_pet.present()