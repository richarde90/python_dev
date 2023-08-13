import traceback

def divide(a, b):
    return a / b

def main():
    numbers = [(10, 2), (5, 0), (8, 4)]

    for num1, num2 in numbers:
        try:
            result = divide(num1, num2)
            print(f"Result of {num1}/{num2} = {result}")
        except ZeroDivisionError as e:
            print(f"Error: {e} - Cannot divide {num1} by zero!")
            traceback.print_exc()  # Print detailed traceback for debugging
        except Exception as e:
            print(f"Error: {e}")
            traceback.print_exc()  # Print detailed traceback for debugging

main()
