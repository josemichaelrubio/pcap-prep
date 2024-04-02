"""
* File Handling Modes
//====================================================================================================
Built-in Functions — Python 3.12.2 documentation:
https://docs.python.org/3/library/functions.html#open

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
	• Most important is the first and second arguments
		○ first is the file
		○ second is the mode
			§ default is `r

----------------------------------------------------------------------------------------------------	
Character	Meaning
----------------------------------------------------------------------------------------------------
'r'	open for reading (default)
'w'	open for writing, truncating the file first
'x'	open for exclusive creation, failing if the file already exists
'a'	open for writing, appending to the end of file if it exists
'b'	binary mode
't'	text mode (default)
'+'	open for updating (reading and writing)
----------------------------------------------------------------------------------------------------	
    •  You can use a combo of these characters like:
		○ open('filename', 'r+b')
			§ open file as binary in the read mode but also allow writing without deleting the existing content
		○ open('filename', 'w+')
			§ open file as text in write mode but also allow reading its content
"""