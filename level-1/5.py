"""
Create a function that takes a sentence and prints how many words in the sentence (do not count the spaces)
"""

# Solution 1
def count_letters(phrase):
    index = 0
    for i in phrase:
        if i != " ":
            index += 1
    print(index)

count_letters("is is is is")