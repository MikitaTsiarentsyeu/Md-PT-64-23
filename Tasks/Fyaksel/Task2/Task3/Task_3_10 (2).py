# Write a program that takes a list of numbers as input and returns the largest prime number in the list.

numbers = list(map(int,input("Input numbers separated by a space:\n").split()))

for a in range(len(numbers)-1):
    max_a = a
    current_a = a

    for b in range(a+1, len(numbers)):
        if numbers[b] >numbers[max_a]:
            max_b = b
    numbers[current_a], numbers[max_a] = numbers[max_a], numbers[current_a]

for num in numbers:
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        continue
    else:
        print(f"The largest prime number in list is", num)
        break
