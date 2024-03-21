"""
* Can you have a default value for the self constructor parameter?
--------------------------------------------------------------
A tricky question that you may encounter in the exam is the following: 
    - can you provide a default value for the first parameter of a constructor (typically name self)?

The answer is: you can do that, but the value will be simply ignored by Python.
"""

class Car():
  def __init__(self='default value', speed=100):
    self.speed = speed
 
my_toyota = Car()
print(my_toyota.speed)   # default value for self ignored