FLORESTA_COMPLETA = 20
FRUTAS = 5
RAIZES = 5
ANIMAIS = 10
URANIO = 10
IODO = 5
PLUTONIO = 5
USINA_NUCLEAR = 20

godzilla_energy = int(input())
kingkong_energy = int(input())
early_recovery = False
for _ in range(int(24 / 4 / 2)):
    godzilla_food = input()

    if godzilla_food == "Uranio":
        godzilla_energy += URANIO
    elif godzilla_food == "Iodo":
        godzilla_energy += IODO
    elif godzilla_food == "Plutonio":
        godzilla_energy += PLUTONIO
    elif godzilla_food == "Usina Nuclear":
        godzilla_energy += USINA_NUCLEAR

    if kingkong_energy >= 100 or godzilla_energy >= 100:
        early_recovery = True
        break

    kingkong_food = input()

    if kingkong_food == "Floresta Completa":
        kingkong_energy += FLORESTA_COMPLETA
    elif kingkong_food == "Frutas":
        kingkong_energy += FRUTAS
    elif kingkong_food == "Raizes":
        kingkong_energy += RAIZES
    elif kingkong_food == "Animais":
        kingkong_energy += ANIMAIS

    if kingkong_energy >= 100 or godzilla_energy >= 100:
        early_recovery = True
        break

    kingkong_food = input()

    if kingkong_food == "Floresta Completa":
        kingkong_energy += FLORESTA_COMPLETA
    elif kingkong_food == "Frutas":
        kingkong_energy += FRUTAS
    elif kingkong_food == "Raizes":
        kingkong_energy += RAIZES
    elif kingkong_food == "Animais":
        kingkong_energy += ANIMAIS

    if kingkong_energy >= 100 or godzilla_energy >= 100:
        early_recovery = True
        break

    godzilla_food = input()

    if godzilla_food == "Uranio":
        godzilla_energy += URANIO
    elif godzilla_food == "Iodo":
        godzilla_energy += IODO
    elif godzilla_food == "Plutonio":
        godzilla_energy += PLUTONIO
    elif godzilla_food == "Usina Nuclear":
        godzilla_energy += USINA_NUCLEAR

    if kingkong_energy >= 100 or godzilla_energy >= 100:
        early_recovery = True
        break

if early_recovery == True and kingkong_energy > godzilla_energy:
    print(
        f"KingKong alcancou a energia maxima antes do fim do dia e com isso sai na vantagem para o proximo combate.\nSua energia total ficou em {kingkong_energy}%."
    )
elif early_recovery == True and godzilla_energy > kingkong_energy:
    print(
        f"Godzilla alcancou a energia maxima antes do fim do dia e com isso sai na vantagem para o proximo combate.\nSua energia total ficou em {godzilla_energy}%."
    )
elif godzilla_energy > kingkong_energy:
    print(
        f"Godzilla se recuperou melhor da ultima batalha e ficou com {godzilla_energy}% de energia. O seu rival KingKong ficou com apenas {kingkong_energy}%."
    )
elif kingkong_energy > godzilla_energy:
    print(
        f"KingKong se recuperou melhor da ultima batalha e ficou com {kingkong_energy}% de energia. O seu rival Godzilla ficou com apenas {godzilla_energy}%."
    )
else:
    print(
        f"Os dois rivais se recuperaram por igual ficando com {kingkong_energy}% de energia e sera mais uma luta acirrada."
    )
