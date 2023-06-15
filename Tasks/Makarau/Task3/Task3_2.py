list = input("Enter a list of numbers separated by spaces: ").split()
num_list = [int(i) for i in list]
even_nambers = [i for i in num_list if not i % 2]
print("Sum of all even numbers: ", sum(even_nambers))