#Write a function that reads a file and returns its contents as a string. Handle the FileNotFoundError and return "File not found" if the file does not exist.

def read_a_file(t):
    try:
        with open (t, 'r', encoding='UTF-8') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"
    
print(read_a_file('new.txt'))