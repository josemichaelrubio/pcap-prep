"""
Internal String Representation
--------------------------------
Character encoding: representing characters as numbers

string -> character encoding -> binary

There are standard encodings, 
ASCII = American Standard Code for Information Interchange
	• Most common
	• 256 characters, first 128 characters are the most significant
	• 1 ASCII character takes 8 bits (1 Byte)

Code Page= standard for using the remaining 128 code points for ASCII to store specific national characters
	• All code pages share the first 128 ASCII characters
	• The other 128 ASCII characters can be different depending on language

i18n = internationalization - the concept of finding a solution to a problem with multiple alphabets for multiple languages

Unicode= universal character encoding
	• No code pages
	• more than 1 million characters
	• first 128 characters are identical to ASCII
	• It's just a standard. It does explain how to code or store all the characters in the memory of your computer
	• It only lists all the available characters, each character can be planed in a plane
	• Plane = a group of similar characters
	• 17 different planes
		○ first plane is called basic multilingual plane
		○ second plane is the supplementary geographic plane for languages such as Japanese or Korean

More than one technique to implement Unicode and specific computers:
	• UCS-4 = Universal character set
		○ each character uses 32 bits (4 bytes)
		○ Problem (takes up a lot of space)
	• UTF-8 =
		○ Only uses as many bits for each character as they are needed (from 8 to 32 bits)
		○ compatible with ASCII
		○ Each ASCII character are 8 bits
		○ Most Non-Latin characters are 16 bits
		○ Chinese, Japanese, and Korean characters are 24 bits
		○ Fully supported by Python 
Can be used for input and output
"""