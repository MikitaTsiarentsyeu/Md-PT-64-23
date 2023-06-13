user_input = list(map(int,input("Enter numbers separated by a space:\n").split()))
sum = 0

for num in user_input:
    sum += num
print(f"The average of all numbers is", round(sum / len(user_input),2))