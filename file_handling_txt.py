file = open("example.txt","r") # R is read mode
file_output = file.read()
print (file_output)
file.close()

## Alternate method with implied close, with is also beneficial to generally close other resources too. Network, DB connections, files etc.

with open("example.txt", "r") as file:
    file_output_with = file.read()
    print(file_output_with)
    # File automatically closed. 
    
    
# Opening in write and writing into file.

with open("test_write.txt", "w") as file:
    file.write("This is a test of writing into a file with python!")
   
   
   
with open("test_write.txt", "r") as file:
    file_output_write = file.read()
    print(file_output_write)