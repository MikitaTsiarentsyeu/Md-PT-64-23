#Write a recursive function to count the number of occurrences of a given character in a string.
def func(string, char):
    if len(string) == 0:
        return 0
    elif string[0] == char:
        return 1+func(string[1:], char)
    else:
        return func(string[1:], char)

print(func('Hello world', 'l'))
print(func('A horse, a horse my kingdom for a horse', 'o'))
print(func('Anny', 'n')) #how to count both types of letters lower and upper a?
print(func('Cat dog ', 'u'))

