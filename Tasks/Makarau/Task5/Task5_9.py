def degree (a, b, x=0, counter=1):    
    if b==0:
        return print(f"Result {x}")  
    if b!=0:  
        x=a**counter      
        return degree (a, b-1, x, counter+1)    
a = int(input("Enter number: "))
b = int(input("Enter the value of the degree: "))
degree(a, b)