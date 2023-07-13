nums = [1,2,4,5,6,7,8,45,46,46,47,47,46,15,16]

def list_coll(nums):
    res = ''
    nums.append(None)
    first = None
    last = None
    single = None
    for i in range(len(nums)-1):
        if nums[i]+1 == nums[i+1]:
            if first is None:
                first = nums[i]
        elif nums[i]+1 != nums[i+1] and nums[i]-1 == nums[i-1]:
            last = nums[i]
        elif nums[i]-1 != nums[i-1] and nums[i]+1 != nums[i+1]:
            if single is None:
                single = nums[i]
        if last != None:
            res +=(f'{str(first)}-{str(last)}, ')
            first = None
            last = None
        elif single != None:
            res +=f'{str(single)}, '
            single = None
    print(res[:-2])


list_coll(nums)