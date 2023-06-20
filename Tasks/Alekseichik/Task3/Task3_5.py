words = input('Enter words:\n').lower().replace(',','').split(' ')

more_then_5 = []
for word in words:
    if len(word) > 5:
        more_then_5.append(word)

print(f'A list containing only strings with more than 5 characters:\n{more_then_5}')
