#Write a program that takes a list of numbers as input and returns the largest prime number in the list.
user_input = input('Enter your numbers\n')
user_input = user_input.split()

user_input = [int(num) for num in user_input]

l_prime = 0

for num in user_input:
    prime = True
    for i in range(2,num):
        if num%i==0:
            prime = False
            break
    if prime:
        if num > l_prime:
            l_prime = num
if l_prime ==0:
    print('lokh')
else:
    print('the largest prime number in the list', l_prime)    