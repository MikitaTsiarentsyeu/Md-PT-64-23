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

coll = Collection(2,3)
coll.add(2)
coll.add("test")
print(coll)

print(Collection(1,2,3)==Collection(1,2,3))

target_coll = Collection(1,2,3,4,5,6,7,8,9)
print([x for x in target_coll])
print([x for x in target_coll])
print([x for x in target_coll])
print([x for x in target_coll])
print([x for x in target_coll])