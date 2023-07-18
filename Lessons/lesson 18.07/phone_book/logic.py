repo = {"name":["4356436536", "5465474757"]}

def add_record(name, *numbers):
    if name not in repo:
        repo[name] = list(numbers)
        return "the record was added"
    else:
        current_numbers = repo[name]
        current_numbers.extend(numbers)
        repo[name] = list(set(current_numbers))
        return "the name exists, the numbers were added"
    
def get_record(name):
    if name in repo:
        numbers = repo[name]
        return f"{name}:{','.join(numbers)}"
    else:
        return "nothing was found"
    
def get_all_records():
    return '\n'.join([f"{name}:{','.join(repo[name])}" for name in repo])
