sample_story = '''Once upon a time, there was a beginner programmer named Alice who was eager to learn Python. She tried to learn from books, but found it difficult to grasp the concepts. One day, she stumbled upon an online course.

Alice was thrilled. The course was taught by a well-known programmer who made the lessons interesting and easy to understand. The course covered everything a beginner programmer needed, and Alice was finally able to understand how to code in Python.'''

def get_longest_word (sentence):
    words = sample_story.replace('.', ' ').replace(',', ' ').split()
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    print(longest_word)
    return longest_word

get_longest_word(sample_story)


    
    