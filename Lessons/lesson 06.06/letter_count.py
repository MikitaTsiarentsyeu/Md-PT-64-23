s = "iuhogih'ogihp ijpi jowih owhoh' "

d = {}
for symbol in s:
    if symbol in d:
        d[symbol] += 1
    else:
        d[symbol] = 1

print(d)

for key in d:
    print(f"{key}:{d[key]}")

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)