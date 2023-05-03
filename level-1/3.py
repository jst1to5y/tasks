"""
Create a python function that takes 2 numbers x, y and prints the multiplication table from x to y
"""
# Solution 1
def mult(x, y):
    for num in range(x, y+1):
        print(f"====== {num} ======")
        for i in range(1, 11):
            print(f'{num}*{i} = {num*i}')



mult(2,3)