file_name = input('Enter file name:\n')

def open_read_print(file_name):
    try:
        with open (f'{file_name}.txt','r') as f:
            lines = f.read()
            print('\n',lines,'\n')
    except FileNotFoundError:
        print('File not found')
    
open_read_print(file_name)

