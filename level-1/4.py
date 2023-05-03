"""
Create a function that takes a sentence and prints the sentence without duplicated words
"""

def remove_duplicated(phrase):
    list_of_str = phrase.split(' ')
    new_list = []
    for s in list_of_str:
        if s not in new_list:
            new_list.append(s)
    print(" ".join(new_list))

remove_duplicated("this is not is not here this ")

