min = 5
max = 100

while True:
    x = input(f"Enter the numeric value higher than {min}:\n")

    try:
        x = int(x)
        if x <= min:
            raise RuntimeError("the value is low")
        if x >= max:
            raise RuntimeError("the value is high")

        break
    
    except ValueError:
        print("It was not a number")
        continue
    except RuntimeError as exception_variable_name:
        print(exception_variable_name)
        continue

print("the main logic goes here")