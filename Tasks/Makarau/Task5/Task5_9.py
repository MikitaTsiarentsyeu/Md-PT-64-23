def degree (a, b, x):
    if b==0:
        return print(f"Result {x}") 
    if b !=0 :
        x *=a
        return degree (a, b-1, x)        
a = int(input("Enter number: "))
b = int(input("Enter the value of the degree: "))
degree(a, b, x=1)