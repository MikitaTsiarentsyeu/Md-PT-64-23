numbers = input('Enter numbers to get average:\n').replace(',','.').replace('. ',' ').split(' ')

sum_numbers = 0
for i in numbers:
    sum_numbers += float(i)

average = sum_numbers/len(numbers)
print(f'The average of this numbers is {average}')
