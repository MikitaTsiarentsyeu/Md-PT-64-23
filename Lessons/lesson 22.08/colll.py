import random

class Collection:

    def __init__(self, *elems) -> None:
        self.__items = []
        if elems:
            self.__items.extend(elems)

    def add(self, item):
        if item not in self.__items:
            self.__items.append(item)

    def remove(self, item):
        if item in self.__items:
            self.__items.remove(item)

    def __str__(self) -> str:
        return f"{Collection.__name__}({','.join([str(x) for x in self.__items])})"

    def __len__(self):
        return len(self.__items)

    def __eq__(self, other):
        if not isinstance(other, Collection):
            return False
        
        return self.__items == other.__items
    
    def __iter__(self):
        self.__iterable_items = list(self.__items)
        random.shuffle(self.__iterable_items)
        self.__iterable_index = 0
        return self
    
    def __next__(self):
        if self.__iterable_index >= len(self.__iterable_items):
            del self.__iterable_index
            del self.__iterable_items
            raise StopIteration
        
        item = self.__iterable_items[self.__iterable_index]
        self.__iterable_index += 1
        return item

    def __getitem__(self, key):
        try:
            return self.__items[key]
        except IndexError:
            raise IndexError(f"{Collection.__name__} index out of range")

    def __setitem__(self, key, value):
        try:
            self.__items[key] = value
        except IndexError:
            self.add(value)

    def __enter__(self):
        return self

    def __exit__(self, e_type, e, traceback):
        self.__items = []

    def __add__(self, other):
        pass

    @classmethod
    def from_list(cls, lst):
        return cls(*lst)

coll = Collection.from_list([1,2,3,4,5])
print(coll)
coll.add(2)
coll.add("test")
print(coll)

print(Collection(1,2,3)==Collection(1,2,3))

target_coll = Collection(1,2,3,4,5,6,7,8,9)
print([x for x in target_coll])


print(target_coll[1])
target_coll[1000] = 1.1
print(target_coll)

# with open("test.txt", 'w') as f:
#     f.write("test")

with Collection(1,2,3,4,5) as coll:
    print(coll)

print(coll)

# str(coll)

# coll.__str__()

# len(coll)

# coll.__len__()

# coll == Collection(1,2,3,4,5)

# coll.__eq__(Collection(1,2,3,4,5))