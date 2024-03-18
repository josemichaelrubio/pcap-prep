'''
Encapsulation and Abstraction
------------------------------
Private Property= a property that can only be access or modified within a class
	• Thus instantiated objects cannot modify private properties
	• This prevents users from changing property values of instantiated object
NOTE: different programming languages implement the concept of private differently than Python
In Python, to have a private property, you need to give it a name that starts with two under score signs `__property`

The four main principles of OOP:
	1. *Encapsulation* = Objects should keep their state private and only expose a set of public functions to the outside world
		a. Private properties
	2. *Abstraction* = Objects should keep the details of how they work to themselves and only expose some high level operations to the outside world
		a. Exposing methods to the outside world. These methods are capable of modifying Private properties 
	3. Inheritance
	4. Polymorphism
'''

class Car:
    # Default values can be set for the parameters
    def __init__(self, model, colour, initial_speed = 0):
        #* The __ prefix makes the attribute private
        self.__model = model
        # Private properties= hiding the state of the object from the outside world, example of Encapsulation
        self.__colour = colour
        if initial_speed < 0:
            self.__speed = 0
        else:
            self.__speed = initial_speed
    
    # Exposed methods to the outside world to manipluate private properties within the class, example of Abstraction
    def speed_up(self):
        self.__speed += 5
    def slow_down(self):
        if self.__speed < 5:
            self.__speed = 0
        else:
            self.__speed -= 5
    def show_speed(self):
        print(f'The speed of the car is {self.__speed} km/h')

# An example of a default value for an attribute
generic_car = Car('Generic', 'Black')

my_lovely_car = Car('T-Roc', 'Red', -50)

my_lovely_car.slow_down()
my_lovely_car.slow_down()

# since __speed is private, it cannot be accessed directly, thus modified below; nothing happens.
my_lovely_car.speed = -10

my_lovely_car.show_speed()


