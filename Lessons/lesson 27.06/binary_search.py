l = [2,4,5,7,8,9,10]

def search(l, target, low=0, high=None):
    if high == None:
            high = len(l)-1
    if high >= low:
        mid = (low + high)//2
        if l[mid] == target:
            return mid
        elif l[mid] > target:
            return search(l, target, low, mid-1)
        else:
            return search(l, target, mid+1, high)
    else:
        return False
    
print(search(l, -20))