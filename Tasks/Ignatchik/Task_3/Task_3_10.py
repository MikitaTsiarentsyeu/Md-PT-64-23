input_list = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61,
            -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 
            79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74,
            -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11,
            -26, -62, -84]

def prime_number_2(enter):
    if len(enter)>0:
        enter.sort(reverse = True)
        for i in enter:
            count = 0
            for j in range(1, i+1):
                if i % j == 0:
                    count += 1
            if count < 3:
                res = j
                break
            elif count > 2 and len(enter) >= 1:
                res = 'no prime numbers found'
    else:
        res = 'no prime numbers found'
    return res
result = prime_number_2(input_list)
print(result)