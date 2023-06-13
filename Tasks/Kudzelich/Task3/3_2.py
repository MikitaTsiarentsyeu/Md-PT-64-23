user_input = list(map(int,input("Enter numbers separated by a space:\n").split()))
res = 0

for num in user_input:
    if num % 2 == 0:
        res += num
print(f"The sum of even numbers is", res)