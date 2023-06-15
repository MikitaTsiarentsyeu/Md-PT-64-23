list = input("Enter a list of numbers separated by spaces: ").replace(","," ").split()
even_nambers = [int(i) for i in list if not int(i) % 2]
print("Sum of all even numbers: ", sum(even_nambers))