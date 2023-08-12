def multiply_numbers(*args):
    accumulator = 1
    for arg in args:
        accumulator *= arg
    return accumulator

result = multiply_numbers(2,3,4)
print(result)

