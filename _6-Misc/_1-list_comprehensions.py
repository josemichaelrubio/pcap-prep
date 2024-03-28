"""
* List Comprehensions
*==================*
NOTE: Serve as a recap from PCEP, since it is the same content

List comprehension is a way to write code with fewer lines:
	• `comprehension= [control_var for control_var range(<number>)]`
		○ the `control_var1 must be place up front too
	• `comprehension= [control_var for control_var range(<number>)  if <condition>]`
		○ if adds more control on what is added to the list
		○ no new line characters, no indentation.
	• `<true result> if <condition> else <false result> comprehension= [control_var for control_var range(<number>) ]`

List comprehensions Creates a list for us
It is a way to create a list on the fly, a shortcut
NOTE: Note needed and many programming languages don't have it

Nested list comprehensions = used to initialize a multidimensional list
	• `table = [[inner_var for inner_var in range(<number>)] for outer_var in range(<number>)]`
		○ NOTE: inner list comprehension used inner_var instead of outer_var before `for`
		○ NOTE: outer list comprehension replaces outer_var with the entire inner list comprehension
			§ repeat the inner list comprehension until outer_var reaches the value after `in`

"""

# Creates a list quickly BUT takes up more space
numbers_for =[]
for i in range(10):
    numbers_for.append(i)
print(numbers_for)

#* List comprehension
numbers_comprehension = [i for i in range(10)] # Creates a list for us
print(numbers_comprehension)

#* if 
skip_divisible_by_3 = [i for i in range(10) if i % 3 != 0]

#*  if else
# put 0 if the modulo division by two of i is 0, otherwise put 1 
alt_zeros_and_ones_with_total_100 = [0 if i % 2 == 0 else 1 for i in range(100)]

#* nested list comprehension
table = [[i for i in range(1,6)] for j in range(5)] # 
print(table)
# 