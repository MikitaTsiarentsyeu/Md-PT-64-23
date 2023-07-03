def get_ranges(numbers):
    res = []
    start = numbers[0]
    end = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i-1] == 1:
            end = numbers[i]
        else:
            if start == end:
                res.append(str(start))
            else:
                res.append(f"{start}-{end}")
                
            start = numbers[i]
            end = numbers[i]
    
    if start == end:
        res.append(str(start))
    else:
        res.append(f"{start}-{end}")
    
    return ", ".join(res)


user_input = list(map(int, input("enter numbers separated by space:\n").split()))
print(get_ranges(user_input))