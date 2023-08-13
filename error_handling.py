import traceback

try:
    print(1 + "2") # some code that raises an exception
except Exception as e:
    print(f"An error occurred: {e}")
    

try:
   print("Hello World")
except:
    traceback.print_exc()

