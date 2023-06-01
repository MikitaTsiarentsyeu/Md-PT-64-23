potential_float = "1.23"

print(potential_float.count('.'))

# potential_float = potential_float.replace('.', '').replace(' ', '')
# print(potential_float)

if potential_float.isdigit() or (potential_float.count('.') == 1 and potential_float.replace('.', '').isdigit()):
    new_float = float(potential_float)
    print(type(new_float), new_float)
else:
    print("wrong number format")


test_str = "123_45_test"
split_res = test_str.split("_")
print(split_res)

potential_float = "1....23"
split_res = potential_float.split('.')
print(split_res)

print('/'.join(split_res))


potential_float = "1.23"

isValid = False

if not potential_float.isdigit():
    splt = potential_float.split('.')
    if len(splt) == 2:
        if splt[0].isdigit() and splt[1].isdigit():
            isValid = True
else:
    isValid = True

if isValid:
    new_float = float(potential_float)
    print(type(new_float), new_float)
else:
    print("wrong number format")

test_str = "SoMe StRiNg"
print(test_str.upper())
print(test_str.lower())

c, d, p = "cat", "dog", "python"

"a cat, a dog and a python"

res = "a " + c + ", a " + d + ", and a " + p
"a cat"
"a cat, a "
"a cat, a dog"
"a cat, a dog, and a "
"a cat, a dog, and a python"

pattern = "a {}, a {}, and a {}"
print(pattern.format(c, d, p))
print(pattern.format(p, c, d))

print(f"a {c}, a {d} and a {p}")