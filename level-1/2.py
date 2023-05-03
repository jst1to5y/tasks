"""
Create a python function that takes 2 numbers x,y and prints
all the numbers between 1 and 100 than can be divided on x,y
"""

# Solution 1
nums = []
def divided_on(x, y):
    for num in range(1, 101):
        if (num % x == 0) and (num % y == 0):
            nums.append(num)
    print(nums)


divided_on(3, 5)







