"""
* Exceptions as Objects
*================================
Exceptions are classes like any other, thus you can use inheritance to create nuances
Put the name as the chosen exception class as the superclass of your own exception
	• If you want to create an exception that will be a special case of an exception already available in Python, use that one particular Python exception as the superclass
	• For bigger applications, it's best to use a more general Python exception as a superclass
NOTE: you don't need to provide any specific content for the new exception type
	• Everything we is inherited from the Python Exception superclass
NOTE: You can pass arguments to the constructor, the created exception inherits the constructor from the Python Exception superclass

__str__ can be overridden to return a custom message

We can also create our own exception class structure
We can inherit from custom exceptions to create more specific exceptions

"""
#* Example of a specific custom exception
#*=======================================
class AnimalValueError(ValueError):
    pass

def produce_animal_sound(animal_type):
        if animal_type == "cat":
            print("Meow")
        elif animal_type == "dog":
            print("Woof")
        else:
            raise AnimalValueError("Animal not found")
try:
    produce_animal_sound("cat")
    produce_animal_sound("dog")
    produce_animal_sound("bird")
except AnimalValueError as e:
    print(e)

#* Example of a  custom exception with a more general exception superclass
#*===========================================================================
class UserActionException(Exception):
    # enables user to provide two specific arguments
    def __init__(self, message='', user_id=''):
        # Call the base class constructor
        Exception.__init__(self)
        # Now our custom exception has two properties
        self.user_id = user_id
        self.message = message
    # Override the __str__ method to return a custom error message
    def __str__(self):
         return type(self).__name__ + ": " + self.message + " for user " + self.user_id

def say_hello(name, user_id):
    if name == "":
        raise UserActionException("User ID is empty", user_id)
    print("Hello", name)

try:
    say_hello("Adam", "DT111")
    say_hello("", "DT112")
except Exception as e:
    print(e)

#* Example of a custom exception inheriting from a custom exception superclass
#*=============================================================================
class EmptyNameUserActionException(UserActionException):
    def __init__(self, user_id=''):
        # UserActionException.__init__(self, user_id)
        super().__init__(user_id) 
        # We don't need to provide the message because the superclass has one that is adequate

def say_hello(name, user_id):
    if name == "":
        raise EmptyNameUserActionException(user_id)
    print("Hello", name)
