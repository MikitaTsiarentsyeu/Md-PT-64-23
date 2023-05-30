a = int(input("Enter the a value:\n"))
c = int(input("Enter the c value:\n"))

a, c, b = int(a), int(c), int((c*c-a*a)**0.5)

# b = int((c*c-a*a)**0.5)

print("The b value is", b)