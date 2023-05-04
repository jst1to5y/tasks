"""
Get the names that contains 2 or more ‘a’ letter using [normal list - list comprehension - functional programming]
"""
names = ["mahmoud", "farida", "ali", "hassan", "mohamed", "khaled", "taha"]

# normal list
new_names = []
for name in names:
    if name.count("a") >= 2:
        new_names.append(name)

print(f"normal list: {new_names}")

# list comprehension
new_names2 = [name for name in names if name.count("a") >= 2]
print(f"list comprehension: {new_names2}")

# functional programming
new_names3 = list(filter(lambda name: name.count("a") >= 2, names))
print(f"functional programming: {new_names3}")