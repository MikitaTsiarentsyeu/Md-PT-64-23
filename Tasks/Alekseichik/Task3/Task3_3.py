words = input('Enter words:\n').lower().replace(',','').split(' ')

word_counter = {}

for word in words:
    if word not in word_counter:
        word_counter[word] = 0
    word_counter[word] += 1
    
for key,value in word_counter.items():
    print(f'{key}: {value}')