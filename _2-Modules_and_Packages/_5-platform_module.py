"""
platform - Access to underlying platform’s identifying data
    - tells python version
    - tells OS
    - tells hardware you're running on

Program environment:
    1- your code
    2- Python
    3- OS
    4- Hardware
"""

import platform

"""
To know for PCAP:
    - platform() - returns a string that includes the system name, release, version, machine, and processor
        - intended to be user readable
        - it has default values: aliased=False, terse=False
        - takes two optional arguments:
            - aliased - if true, the function will return aliased system type, if false, it will return the system type
            - terse - if true, the function will return a short version of the platform name
    - machine() - returns the machine type, e.g. 'i386'
    - processor() - returns the processor type, e.g. 'i386'
    - system() - returns the system/OS name, e.g. 'Linux'
    - python_implementation() - returns the Python implementation, e.g. 'CPython'
        - CPython - written in C, the most popular implementation of Python
    - python_version_tuple() - returns the Python version, e.g. ('2', '7', '13')
        1: major version
        2: minor version
        3: patch level
"""

print(platform.platform())

print(platform.machine())

print(platform.processor())

print(platform.system())

print(platform.python_implementation())

print(platform.python_version_tuple())

