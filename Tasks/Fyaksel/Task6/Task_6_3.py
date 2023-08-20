# Write a function that takes a list of integers as input and returns the sum of all even numbers in the list. Handle the TypeError and return "Invalid input type" if the input is not a list or not every element is int.

def famix(namber):
    try:
        return sum(f for f in namber if f%2==0)
    except TypeError:
        return "Invalid input type"
    
print(famix('[0,1,2,3,4,5,6,7]'))
print(famix([1,10,18,45,0]))
print(famix([0,1,3,7,57,54]))
print(famix([27,69,54,33,21,90]))