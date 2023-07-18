number_length = 10

def check_numbers(numbers):
    numbers = numbers.replace(" ", '').split(",")
    if not numbers:
        return []
    return list(filter(lambda x: len(x) == number_length and x.isdigit(), numbers))
