list = input("Enter a list of numbers separated by spaces: ").split()
first_largest = list[0] 
second_largest = list[0] 
for i in range(1,len(list)): 
    if list[i] > first_largest: 
        first_largest = list[i] 
    for i in range(1,len(list)): 
        if list[i] > second_largest and list[i] != first_largest: 
            second_largest = list[i] 
print(second_largest)
    