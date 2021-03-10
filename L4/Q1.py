import math


def check_fibonacci(num):
    if math.sqrt((5*num*num) + 4).is_integer() or math.sqrt((5*num*num) - 4).is_integer():
        return True
    else:
        return False


numbers = list(map(int, input().split(sep=", ")))
fibonacci_count = 0
for num in numbers:
    if check_fibonacci(num):
        fibonacci_count += 1

if fibonacci_count == len(numbers):
    print("Muito bem Sr Weasley o senhor esta quase um trouxa")
elif fibonacci_count == 0:
    print("Ainda ha muito a aprender Sr Weasley")
else:
    print("O senhor esta apendendo Sr Weasley")
