"""
* Inheriting Class Variables and Methods
*=======================================
Class variables can be inherited the same way as instance variables, same syntax too
"""

class Vechile:
    class_message = "This is a message from the Vechile class"
    def __init__(self, speed):
        self.speed = speed

class LandVechile(Vechile):
    def __init__(self, speed, wheel_count):
        super().__init__(speed)
        self.wheel_count = wheel_count
        print(f"From superclass using super(): {super().class_message}")
        print(Vechile.class_message)

    def speed_up(self):
        self.speed += 10

class Car(LandVechile):
    def super_speed(self):
        print('Super Speed activated')
        super().speed_up()
        super().speed_up()
        super().speed_up()

my_car = Car(4, 4)
# Using dot notation to access the class variable
print(my_car.class_message)

my_fast_car = Car(10, 4)
print(my_fast_car.__dict__)
# Access the superclass method using dot notation
my_fast_car.super_speed()
print(my_fast_car.__dict__)

my_fast_car.speed_up()
print(my_fast_car.__dict__)