#Write a function that takes a list of integers as input and returns the sum of all even numbers in the list. Handle the TypeError and return "Invalid input type" if the input is not a list or not every element is int.

def sum_of_even(args):
    try:
        return sum(i for i in args if i%2==0)
    except TypeError:
        return "Invalid input type"
    
print(sum_of_even([7,12,0]))
print(sum_of_even([7,5,3]))
print(sum_of_even([2,4,6]))
print(sum_of_even('[7,12,0]'))