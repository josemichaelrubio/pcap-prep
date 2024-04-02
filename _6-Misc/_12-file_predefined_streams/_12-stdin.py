import sys

# It will read the input from the user until the user presses "q"
for line in sys.stdin:
    # rstrip() removes the trailing newline character 
    if line.rstrip() == 'q':
        break
    print(line)

print('You pressed "q" to exit the program.')