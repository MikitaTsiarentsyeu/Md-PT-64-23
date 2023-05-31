x = 2

if x == 0:
    print("it's zero")
elif x == 1:
    print("it's one")
elif x == 2:
    print("it's two")
else:
    print("I don't know what it is")

# print((x == 0)*"it's zero"+(1-(x == 0))*"I don't know what it is")

if x >= 0:
    if x == 0:
        print("it's zero")
    # elif x > 0:
    else:
        print("it's positive")
else:
    print("it's negative")

print("the end")

if x > 0:
    print("it's positive")
else:
    print("I don't know what it is")

print("it's positive") if x > 0 else print("I don't know what it is")
res = "it's positive" if x > 0 else "I don't know what it is"

print("it's zero") if x == 0 else print("it's positive") if x >= 0 else print("it's negative")

