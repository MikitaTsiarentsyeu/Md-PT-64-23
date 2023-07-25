def reader ():
    try:
        with open (f'{input("Enter name file without specifying Extension ")}.txt') as f:
            s = f.read()
        print(s)
    except FileNotFoundError:
        print("File not found")
reader ()