"""
There is a special variable in Python called __path__ that is used to specify the location of the module.
Location is checked in the same order as the paths are listed in the sys.path list.
As soon as the module is found, the search stops.
If the module is not found, an ImportError exception is raised.
New locations can be added to the sys.path list at runtime.

Can add relative paths to the sys.path list, full address of the folder like "C:/Users/username/Desktop/Python/secret" or "C:\\Users\\username\\Desktop\\Python\\secret".
    - ..  goes up one level
    - \\ means a single backslash because \ is an escape character
Can add absolute paths to the sys.path list, but it's not recommended.

"""
import sys

# adds a new path at the end of the sys.path list
sys.path.append("secret")

# adds at a place of the list you want
sys.path.insert(0, "secret")

# prints all the paths where Python looks for modules
print(sys.path)

