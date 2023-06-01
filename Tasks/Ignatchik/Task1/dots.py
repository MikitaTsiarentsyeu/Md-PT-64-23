def presence_of_dots(string1):
    """A function that checks for the presence and number of points"""
    quantity = 0
    for i in string1:
        if i == '.':
            quantity += 1
    return True if quantity <= 1 else False