def fibonaccio(n,a=0,b=1):
    if n==1:
        return print(a)
    if n>0:
        a, b = b, a + b
        return fibonaccio (n-1,a,b)
n=int(input("Enter number: "))    
fibonaccio (n)    