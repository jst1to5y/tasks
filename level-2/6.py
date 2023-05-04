"""
Unpack the list in
a,b , a= the first index , b = rest of the list
a = the first index , b = the last index
a = the first index , b = the second index
"""
names = ["mahmoud", "farida", "ali", "hassan", "mohamed", "khaled", "taha"]

# a,b , a= the first index , b = rest of the list
a, *b = names
print(f"1- {a}, {b}")

# a = the first index , b = the last index
a, *_, b = names
print(f"2- {a}, {b}")

# a = the first index , b = the second index
a, b, *_ = names
print(f"3- {a}, {b}")
