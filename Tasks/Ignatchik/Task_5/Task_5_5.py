list_input = [0, 1, 2, 3, 4, 7, 8, 10]

def get_ranges(numbers):
    ranges = []
    start = numbers[0]
    end = numbers[0]
    
    for num in numbers[1:]:
        if num == end + 1:
            end = num
        else:
            if start != end:
                ranges.append(f"{start}-{end}")
            else:
                ranges.append(str(start))
            start = end = num
    
    if start != end:
        ranges.append(f"{start}-{end}")
    else:
        ranges.append(str(start))
    
    return ', '.join(ranges)

print(get_ranges(list_input))