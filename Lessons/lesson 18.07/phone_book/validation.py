number_length = 10

def check_numbers(numbers:str) -> list:
    numbers = numbers.replace(" ", '').split(",")
    if not numbers:
        return []
    try:
        return list(filter(lambda x: len(x) == number_length and x.isdigit(), numbers))
    except:
        raise RuntimeError("an error occured during numbers parsing")