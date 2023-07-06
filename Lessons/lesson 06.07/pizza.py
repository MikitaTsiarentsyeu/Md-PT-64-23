def prepare():
    print("STARTING A NEW PIZZA MAKING PROCESS")
    print("preparing a base")
    print("choosing a sauce")

def add_ingridient(ingridient):
    print(f"adding {ingridient}")

def grind_cheese():
    print("grinding cheese")

def bake(temp, time):
    print(f"baking for {time} minute at {temp} degrees")

def done():
    print("boxing")
    print("slicing")
    print("DONE")

# def make_pepperoni():
#     prepare()
#     add_ingridient("pepperoni")
#     grind_cheese()
#     bake(180, 2)
#     done()

# def make_double_pepperoni():
#     prepare()
#     add_ingridient("pepperoni")
#     add_ingridient("pepperoni")
#     grind_cheese()
#     bake(180, 2)
#     done()

# def make_4_cheeses():
#     prepare()
#     add_ingridient("chedder")
#     add_ingridient("cordon-blue")
#     add_ingridient("parmesan")
#     add_ingridient("mozarella")
#     grind_cheese()
#     bake(150, 3)
#     done()

def pizza_factory(ingridients, temp, time):
    def factory_method():
        prepare()
        for i in ingridients:
            add_ingridient(i)
        grind_cheese()
        bake(temp, time)
        done()
    return factory_method

make_pepperoni = pizza_factory(["pepperoni"], 180, 2)
make_double_pepperoni = pizza_factory(["pepperoni", "pepperoni"], 180, 2)
make_4_cheeses = pizza_factory(["chedder", "cordon-blue", "parmesan", "mozarella"], 150, 3)

make_double_pepperoni()