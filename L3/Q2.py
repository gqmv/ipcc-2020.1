bonus_elements = input().split()

player_count = int(input())

for _ in range(player_count):
    name, position = input().split()
    position = int(position)

    i = (position * 2) % len(bonus_elements) - 1

    bonus_element = bonus_elements[i]
    print(f"{name} coletou a caixa e vai ganhar um/uma {bonus_element}")
