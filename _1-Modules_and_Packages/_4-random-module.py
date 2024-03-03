# Provides random values
# Python offers pseudo-random numbers, which means that the numbers are generated by a fixed algorithm.
# Seed -> The seed is a number that is used to initialize the random number generator.
# If you use the same seed, you will get the same output. If you close the program and run it again, you will get the same output.
# Python uses the current time as the default seed.

import random
"""
 To know for PCAP:
   random.random() - returns a random float number between 0 and 1
   random.seed(x) - changes the default seed
   random.choice(seq) - returns a random element from the non-empty sequence.
       The sequence can be a list, a tuple, or a string
       doesn't care about duplicates
   random.sample(population, k) - returns a new list with k elements from the population
       takes two arguments: sequence and the number of elements to be chosen
       elements will always be unique
       If k is larger than the population, a ValueError is raised
"""

# random()
# produces a float number between 0 and 1
print(random.random())
print(random.random())

# seed()
# Seed function changes the default seed, so the random numbers can be reproduced (the same)
print(random.seed(0))
print(random.random())

numbers = [1, 2, 3, 4, 5]
names = ['Ana', 'John', 'Denise', 'Steve', 'Joe']

# choice()
# returns a random element from the non-empty sequence
print(random.choice(numbers))
print(random.choice(names))
# choice() doesn't care about duplicates
for i in range(5):
    print(random.choice(numbers), end=' ')

# sample()
# returns a new list with k elements from the population
# takes two arguments: sequence and the number of elements to be chosen
# elements will always be unique
# If k is larger than the population, a ValueError is raised
print(random.sample(numbers, 3))





