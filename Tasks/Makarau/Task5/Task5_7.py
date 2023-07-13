def polindrome (string):
    if len(string) == 0:
        return print("It's a palindrome")
    if string[0] == string[-1]:
        return polindrome (string[1:-1])
    else:
        return print("It's not a palindrome")
polindrome(input("Enter string: "))
    