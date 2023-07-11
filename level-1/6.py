"""
Create a function that takes a sentence and word and remove the word from the sentence
"""

def remove_word(phrase, word):
    words = phrase.split(" ")
    new_sentance = []
    for w in words:
        if w != word:
            new_sentance.append(w) 
    print(" ".join(new_sentance))


remove_word("hi hello hi there hi ", "hi")

