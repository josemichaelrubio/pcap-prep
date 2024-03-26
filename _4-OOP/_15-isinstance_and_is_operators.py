"""
* isinstance() an 'is' operator
*===============================
`isinstance(object, Class)` = instance returns true if an object was created in a given class, AND returns true if the object was created from a subclass of the class

`is` operator = checks whether two variables point to the same object
	• NOTE: Variables store references to objects in memory, not stored in objects directly
		○ Objects Variables contain the address of an object in the memory, not in the object intself
	• For primitive variables:
		○ numbers: if value is the same, it returns true
		○ string
			§ NOTE: In Python, if two string variables contains the same values, the second variable actually points to the first string
			§ NOTE:  In Python, Strings are immutable, if you try to change a string, Python will just create a new string

`==` operator = returns true if the both variables contains the very same string value

"""

class Vechile:
    def __init__(self, speed):
        self.speed = speed

class LandVechile(Vechile):
    def __init__(self, speed, wheel_count):
        super().__init__(speed)
        self.wheel_count = wheel_count

class Car(LandVechile):
    pass

my_vechile = Vechile(4)
my_land_vechile = LandVechile(4, 4)
my_car = Car(4, 4)

#* isinstance() function:
print(isinstance(my_vechile, Vechile)) # True
print(isinstance(my_land_vechile, Vechile))  # True
print(isinstance(my_car, Vechile)) # True

print(isinstance(my_vechile, LandVechile)) # False
print(isinstance(my_land_vechile, LandVechile)) # True
print(isinstance(my_car, LandVechile)) # True

print(isinstance(my_vechile, Car)) # False
print(isinstance(my_land_vechile, Car)) # False
print(isinstance(my_car, Car)) # True

# Created a New object in memory: 
my_vechile = Vechile(60)

# Reference to the same object in memory:
my_new_vechile = my_vechile
#* is operator: 
print(my_vechile is my_new_vechile) # True
print(my_vechile.__dict__, my_new_vechile.__dict__)
my_vechile.speed = 100
print(my_vechile.__dict__, my_new_vechile.__dict__)

# Creating two new objects in memory with same values
my_vechile = Vechile(60)
my_new_vechile = Vechile(60)
print(my_vechile is my_new_vechile) # False
print(my_vechile.__dict__, my_new_vechile.__dict__)
my_vechile.speed = 100
print(my_vechile.__dict__, my_new_vechile.__dict__)

#* How is operator works with Primitive Data Types (Outside of OOP)
first_num = 5
second_num = 5
print(first_num is second_num) # True

first_string = 'Hello'
# This is a reference to the same object in memory
second_string = 'Hello'
print(first_string is second_string) # True

third_string = 'Hello World'
fourth_string = 'Hello Worl'
# since we modified the object, it is a new object in memory.
fourth_string += 'd'
# Even though the values are the same, the objects are different in memory
print(third_string is fourth_string) # False

#* == operator
print(third_string == fourth_string)