def translate(number):
    if number == 100:
        return " "

    elif number >= 0 and number <= 49:
        i = number % 26
        letter = chr(ord("a") + i)

        return letter

    elif number >= 50 and number <= 99:
        i = (number - 50) % 26
        letter = chr(ord("A") + i)

        return letter

is_valid = True
numbers = list(map(int, input().split()))
text = ""
for number in numbers:
    if number > 100 or number < 0:
        is_valid = False
        break

    text += translate(number)

if is_valid:
    print(text)
else:
    print("Infelizmente os números nao dizem nada")
