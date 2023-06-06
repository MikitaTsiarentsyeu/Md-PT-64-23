# while True:
#     print("to infinity and beyond!")

x = 0
while x < 4:
    print(x)
    x += 1

test_str = "test str"
i = 0
while i < len(test_str):
    print(test_str[i])
    i += 1

for letter in test_str:
    print(letter)

for item in [1,2,3,4,5]:
    print(item)

for item in {1,2,3,4,5}:
    print(item)

# l = [1]
# for i in l:
#     l.append(i+1)
#     print(l)

x = 0
while True:
    if x == 10: 
        break
    x += 1
    if x % 2 == 0:
        continue
    print(x)

for letter in "test str":
    if letter == " ":
        break
        # continue
    print(letter)

for letter in "te,s.t s!tr":
    if letter in ",.!":
        # break
        continue
    print(letter)


l = [1,2,3,4,5]
for i in range(len(l)):
    print(l[i])

rng = list(range(10))
print(rng)

d = {}
for i, symbol in enumerate("test str"):
    d[i] = symbol

print(d)