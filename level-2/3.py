"""
Get the names that starts with ‘t’ in a list using [normal list - list comprehension - functional
"""

names = ["mahmoud", "farida", "ali", "hassan", "mohamed", "khaled", "taha"]

# normal list
start_t = []
for name in names:
    if name.startswith("t"):
        start_t.append(name)
print(f"normal list: {start_t}")

# list comprehension
start_t2 = [name for name in names if name.startswith("t")]
print(f"list comprehension: {start_t2}")

# functional programming
start_t3 = list(filter(lambda name: name.startswith("t"), names))
print(f"functional programming: {start_t3}")
