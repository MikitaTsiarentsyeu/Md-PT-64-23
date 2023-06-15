import os

# with open("test.txt", "w") as f:
#     pass

print(os.name)
print(os.sep)
print(os.sep.join(['level 1', 'level 2', 'level 3']))

# "level 1/level 2/level 3/test.txt"

p = os.path.join('level 1', 'level 2', 'level 3')
print(p)

print(os.getcwd())
print(os.listdir())
print(os.walk(os.getcwd()))

for l in os.walk(os.getcwd()):
    print(l)

file_p = os.path.join(p, "test.txt")
os.remove(file_p)
os.removedirs(p)

# os.makedirs(p)
# os.chdir(p)
# print(os.getcwd())
# open("test.txt", 'w')
# print(os.listdir())

