s = input().lower()
g = 0
for i in range(len(s)):
    if s[i] in 'ауоыиэяюёеaeyuio':
        g = g +1
print('Количество гласных букв равно', g)
