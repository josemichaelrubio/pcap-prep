"""
Comparison: Instance, Class, & Local variables
------------------------------------------------
*instance variable overrides the class variable with the same name

General:
	• Class Variables
		○ `Class_Name.class_variable`
		○ declared outside of __init__ constructor 
		○ belongs to class, thus share the same value of all instantiated objects. 
		○ If an object modifies a class variable, it reflects on all its siblings
		○ Can be access outside of Class if not private
	• Instance Variable
		○ `object_name.instance_variable`
		○ declared within the __init__ constructor
		○ belongs to the instance of a class
		○ Can be access outside of the class if not private
	• Local Variables
		○ `local_variable`
		○ Can be declared anywhere
		○ Can only be accessed within the block it was declared

"""

class House():
    counter = 0
    def __init__(self, address, area, price):
        self.address = address
        self.area = area
        self.price = price
        House.counter += 1

        # Class variable
        House.quality = 'low'
        # Instance variable
        self.quality = 'medium'
        # Local variable = this variable only available in the __init__ method
        quality = 'high'

        # Printing within the class definition
        print(f'\nPrinting within the class definition:\n Class Variable: {House.quality} \n Instance Variable: {self.quality} \n Local Variable: {quality} \n\n')
    
    def present(self):
        print(f'Address: {self.address}, area: {self.area}, price: {self.price}')

soho_house = House('Blah st, Soho',130, 1000000)

# Printing outside the class definition
print(f'Printing outside the class definition: \n Class Variable: {House.quality} \n Instance Variable: {soho_house.quality} \n\n')

soho_house.present()
print(House.counter)