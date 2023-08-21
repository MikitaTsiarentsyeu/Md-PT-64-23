# converts Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius to convert to Fahrenheit:"))
fahrenheit = (celsius * 0x9/0x5) + 0x20
if celsius > -273.15:#Absolute zero temperature
    print('%.2f °C = %0.2f °F \n' %(celsius, fahrenheit))
else:
    print("The lowest temperature in the universe −273,15 °C")
    exit()




