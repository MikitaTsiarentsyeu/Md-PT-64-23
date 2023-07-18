import json
repo_name = "repo.json"

try:
    with open(repo_name, 'r') as f:
        repo = json.load(f)
except:
    raise RuntimeError("an error occured while accessing a storage")

def add_record(name, *numbers):
    if name not in repo:
        repo[name] = list(numbers)
        res = "the record was added"
    else:
        current_numbers = repo[name]
        current_numbers.extend(numbers)
        repo[name] = list(set(current_numbers))
        res = "the name exists, the numbers were added"
    with open(repo_name, 'w') as f:
        json.dump(repo, f)
    return res
    
def get_record(name):
    try:
        numbers = repo[name]
        return f"{name}:{','.join(numbers)}"
    except KeyError:
        return "nothing was found"
    except:
        raise RuntimeError("an error occured during getting a record")
        
    
def get_all_records():
    try:
        return '\n'.join([f"{name}:{','.join(repo[name])}" for name in repo])
    except:
        raise RuntimeError("an error occured during getting records information")