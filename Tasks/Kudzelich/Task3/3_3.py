user_input = input("Enter your sentence:\n").split()

new_dict = {}

for key in user_input:
    value = user_input.count(key)
    new_dict[key] = value    

print(new_dict)

# Help me, please, how can I do this task using a comprehension, if it's possible? 