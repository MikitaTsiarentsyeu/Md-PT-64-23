user_input = list(map(int,input("Enter numbers separated by a space:\n").split()))

for j in range(2):
    max_i = j
    current_i = j

    for i in range(j+1, len(user_input)):
        if user_input[i] > user_input[max_i]:
            max_i = i
    user_input[current_i], user_input[max_i] = user_input[max_i], user_input[current_i]

print(f"The second largest number in list is", user_input[1])
