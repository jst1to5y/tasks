"""
Create a python function that takes 2 numbers x,y and prints 2 lists containing
the odd and even numbers in the x,y range
"""
odd = []
even = []


def make_lists(x, y):
    for num in range(x, y + 1):
        if num % 2 != 0:
            odd.append(num)
        else:
            even.append(num)
    return f'Odd: {odd}\nEven: {even}'


print(make_lists(1, 10))

"""
#### Solution 2 ####
"""


def make_lists(x, y):
    odd = [num for num in range(x, y + 1) if num % 2 != 0]
    even = [num for num in range(x, y + 1) if num % 2 == 0]
    return f'Odd: {odd}\nEven: {even}'


print(make_lists(10, 20))
