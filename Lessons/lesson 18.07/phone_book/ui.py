import validation
import logic


def add_record():
    """ask a user for a name and numbers, then go to logic"""
    name = ask_for_param("a name")
    numbers = ask_for_param("numbers separated by comma")
    numbers = validation.check_numbers(numbers)
    if numbers:
        res = logic.add_record(name, *numbers)
        print(res)
    else:
        print("something went wrong while processing numbers, please try again")

def get_record():
    """ask a user for a name, then go to logic"""
    name = ask_for_param("a name")
    res = logic.get_record(name)
    print(res)

def get_all_records():
    print(logic.get_all_records())

def ask_for_param(param):
    value = input(f"Please enter {param}:\n")
    return value

def start():
    while True:
        answ = input("""
            Choose the menu option:
            0.exit
            1.get all records
            2.get a record
            3.add a record
        """).strip()
        if answ == '0':
            break
        elif answ == '1':
            get_all_records()
        elif answ == '2':
            get_record()
        elif answ == '3':
            add_record()
        else:
            print("choose only numbers presented in the list")
            continue