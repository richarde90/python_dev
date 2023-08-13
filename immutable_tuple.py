colours = ("Red", "Blue", "Yellow")
print(id(colours))
colours_2 = ("Purple")
print(id(colours_2))

colours = colours + colours_2
print(id(colours))

print(colours)
