blocks = input().split()
inversions_count = int(input())

for _ in range(inversions_count):
    initial, final = input().split()
    initial = int(initial) - 1
    final = int(final) - 1

    blocks = blocks[:initial] + blocks[initial:final+1][-1::-1] + blocks[final+1:]

    isOrdered = True
    highest_block = 0
    for block in blocks:
        if int(block) > highest_block:
            highest_block = int(block)
            continue

        isOrdered = False
        break

    if isOrdered:
        break

for block in blocks[:-1]:
    print(block, end=" ")
print(blocks[-1])
if isOrdered:
    print("Voce conseguiu!")
else:
    print("Oops, nao deu certo. Tente novamente!")


