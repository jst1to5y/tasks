"""
Create a function that takes x,y and prints all the number that can be divided by y from x to 100
"""

# Solution 1
def divided_by_y(x, y):
    nums = []
    for num in range(x, 101):
        if num % y == 0:
            nums.append(num)
    print(nums)


divided_by_y(50, 3)

# Solution 2

def divided_by_y(x, y):
    nums = [num for num in range(x, 101) if num % y == 0]
    print(nums)


divided_by_y(50, 3)