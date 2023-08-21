# Write a program that takes a list of numbers as input and returns the sum of all even numbers in the list.

myList = [1, 3, 5, 6, 8, 10, 34, 2, 0, 3]
result = 0
for item in myList:
    if not item%2:
      result += item

print ( myList, "The sum of all even numbers in the list", result)