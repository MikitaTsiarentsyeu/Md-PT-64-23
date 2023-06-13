user_input = list(input("Enter strings separated by a space:\n").split())

print([item for item in user_input if len(item)>5])