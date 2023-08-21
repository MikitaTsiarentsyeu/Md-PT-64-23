# Write a program that takes a list of numbers as input and returns the average of all numbers in the list.

list_of_numbers = list(map(int,input("Inpyt numbers separated by a space:\n").split()))
sum = 0

for num in list_of_numbers:
    sum += num
print(f"The average of all numbers in the list", round(sum / len(list_of_numbers),2))
