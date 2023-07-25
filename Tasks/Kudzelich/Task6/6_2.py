def file_reader(file):
    try:
        with open (file, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"
    
print(file_reader("test.txt"))