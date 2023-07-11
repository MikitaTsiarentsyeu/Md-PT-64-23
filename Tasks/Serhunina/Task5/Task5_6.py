#Write a recursive function to reverse a string.

def reverse_string(string):
    if len(string) == 0:
        return ""
    else:
        return reverse_string(string[1:]) + string[0]

string = "abcd"
reversed_string = reverse_string(string)
print(reversed_string)