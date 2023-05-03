"""
Create a function that takes a sentence and word and remove the word from the sentence
"""

def remove_word(phrase, word):
    list_phrase = phrase.split(" ")
    if word in list_phrase:
        list_phrase.remove(word)
    print(" ".join(list_phrase))


remove_word("hello hi there", "hi")

