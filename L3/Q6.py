bosses_count = input()  # This implementation does not use this variable.
bosses = input().split()
difficulties = input().split()

bosses_map = []

for i in range(len(difficulties)):
    difficulty = difficulties[i]
    if difficulty == "Facil":
        difficulty = 0

    elif difficulty == "Medio":
        difficulty = 1

    elif difficulty == "Dificil":
        difficulty = 2

    bosses_map.append([bosses[i], difficulty])

elements = len(bosses_map)-1
ordered = False
while not ordered:
    ordered = True
    for i in range(elements):
        if bosses_map[i][1] > bosses_map[i+1][1]:
            bosses_map[i], bosses_map[i+1] = bosses_map[i+1], bosses_map[i]
            ordered = False
        elif bosses_map[i][1] == bosses_map[i+1][1]:
            if bosses_map[i][0] > bosses_map[i+1][0]:
                bosses_map[i], bosses_map[i + 1] = bosses_map[i + 1], bosses_map[i]
                ordered = False

for boss in bosses_map[:-1]:
    print(boss[0], end=" ")

print(bosses_map[-1][0])
