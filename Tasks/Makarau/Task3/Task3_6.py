string = list(input("Enter a string: "))
for i in string:
    if i in "aeiouAEIOU":
        string.remove (i)
print(str("".join(string)))