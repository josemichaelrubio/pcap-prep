# by convention, all imports go to the top
import sys #must use sys. namespace, bettet to use
# or import sys, math

# Aliases
# You can assign aliases to modules
import math as m  # or import math as m,
# You can also give aliases to entities in a module
# from sys import exit as bye_bye


# Very dangerous to import everything from a module
from sys import * # dont need to start with sys. namespace
# to omit the module name, use
#   from sys import exit
#   exit()
# however, this is not recommended as it can cause confusion.
# if you have a function called exit, the function will be called instead of the module's exit function

# how to print all the entities in a module
for name in dir(sys):
    print(name, end='\t')

def exit():
    print('Exiting...')

exit()
sys.exit()

