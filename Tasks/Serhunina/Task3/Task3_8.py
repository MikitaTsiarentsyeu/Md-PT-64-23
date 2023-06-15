#Write a program that takes a list of numbers as input and returns the average of all numbers in the list.
user_input = input('Enter your numbers separated by space\n')
user_input = user_input.split()

to_list = [int(num) for num in user_input]

av = sum(to_list)/len(user_input)
print('The average of all numbers in the list:',av)