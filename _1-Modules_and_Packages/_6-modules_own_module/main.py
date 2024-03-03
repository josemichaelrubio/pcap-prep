import own_module

"""
When a module is imported, the code in the module is automatically executed, even print invocations.
That's why most modules only contain functions and variable definitions, and don't do anything on their own.
Each module is only initialized once, no matter how many times it's imported.
Each module has a special name created by Python, and it's stored in the __name__ variable.
    - if the module is run as a script or ran directly, __name__ is set to '__main__'
    - if the module is imported, __name__ is set to the module's name
Many modules use the name variable to decide whether to run tests or not
    - Good modules contain automated tests to verify whether the functions are working correctly
    - These tests are only run if the module is executed directly, not if it's imported

Public vs. private functions:
    - public functions are intended to be used by other modules
    - private functions are intended to be used only inside the module
    - private functions are preceded by an underscore
    - private functions are not imported when the module is imported
Python has no mechanism to enforce the privacy of a variable, but it's a convention:
    - if you see a variable start  with one or two underscores (__var or _var), you should not modify it
"""
