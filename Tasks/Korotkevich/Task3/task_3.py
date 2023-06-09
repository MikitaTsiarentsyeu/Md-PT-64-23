stroka = input('Please enter the string: ').split(' ')
numbers = [i for i in range(1, len(stroka)+1)]
final_dict = {}
for x in numbers:
    final_dict[x] = stroka[x-1]
print(final_dict)
