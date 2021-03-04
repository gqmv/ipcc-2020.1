scoreboard = []
player_map = []
for _ in range(12):
    character = input()
    scoreboard.append(character)

for _ in range(4):
    player = input()
    player_map.append(player.split())

winner = None
for player in reversed(scoreboard):
    for family_member in player_map:
        if player in family_member:
            winner = family_member[0]
            break
    if winner is not None:
        break


print(winner)