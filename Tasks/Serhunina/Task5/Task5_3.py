#Write a function that takes a list of strings as an argument and returns a new list with all the strings that have a length greater than 5

def func(strings):
    list = []
    for s in strings:
        if len(s)>5:
            list.append(s)
    return list

strings = ['foo', 'bar','loloko','smile']
list = func(strings)
print(list)

#Is there a way to write smth like that(see below) and get the result like this ['loloko'] and not like this [False, False, True, False]?
# def func(strings1):
#     return [len(s)>5 for s in strings1]

# strings1 = ['foo', 'bar','loloko','smile']
# print(func(strings1))