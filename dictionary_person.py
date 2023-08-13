person = { 
          "name":"Richard",
          "age":"30",
          "city":"Retford",
          "county":"Nottinghamshire"
}

print(person["name"]) #Prints dictionary name value
print(person["age"])

# Adding and Modifying Entries 

# Modifying
person["job"] = "Data Engineer"
person["age"] = '33'


print(person["age"])
print(person["job"])

# Removing Entries

del person["age"] # Removes key and associated values

# Search Dictionary

if "name" in person:
    print("Name is present in person dictionary")

# Creating a set - Sets are useful for union, intersection and difference for example.

fruits = { "apple", "banana", "cherry"}

# Add/Remove from Set
fruits.add("pineapple")
fruits.remove("apple")

print(fruits)


# Set Operations

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))  # {1, 2, 3, 4, 5, 6}
print(a.intersection(b))  # {3, 4}
print(a.difference(b))  # {1, 2}


# Dictionary Practice

book = {
    "title":"To Kill a Mockingbird",
    "author":"Harper Lee",
    "year":"1960"
}

print(book["title"])

# Colour Set Practice

colours = {"red", "green"}
colours.add("blue")
colours.remote("yellow")

"""Key Differences:
Duplicates: Lists allow them; sets don't.
Order: Lists maintain order; sets don't.
Access: You can access list items by index; you can't with sets.
Syntax: Lists use []; sets use {}.
When to Use Which?
Use a list when order matters, when you need to access items by index, or when you need to allow duplicates.
Use a set when you want to ensure all items are unique or when you need to perform set operations like union, intersection, and difference.
"""