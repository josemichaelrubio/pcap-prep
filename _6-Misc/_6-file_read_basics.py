"""
* Text File Reading Basics
//================================================================================================
The whole code is enclosed in a try and except block because a lot can go wrong will file processing
	• Inside try:
		○ open file and assign to a variable
		○ process file
		○ variable.close()
			§ It is important to close every stream that you open, otherwise you run into memory problems very quickly
	• Inside except:
		○ How you want to handle the exception

.read(<number of bytes (characters)>) = most basic way to read the content of a file. 
	• By default, it returns the whole content of the file
	• You can also specify the number of bytes that should be read, and each byte typically means one character
		○ Once you read the specified number of bytes, the stream moves inside the file. Thus if invoked again (and the file was still open and not closed), you will see the next specified number of bytes
		○ If the stream reaches the end of the file, it returns an empty string
			§ NOTE: If you ask Python to read more bytes than there are in the file, nothing bad will happen. 
				□ Python will simply return the string with all the characters in file 
				□ the pointer in this stream will be set at the very end of the file
					® Any subsequent read call will return an empty string

read(1)
	• NOTE: Reading a file character by character protects us from against corrupting our OS in terms of very big files

.readline() =Reading files line by line
	• When it reaches the end of a line, it returns an empty string
	• NOTE: even though we instruct the print function not to put a new line character at the end of the print invocation, the lines are still shown in the output separated by new line characters
		○ Because each new line read from the file contains a new line character at the end by itself

.readlines() = reads all the file contents line by line and returns a list of strings, one string per line
	• NOTE: If you try this method on big files, there may be performance problems
	• It can also accept arguments with the suggested number of bytes to read at once
		○ If the number of suggested bytes is larger than the line, then it will continue onto the next line.
		○ If the number of suggested bytes is equal to the line, then it just be the line
		○ If the number of suggest bytes smaller than the line, then Python will increase the limit to the length of the line
	• If you get an empty list, it means that you've reached the end of the file
	• NOTE: This may increase performance compared to readline() But its more complicated

By default, the stream that you get by calling the open function is an object that is iterated
	• Iterable objects can be iterated using the for loop, like sequences 
	• The stream will return another line of the file in each iteration of the loop 
	• NOTE: You don't need to close the stream if you choose this technique.
		○ When you reach the end of the stream, Python automatically closes it for you
	• Much quicker and shorter because Python has ready-made solutions for you
"""
#* Basic template for opening, reading, and closing a file
try:
    stream = open('animals.txt')
    # your code goes here
    stream.close()
except Exception as e:
    print('An error occurred: ', e)

#* Example of a file that doesn't exist
try:
    stream = open('animalaaas.txt')
    # your code goes here
    stream.close()
except Exception as e:
    print('An error occurred: ', e)

#* Example of read()
try:
    stream = open('animals.txt')
    # read() method
    print(stream.read())
    stream.close()
except Exception as e:
    print('An error occurred: ', e)

#* Example of read(n)
try:
    stream = open('animals.txt')
    print(stream.read(10))
    print(stream.read(10))
    stream.close()
except Exception as e:
    print('An error occurred: ', e)

#* Example of reading a file character by character
try:
    stream = open('animals.txt')
    # read the first character
    character = stream.read(1)
    # check if the character is not an empty string ( end of file)
    while character != '':
        # print the character with a - after it
        print(character, end='-')
        # read the next character
        character = stream.read(1)
        # Once the end of the file is reached, the read() method will return an empty string and exit the loop
    stream.close()
except Exception as e:
    print('An error occurred: ', e)

#* Example of counting the number of characters in a file
try:
    stream = open('animals.txt')
    # counter
    counter = 0
    character = stream.read(1)
    while character != '':
        # increment the counter
        counter += 1
        print(character, end='-')
        character = stream.read(1)
    stream.close()
    print('\nNumber of characters in the file: ', counter)
except Exception as e:
    print('An error occurred: ', e)

#* Example of readline()
try:
    stream = open('animals.txt')
    counter = 0
    # readline() method
    line = stream.readline()
    while line != '':
        counter += 1
        print(line, end='-')
        line = stream.readline()
    stream.close()
    print('\nNumber of line in the file: ', counter)
except Exception as e:
    print('An error occurred: ', e)

#* Example of readlines()
try:
    stream = open('animals.txt')
    # readlines() method
    lines = stream.readlines()
    print('content of the file: ', lines)
    print('Number of lines in the file: ', len(lines))
    for line in lines:
        print(line, end='')
    stream.close()
except Exception as e:
    print('An error occurred: ', e)

#* Example of readlines(n)
try:
    stream = open('animals.txt')
    # readlines(n) method
    lines = stream.readlines(2)
    # If there are leftover characters
    while len(lines) != 0:
        # print the lines 
        for line in lines:
            print(line, sep='')
        
        lines = stream.readlines(2)
    stream.close()
except Exception as e:
    print('An error occurred: ', e)

#* Example of iterating over the stream object
try:
    stream = open('animals.txt')
    for line in stream:
        print(line, end='')
except Exception as e:
    print('An error occurred: ', e)