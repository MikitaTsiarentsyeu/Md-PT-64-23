value = [5]

def change_value():
    value[0] = value[0]+1

change_value()
print(value)

letters = []
target_str = "abcdef"
test_str = "test"
def reverse(t_s, i=None, clear=True):
    if clear:
        letters.clear()
    if i == None:
        i = len(t_s)-1
    if i < 0:
        return ''.join(letters)
    letters.append(t_s[i])
    return reverse(t_s, i-1, False)

print(reverse(target_str))
print(letters)
print(reverse(test_str))

test = "test"

def reverse():
    global test
    test = test[::-1]
    print(test)

print(test)