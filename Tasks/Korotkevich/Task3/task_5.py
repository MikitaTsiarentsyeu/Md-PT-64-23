list_of_strings = input('Please enter the strings with space: ').split(' ')
new_list = []
for i in list_of_strings:
    if len(i) > 5:
        new_list.append(i)
print(new_list)
