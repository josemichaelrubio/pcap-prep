"""
* Predefined Streams
//==================================================================================================
When you start a program in Python, there are actually three predefined streams that:
	• don't need any preparation
	• Are not associated with any files
	• Don't need to call the open function to get these 
	• Already made for you

To use the predefined steams, you must import the sys module

name of the three streams:
	• sys.stdin = Standard input
		○ By default, it reads user input from the keyboard, not from the file
		○ input()  reads data from this stream by default
		○ Rarely used directly, theoretically used to read input directly from console
	• sys.stdout = Standard output
		○ By default, the print function outputs the data to the stdout stream so it can be shown to the console 
		○ print()
		○ Rarely used
			§ can't use sep or end arguments
			§ can't provide more than one argument at all
			§ If you want to print an int using this technique, you have to turn it into a string first 
	• sys.stderr = standard error
		○ Similar to stdout
			§ useful results  produced by out programs should be directed to the stdout, while errors messages should be directed to the stderr
		○ NOTE: this is beyond the scope of the course
		
"""