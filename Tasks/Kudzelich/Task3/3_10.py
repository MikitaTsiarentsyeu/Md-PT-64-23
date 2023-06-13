user_input = list(map(int,input("Enter numbers separated by a space:\n").split()))

for j in range(len(user_input)-1):
    max_i = j
    current_i = j

    for i in range(j+1, len(user_input)):
        if user_input[i] > user_input[max_i]:
            max_i = i
    user_input[current_i], user_input[max_i] = user_input[max_i], user_input[current_i]

#The remaining numbers no need to be checked, because if the numbers are not simple, then they have a divisor of 2,3,5 or 7
for num in user_input:
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        continue
    else:
        print(f"The largest prime number in list is", num)
        break