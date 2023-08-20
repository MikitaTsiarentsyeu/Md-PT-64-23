numbers = list(map(int, input("Enter ordered list of numbers: ").split()))

def my_ranges (numbers):
    res = str(numbers[0]) 
    for i in range(1,len(numbers)):
        if numbers[i] == numbers[i-1]+1: 
            if res[-1] !="-":
                res +="-"       
            if i == len(numbers)-1:
                res +=str(numbers[i])                       
        elif numbers[i] != numbers[i-1]+1:
            if res[-1] =="-":
                res += str(numbers[i-1])+", "+ str(numbers[i])
            else:
                res +=", "+str(numbers[i])
    return res    
print(my_ranges(numbers))



