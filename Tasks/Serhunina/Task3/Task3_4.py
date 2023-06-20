#Write a program that takes a list of numbers as input and returns the second largest number in the list.

user_input = input('Enter your numbers separated by space:\n')
user_input = user_input.split()

user_input = [int (num) for num in user_input]

first_l = user_input[0]
second_l = user_input[0]

for number in user_input:
    if number > first_l:
        second_l = first_l
        first_l = number
    elif number>second_l and number!=first_l:
        second_l = number
print('The second largest number in the list is:', second_l)