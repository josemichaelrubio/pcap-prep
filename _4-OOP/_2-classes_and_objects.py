"""
Classes and Objects
-------------------
Objects cannot exist without classes
Classes are templates used to create objects
Classes contain two types of entity  
	• Attributes = variables
	• Methods = functions
Objects contain the attributes and methods of a class
Instantiate = Creation of a object from a class. 
Objects are instances of a class
"""
# When defining a class, we use the keyword `class`` followed by the class name and a colon `:`.
# The class name should always be written in Pascal case, capitalize each word.
class User:
    #* The constructor method is ALWAYS called `__init__` (double underscore init double underscore).
    #   - if you used any other name, Python would not recognize it as a constructor method.
    # It is called when an object is created from the class and it allows the class to initialize the attributes of the class.
    #* All Python constructors must have at lease one paramater, the convention is to call it `self`.
    #*   - `self` is always pointing to the object that you are currently creating within the constructor.
    #*   - 'self` always the first parameter of the constructor.
    def __init__(self):
        # In general, we use dots `.` in Python objects to refer to the attributes and methods of that object.
        self.nickname = 'sampleNickname'
        self.city = 'sampleCity'
    
    # Methods are functions that are defined within a class. Can have any name.
    # `self` parameter refers to the current object
    def introduce(self):
        # We use `self` and `.` to acess specific attributes of the current object
        print(f'Hello, my name is {self.nickname} and I live in {self.city}')

# Creating an object from the class
#   - variable = NameOfClass()
sample_user = User()
#* Note: even though the constructor has a paramater called `self`, we don't need to pass any arguments when creating an object from the class.
#   - Python automatically passes the object to the constructor when the object is created.'

# Calling a method from the object
#   - variable.method()
sample_user.introduce()

# Calling an attribute from the object
#   - variable.attribute
print(sample_user.nickname)

#* Providing our own values to the constructor
class User:
    # We added two parameters to the constructor, then we use these parameters to initialize the attributes of the class. 
    # Parameters name can be anything, you can even use the same name as the attribute, but it is a good practice to use different names.
    def __init__(self, user_nickname, city):
        self.nickname = user_nickname
        # Parameters name can be anything, you can even use the same name as the attribute, but it is a good practice to use different names.
        self.city = city
        #* `self.city` is different from the parameter `city`
        #   - `self.city` is refers to the property of the object
        #   - `city` refers to the arguement passed to the constructor
    def introduce(self):
        print(f'Hello, my name is {self.nickname} and I live in {self.city}')

# Now, when creating an object from the class, we need to pass the arguments to the constructor or we will get a TypeError.
sample_user = User('Dark Knight', 'Gotham City')
sample_user.introduce()
print(sample_user.nickname)

# Now that we have a class, we can instantiate as many objects as we want from that class.
first_user = User('John Doe', 'New York')
second_user = User('Jane Doe', 'Los Angeles')
third_user = User('Bruce Wayne', 'Gotham City')

first_user.introduce()
second_user.introduce()
third_user.introduce()