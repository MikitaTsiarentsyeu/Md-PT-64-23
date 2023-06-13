input_string = 'ASCII stands for American Standard Code for Information Interchange'

def number_of_vowels_1(enter):
    """A function that counts the total number of vowels in a string"""
    enter = enter.lower()
    vowel_list = ["a", "e", "i", "o", "u", "y"]
    count = 0
    for vowel in vowel_list:
        count += enter.count(vowel)
    return count
result = number_of_vowels_1(input_string)
print(result)

def number_of_vowels_2(enter):
    """A function that counts the number of unique vowels in a string"""
    enter = enter.lower()
    vowel_list = ["a", "e", "i", "o", "u", "y"]
    new_string = ''
    for vowel in enter:
        if vowel in vowel_list:
            new_string += vowel 
    res = len(set(new_string))
    return res
result = number_of_vowels_2(input_string)
print(result)