def symbol_search (string, counter=0):
    if len(string) == 0:
        return print (f"Number of occurrences of a given symbol: {counter}")
    if symbol == string[0]:
        return symbol_search(string[1:], counter+1)
    else:
        return symbol_search(string[1:], counter)
symbol = input("Enter symbol: ")
symbol_search(input("Enter string: "))