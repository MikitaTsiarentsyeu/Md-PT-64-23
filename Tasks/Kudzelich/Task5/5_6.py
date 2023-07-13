def reverse(string, new_string="", index=None):
    if index == None:
        index = len(string)-1
    if index < 0:
        return new_string
    new_string += string[index]
    return reverse(string, new_string, index-1)

print(reverse(input("enter the string:\n")))
