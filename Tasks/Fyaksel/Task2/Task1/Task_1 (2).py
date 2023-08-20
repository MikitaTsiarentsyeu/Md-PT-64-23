# converts Celsius to Fahrenheit

celsius = float(input("Enter temperature in celsius (>!= −273,15 °C):\n")) #Absolute zero temperature
print("         degrees celsius\n")
fahrenheit = (celsius * 9/5) + 32
print('%.2f °C = %0.2f °F \n' %(celsius, fahrenheit))

#print("{0} degrees celsius = {1} degrees fahrenheit ".format(celsius, fahrenheit))




