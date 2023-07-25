import pickle

cache_file_path = "cache_file"

try:
    print("Open file for reading.")
    with open(cache_file_path, 'rb') as cached_file:
        cached_data = pickle.load(cached_file)

except FileNotFoundError:
    cached_data = {}


def cache(func):
    def wrapper(*args, **kwargs):

        func_name = func.__name__

        if func_name not in cached_data:
            cached_data[func_name] = {}

        key = str((args, kwargs))

        if key in cached_data[func_name]:
            output = cached_data.get(func_name).get(key)
            print(f"From cache for {func_name}{*args, *kwargs} = ", end="")
        else:
            output = func(*args, **kwargs)
            cached_data[func_name][key] = output

            print("Open file writing.")
            with open(cache_file_path, 'wb') as file:
                pickle.dump(cached_data, file)
            print(f"New value for {func_name}{*args, *kwargs} = ", end="")

        return output

    return wrapper


@cache
def f1(a):
    return a ** 2


@cache
def f2(a):
    return a + 5


@cache
def f3(*args, **kwargs):
    return [args, kwargs]

@cache
def summa(l):
    return sum(l)


print(f1(2))
print(f1(3))
print(f1(4))
print(f1(2))

print(f2(2))
print(f2(3))
print(f2(3))

print(f1(4))

print(summa([1,2,3,4,5,6,7]))
print(summa([1,2,3,4,5,6,7]))