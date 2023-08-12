# Example of building a function, defines greet where the parameter is name and outputs an f string with the greeting and dynamic name. 

def greet(name="User"):
    print(f"Hello, {name}!")

greet()          # This will print "Hello, User!"
greet("Alice")   # This will print "Hello, Alice!"