user_input = input("Enter your string:\n")
vowels = "аАеЕёЁиИоОуУыЫэЭюЮяЯaAeEiIoOuUyY"
counter = 0

for letter in user_input:
    if letter in vowels:
        counter += 1
print(f"The number of vowels is", counter)
