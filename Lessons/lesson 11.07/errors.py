l = [1,2,3,4,5]


try:

    print("the start of the inner try")
    # l[100]

    try:
        # print(l[100])
        print(test)
        print("the rest og the block")
    except IndexError:
        print("something went wrong with an index")
    except NameError:
        # print(l[100])
        # print(name)
        # raise KeyError()
        print("oops")
    finally:
        print("I work every time")


    print("the end of inner try")

    
except NameError:
    print("something went wrong with a variable")
except:
    print("I will catch 'em all")
else:
    print("nothing went wrong")
finally:
    print("I work every time")


print("the logic goes here")

try:
    f = open("test.txt", 'w')
    # raise KeyError()
finally:
    f.close()

with open("test.txt", 'w') as f:
    f.write("test")