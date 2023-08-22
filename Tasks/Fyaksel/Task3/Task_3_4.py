# Write a program that takes a list of numbers as input and returns the second largest number in the list.

list1 = input('Input numbers separated by space:\n')
list1 = list1.split()

list1 = [int (num) for num in list1]

mx = max(list1[0], list1[1])
second = min(list1[0], list1[1])
n = len(list1)
for i in range(2,n):
    if list1[i] > mx:
        second = mx
        mx = list1[i]
    elif list1[i] > second and \
        mx != list1[i]:
        second = list1[i]
    elif mx == second and \
        second != list1[i]:
          second = list1[i]
 
print("Second highest number is : ",\
      str(second))

