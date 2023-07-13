def file_to_line(a):
    try:
        with open(a,'r',encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"
    
print(file_to_line('log.txt'))
