string = input("Enter a string: ")
new_string = ""
for i in range(len(string)-1,-1,-1):
    new_string += string[i]
print(new_string)