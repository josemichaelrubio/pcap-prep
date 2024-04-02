"""

"""

# create an array of 100 bytes, initally all equal to 0
data = bytearray(100)
# set the first byte as the binary representation of 100
data[0] = 100
data[1] = 120

# write the binary file, create if none exists
try:
    # `wb` = write binary mode
    stream = open('binary_file.bin', 'wb')
    stream.write(data)
    stream.close()
except Exception as e:
    print('An error occurred: ', e)

# read the binary file
try:
    # `rb` = read binary mode
    bf = open('binary_file.bin', 'rb')
    byte_array = bf.read()
    bf.close()
except Exception as e:
    print('An error occurred: ', e)

print(byte_array)

# print the byte array in hexadecimal format
for byte in byte_array:
    print(hex(byte), end=' ')

# print the byte array in decimal format
for byte in byte_array:
    print(int(byte), end=' ')

# read first 10 bytes the binary file 
try:
    # `rb` = read binary mode
    bf = open('binary_file.bin', 'rb')
    byte_array = bf.read(10)
    bf.close()
except Exception as e:
    print('An error occurred: ', e)


