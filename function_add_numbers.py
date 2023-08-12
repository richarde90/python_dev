def add_numbers(*args):
    total = 1
    for num in args:
        total *= num
    return total

result = add_numbers(1,2,3)
print(result)