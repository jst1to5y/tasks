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


# Solution 2


def count_letters(phrase):
    new_str = ""
    for s in phrase:
        if s != " ":
            new_str += s
    print(len(new_str))

count_letters("is is is i")