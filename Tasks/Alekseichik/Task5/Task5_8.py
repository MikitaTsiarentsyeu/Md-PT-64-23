text = 'count "char" in this sting'

char = 'i'

def occurrences (text,char,counter=0):
    if char in text:
        counter += 1
        return counter + occurrences(text[text.index(char)+1:],char)
    else:
        return 0
    
print(f'found "{char}" {occurrences(text,char)} times')