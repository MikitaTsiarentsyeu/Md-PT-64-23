list = list(input("Enter a string list ").split())
print([i for i in list if (len(i)+1)>5])