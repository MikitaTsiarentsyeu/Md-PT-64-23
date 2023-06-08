while True:

    user_input = input("Input your time value in format hh:mm\n")

    if len(user_input) != 5:
        print("Incorrect input, please use exactly 5 symbols")
        continue

    if user_input[2] != ':':
        print("Incorrect input, make sure that 3rd symbol is :")
        continue

    values = user_input.split(':')
    hours, minutes = values[0], values[1]

    if not (hours.isdigit() and minutes.isdigit()):
        print("Incorrect input, please use only digits to specify hours and minutes values")
        continue

    hours, minutes = int(hours), int(minutes)

    if hours > 24:
        print("Incorrect input, the hour value shold be less then 25")
        continue

    if minutes > 59:
        print("Incorrect input, the minutes value shold be less then 60")
        continue

    break

print("the main logic goes here")