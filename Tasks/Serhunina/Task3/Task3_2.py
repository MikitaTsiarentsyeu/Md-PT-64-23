#Write a program that takes a list of numbers as input and returns the sum of all even numbers in the list.

user_input = input('Enter your numbers separated by space:\n')
user_input = user_input.split()

user_input = [int(num) for num in user_input]
sum_of_even_numbers = 0

for numbers in user_input:
    if numbers %2==0:
        sum_of_even_numbers += numbers
print('The sum of even numbers is:', sum_of_even_numbers,'\n')
#how to count just even numbers?