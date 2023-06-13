user_input = list(input("Enter strings separated by a space:\n").split())

new_list = []

for item in user_input:
    if len(item) > 5:
        new_list.append(item)
print(f"The list of strings with length greater than 5 characters is", new_list)