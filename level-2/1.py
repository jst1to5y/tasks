"""
1. Transform all names to uppercase using [normal list - list comprehension - functional programming]
"""
names = ["mahmoud", "farida", "ali", "hassan", "mohamed", "khaled", "taha"]
# Uppercase Normal list
upper_names = []
for name in names:
    upper_names.append(name.upper())

print(f"Normal list: {upper_names}")

# Uppercase list comprehension
upper_names = [name.upper() for name in names]
print(f"List comprehension: {upper_names}")

# Uppercase functional programming
def upperCase(x):
    return x.upper()


upper_names = list(map(upperCase, names))
print(f"Functional programming: {upper_names}")


# Functional programming 
new = map(str.upper, names)
print(list(new))
