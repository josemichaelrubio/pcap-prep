"""
A Package is a container or a box for similar modules.
That way, you can easily organize modules into categories
To create a package in python, just create a folder and name it
You can have multiple folders at the same level,
or you can have folders inside folders which are treated as sub-packages in packages

__init__.py
    - Used to initialize the package
    - can be empty or have code
    - special file that tells Python that the folder is a package
    - Executed by python when any of the packages modules is or are imported
    - It is optional from python 3.3 and after,
        - in previous versions of python it was mandatory to include this file in order to be treated as a package
"""

import modules_own_module.project_modules.communication.com as com

com.my_fun()