"""
*Introduction to File Handling
//================================================================================================
Programs written in Python don't communicate with files directly, instead they use a couple of intermediates entities that will behave differently based on operating system
Handles/ Streams = the intermediate entities, Python makes them avilable to you so you don't have to worry about OS

Opening the File =Connect to a stream to the file
Closing the File = Disconnect the stream
In Python, when you open a file, Python creates a special kind of object. When you close it, Python destroys it.

There are different ways to open a file, thus different operations will be available

The Object to handle the file will come from: (IOBase = Superclass of these classes) RawIOBase, BufferedIOBase, and TestIOBase.

There are two kinds of files: text and binary
Text files = are handled with text streams
	• Files are read line by line
	• Each line typically contains characters such as letters, digits, punctuations
	• There is a character that denotes the end of a line, and that character Is different for each operating system.  BUT, Python handles this for us.
		○ Linux= \n
		○ Windows = \n or \r
Binary Files = 
	• files are read as sequences of bytes
		○ sequences can be images, audio files, video clips, executable programs, etc
			§ They don't contain lines
			§ They are read as portions of data, single bytes, or bigger blocks of bytes
"""

# No code to show here, just an introduction to file handling in Python