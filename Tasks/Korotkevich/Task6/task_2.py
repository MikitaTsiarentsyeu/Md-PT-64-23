import os
p = os.path.join('Md-PT-64-23', 'Tasks', 'Korotkevich', 'Task6')
os.chdir(p)


# while True:
#     name_file = input('Enter the name of file: ')
#     try:
#         with open(name_file, 'r') as f:
#             print(f.read())
#         break
#     except FileNotFoundError:
#         print('File not found')
#         print('Try again')
#         continue

def read_file(name_file):
    try:
        with open(name_file, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print('File not found')

read_file('text.txt')
print()
read_file('test.txt')