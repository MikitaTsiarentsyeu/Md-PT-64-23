with open("test.txt", 'w') as f:
    f.write("test file\n")
    f.write("test file\n")
    f.write("test file\n")
    f.writelines(["test line 1\n", "test line 2\n", "test line 3\n"])
    # f.read() error

with open("test.txt", 'r') as f:
    # print(f.read())
    # print(f.readline())
    # print(f.readline())
    # print(f.readlines())
    # for line in f:
    #     print(line)
    print(f.read(2))
    print(f.read(2))
    print(f.read(2))
    print(f.read(2))
    f.seek(0)
    print(f.read(200))

with open("test.txt", 'a') as f:
    f.seek(0)
    f.write("appended text\n")

with open("test.txt", 'a+') as f:
    print(repr(f.read()))
    f.seek(0)
    print(repr(f.read()))
    f.write("appended text\n")

with open("test.txt", 'r+') as f:
    print(repr(f.read()))
    f.write("some text from r+\n")
    f.seek(0)
    print(repr(f.read()))
    f.seek(0)
    f.write("new text from r+")
    f.seek(0)
    print(repr(f.read()))

with open("test.txt", 'w+') as f:
    print(repr(f.read()))
    f.write("new content")
    f.seek(0)
    print(repr(f.read()))