file = open("example.txt","r") # R is read mode
file_output = file.read()
print (file_output)
file.close()

## Alternate method with implied close, with is also beneficial to generally close other resources too. Network, DB connections, files etc.

with open("example.txt", "r") as file:
    file_output_with = file.read()
    print(file_output_with)
    # File automatically closed. 