def count_case(string, count_upper=0, count_lower=0):
    for letter in string:
        if letter.islower():
            count_lower += 1
        elif letter == " ":
            continue
        else:
            count_upper +=1
    print(f"{count_lower} symbols in lower case ", f"{count_upper} symbols in upper case ",  sep="\n")

count_case(input("Enter the string:\n"))