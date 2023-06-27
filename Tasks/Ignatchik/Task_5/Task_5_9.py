def exponentiation(number, power):
    if power == 1:
        return number
    else:
        return number*exponentiation(number, power-1)
    
print(exponentiation(2, 3))