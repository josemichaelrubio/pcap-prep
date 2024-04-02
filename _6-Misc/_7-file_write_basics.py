"""
*Text File Writing Basics
//====================================================================================================
Simpler than reading files
what’s different is how we open the file
	• var = open('file.txt', 'w')
		○ the `w` instructs Python that you want to write into the file
			§ `w` = write mode
			§ NOTE: whenever we use the `w` mode Python ether creates the file for us or if the file already exists, then it will simply erases the content from it then put new content according to the code
				□ There are ways to add content to an existing file, but it will be discussed later
		○ if file.txt doesn't exist, Python will create one automatically for us
		○ NOTE: New line characters must be manually written 
Closing the stream is the same

write()
"""

# w mode will create a new file if it doesn't exist
try:
    stream = open('new_file.txt', 'w')
    stream.write('Hello World!\n')
    stream.write('This is a new file\n')
    stream.write('This is the third line\n')
    stream.close()
except Exception as e:
    print('An error occurred: ', e)

# w mode will erase the content of the file if it exists and replace it with the new content
try:
    stream = open('new_file.txt', 'w')
    stream.write('Hello again!\n')
    stream.write('We are writing on an existing file\n')
    stream.write('This will delete the content that was previously written here and replace it with this!\n')
    stream.close()
except Exception as e:
    print('An error occurred: ', e)

