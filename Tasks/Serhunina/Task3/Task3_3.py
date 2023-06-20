#Write a program that takes a string as input and returns a dictionary with the count of each word in the string.
user_input = input('Enter your string values\n')
user_input = user_input.split()

my_dict = {}

for word in user_input:
    value = user_input.count(word)
    my_dict[word] = value
    # if word in my_dict:
    #     my_dict[word] +=1
    # else: 
    #     my_dict[word] = 1
print(my_dict)

#There are 2 solutions for this task but could it be done via comprehension?