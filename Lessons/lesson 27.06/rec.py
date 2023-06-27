test_str = "abcdef"

def reverse(target_str, result="", index=None):
    if index == None:
        index = len(target_str)-1
    if index < 0:
        return result
    # print(target_str[index])
    result += target_str[index]
    return reverse(target_str, result, index-1)

reversed = reverse(test_str)
print(reversed)

# 5! = 5*4*3*2*1 = 5*4!
# 4! = 4*3*2*1 = 4*3!
# 3! = 3*2*1 = 3*2!
# 2! = 2*1
# 1! = 1

def factorial(n):
    if n <= 1:
        return 1
    res = factorial(n-1)
    return n*res

print(factorial(5))

n = 1234 # -> 10

def digit_sum_str(num, i=0, res=0):
    str_num = str(num) if isinstance(num, int) else num
    if i == len(str_num):
        return res
    res += int(str_num[i])
    return digit_sum_str(str_num, i+1, res)

print(digit_sum_str(n))

def digits_sum(num):
    if num == 0:
        return 0
    return (num % 10)+digits_sum(num // 10)

print(digits_sum(n))