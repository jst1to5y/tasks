"""
Print a list contains the len of each word in the list using [normal list - list comprehension -
functional programming]
"""
names = ["mahmoud", "farida", "ali", "hassan", "mohamed", "khaled", "taha"]

# normal list
length = []
for name in names:
    length.append(len(name))

print(f"normal list: {length}")

#  list comprehension
length2 = [len(name) for name in names]
print(f"list comprehension: {length2}")


# functional programming
length3 = list(map(lambda name: len(name), names))

print(f"functional programming: {length3}")