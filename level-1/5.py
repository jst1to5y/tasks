"""
Create a function that takes a sentence and prints how many words in the sentence (do not count the spaces)
"""

# solution
def count_w(sentence):
    split_sentence = sentence.split(" ")
    print(f"Words count: {len(split_sentence)}")


count_w("hello there")


# Solution 2
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