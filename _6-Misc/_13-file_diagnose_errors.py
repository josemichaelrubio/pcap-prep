"""
*Stream Errors
//==================================================================================================
Each error that we encounter when working with files has a specific number assigned =
To access that number:
	• Exception.errno 

To know what the error numbers mean: 
	• errno — Standard errno system symbols — Python 3.12.2 documentation

`from os import strerror`
	• Python also provides a function in the OS module that accepts the error number and then prints an explanation

NOTE: In practice, you don't need to work with error numbers
	• By default, when you print the exception, Python also includes a description of the error
NOTE: Error numbers could be useful when you want to check the specific kind of problem with handling your file and then react differentially to different problems

"""

from os import strerror

try:
    stream = open('non_existent_file.txt')
    stream.close()
except Exception as e:
    print('An error occurred: ', e)
    # Example of using the strerror() function from the os module and .errno attribute of the exception object
    print(strerror(e.errno))