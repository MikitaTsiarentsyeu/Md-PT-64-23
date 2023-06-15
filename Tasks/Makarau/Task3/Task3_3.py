string = input("Enter a string: ").split()
x={}
for i in string:
    l=string.count(i)
    x[i]=l
print(x)

