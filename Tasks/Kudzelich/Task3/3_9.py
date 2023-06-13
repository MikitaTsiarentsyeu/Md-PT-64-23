user_input = input("Enter your string:\n")
new_string = ""

for letter in user_input:
    new_string = letter + new_string
print(f"The reversed string is", new_string)