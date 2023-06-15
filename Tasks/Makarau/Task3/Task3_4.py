list = input("Enter a list of numbers separated by spaces: ").split()
num_list = [int(i) for i in list]
first_largest = num_list[0] 
second_largest = num_list[0] 
for i in range(1,len(num_list)): 
    if num_list[i] > first_largest: 
        first_largest = num_list[i] 
for i in range(1,len(num_list)): 
    if num_list[i] > second_largest and num_list[i] != first_largest: 
        second_largest = num_list[i] 
print(second_largest)
    