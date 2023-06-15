list = input("Enter a list of numbers separated by spaces: ").split()
l = [int(i) for i in list]
print(sum(l)/len(l))