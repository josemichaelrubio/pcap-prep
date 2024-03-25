"""


"""

#* A Class with no constructor
#* ===========================
class Vechile:
    pass

class LandVechile(Vechile):
    pass

class Car(LandVechile):
    pass

my_car = Car()
# the object is empty `{}` due to no constructor 
print(my_car.__dict__)

#* The Superclass with a constructor
#* ================================
class Vechile:
    def __init__(self, speed):
        self.speed = speed

class LandVechile(Vechile):
    pass

class Car(LandVechile):
    pass

# my_car = Car()
#NOTE: We get a TypeError since we are missing one required positional argument `speed`
# print(my_car.__dict__)

my_car = Car(4)
print(my_car.__dict__)

#* The Superclass & Subclass with a constructor
#* ===========================================
class Vechile:
    def __init__(self, speed):
        self.speed = speed

class LandVechile(Vechile):
    # This constructor superseeds the constructor of the superclass
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count

class Car(LandVechile):
    pass

my_car = Car(4)
print(my_car.__dict__)

#* Obtain the properties of the superclass with a sublcass constructor 
#* =================================================================
class Vechile:
    def __init__(self, speed):
        self.speed = speed

class LandVechile(Vechile):
    # The Constructor needs the parameters of the superclass
    def __init__(self, speed, wheel_count):
        # We call the superclass constructor with the required parameters
        # Vechile.__init__(self, speed)
        #- However, it is better to use the `super()` function
        super().__init__(speed)
        self.wheel_count = wheel_count

class Car(LandVechile):
    pass

my_car = Car(4, 4)
print(my_car.__dict__)

# Calling an instance variable from the superclass 
print(my_car.speed)