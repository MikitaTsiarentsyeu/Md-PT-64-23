#Write a function that takes a list of strings as an argument and returns a new list of strings that are all reversed.
def func(strings):
    my_list = []
    for i in strings:
        my_list_of_str = i[::-1]
        my_list.append(my_list_of_str)
    return my_list

strings = ['abcdef','123','loka']
reversed_version = func(strings)
print(reversed_version)        




def func (strings):
   
   return [s[::-1] for s in strings]
strings = ['foo', 'bar']
print(func(strings)) 