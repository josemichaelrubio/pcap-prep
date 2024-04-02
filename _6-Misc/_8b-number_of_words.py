"""
NOTE: INSTRUCTOR VERSION:
* EXCERISE:
*Counting words in files
//====================================================================================================
Write a function that accepts two arguments: the name of a text file and a word:

`count_occurences(file_name, word)`

The function should return an integer number that denotes how many times the given word appears in the given file.

Note 1: Do not change the content of the text files. They are there to help you and to verify your solution.

Note 2: 'The', 'the' and 'THE' should all be counted as occurrences of the same word.
"""

def count_occurences(file_name, word):
    count = 0
    try:
        stream = open(file_name, 'r')
        for line in stream:
            words = line.replace('.', ' ').replace(',', ' ').split()
            for i in words:
                if i.lower() == word.lower():
                    count = count + 1
    except Exception as e:
        print('An error occurred: ', e)
    finally:
        stream.close()
    return count