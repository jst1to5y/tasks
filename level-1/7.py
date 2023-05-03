"""
Create a function takes a sentence and a word and prints how many time the word used in the sentence
"""

def count_word(sentence, word):
    list_sen = sentence.split(" ")
    index = 0
    for i in list_sen:
        if i == word:
            index += 1
    print(f"Count of word ({word}): {index}")

count_word("hi hi hi ", "hi")
