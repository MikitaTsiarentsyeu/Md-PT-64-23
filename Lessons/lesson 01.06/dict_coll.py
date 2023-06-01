d = {"one":1, "two":2, 3:"three"}

print(d["one"])
print(d["two"])
print(d[3])

d["two"] = 2.0
print(d)

d["test"] = [1,2,3]
print(d)

print(d.keys())
print(d.values())

print("two" in d.values())

# print(d['some key']) error
val = d.get("some key", "nothing was found")
print(val)