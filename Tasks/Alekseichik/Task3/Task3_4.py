nums = input('Enter numbers:\n').replace(',','').split(' ')

for i in range(1,len(nums)):
    insert = int(nums[i])
    j = i - 1
    while j >= 0 and int(nums[j]) > insert:
        nums[j + 1] = nums[j]
        j -= 1
    nums[j + 1] = insert

print(f'The second largest number in your list: {nums[-2]}')