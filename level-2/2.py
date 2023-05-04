"""
Get the names that contains ‘a’ in a list using [normal list - list comprehension - functional programming]
"""
names = ["mhmoud", "farida", "ali", "hassan", "mohamed", "khaled", "taha"]

# normal list
new_names = []
for name in names:
    if "a" in name:
        new_names.append(name)

print(f"normal list: {new_names}")

# list comprehension
new_names2 = [name for name in names if "a" in name]
print(f"list comprehension: {new_names2}")

# functional programming
def myFilter(x):
    if "a" in x:
        return x

new_names3 = list(filter(myFilter, names))
print(f"functional programming: {new_names3}")

# Lambda Function
new = list(filter(lambda name:  "a" in name, names))
print(f'Lambda Function: {new}')
