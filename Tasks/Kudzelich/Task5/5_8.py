def occurences(letter, string, index=0, count=0):
    if index > len(string)-1:
        return count
    else:
        if letter == string[index]:
            count +=1
        return occurences(letter, string, index+1, count)

letter = input("enter letter:\n")
string = input("enter string:\n")
print(f"there're {occurences(letter, string)} occurences of a given letter in a string")