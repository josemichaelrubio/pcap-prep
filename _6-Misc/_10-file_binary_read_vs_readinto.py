"""
* Reading Binary Files: read() vs readinto()
//====================================================================================================
The read() method mentioned in the previous lesson reads all the contents of the file into the memory. This method creates an object of a special class called bytes (see variable newly_created below):

try:
	bf = open('file.bin', 'rb')
	newly_created = bf.read()
	bf.close()
except Exception as e:
	print('An error occured:', e)

The bytes class is very similar to bytearray that we mentioned in that video. 
NOTE: There is one difference: the bytes class is immutable (once created, it can't be changed).
If, for some reason, you need a bytearray object rather than a bytes object, you can simply wrap the bf.read() method call like this: bytearray(bf.read()). This will return a bytearray rather than a bytes object.
Another option to get a bytearray is to create it manually and then use bf.readinto(bytearray) instead of bf.read():

data = bytearray(10)
try:
    bf = open('file.bin', 'rb')
    bf.readinto(data)
    bf.close()
except Exception as e:
    print('An error occured:', e)
"""