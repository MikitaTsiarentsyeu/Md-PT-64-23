user_input = input("Enter your string:\n")
vowels = "аАеЕёЁиИоОуУыЫэЭюЮяЯaAeEiIoOuUyY"

for letter in user_input:
    if letter in vowels:
       user_input = user_input.replace(letter, "")

print(f"The string without vowels is", user_input)