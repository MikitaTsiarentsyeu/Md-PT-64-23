def open_a_file(name_of_file):
    try:
        with open(name_of_file, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"


print(open_a_file("test.txt"))
