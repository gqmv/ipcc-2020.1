ALPHABET = list("abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ")

def find_index(letter, alphabet):
    for i, possible_letter in enumerate(alphabet):
        if letter == possible_letter:
            return i

def encode(text, k):
    output = ""
    for letter in text:
        if letter in ALPHABET:
            i = (find_index(letter, ALPHABET) + k) % len(ALPHABET)
            output += ALPHABET[i]
        else:
            output += letter

    return output

def decode(text, k):
    output = ""
    for letter in text:
        if letter in ALPHABET:
            i = find_index(letter, ALPHABET) - k
            output += ALPHABET[i]
        else:
            output += letter

    return output

k = int(input())
n = int(input())

for _ in range(n):
    opcode, text = input().split(maxsplit=1)

    if opcode == "C":
        print(encode(text, k))
    elif opcode == "D":
        print(decode(text, k))
    else:
        print("Esta mensagem é falsificada!")
