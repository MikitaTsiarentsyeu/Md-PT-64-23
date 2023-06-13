user_input = input("Enter your string:\n")
# print(user_input.swapcase()) 
# :)

new_string = ""

for letter in user_input:
    if letter.isupper():
        new_string += letter.lower()
    else:
        new_string += letter.upper()

print(f"The converted string is", new_string)