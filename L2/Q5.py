MAX_ROUNDS = 5
DMG_BITE = 400
DMG_PUNCH = 200
DMG_THROW = 500
DMG_TAIL = 300
DMG_ATOMICBLOW = 700
DMG_RADPULSE = 100

hp_kingkong = int(input())
hp_godzilla = int(input())

rounds = 0
for _ in range(MAX_ROUNDS):
    rounds += 1
    atktype_kingkong = input()

    if atktype_kingkong == "Morder":
        hp_godzilla -= DMG_BITE

    elif atktype_kingkong == "Arremessar":
        hp_godzilla -= DMG_THROW

    else:
        for algarism in atktype_kingkong:
            if algarism.isdigit():
                hp_godzilla -= int(algarism) * DMG_PUNCH

    atktype_godzilla = input()

    if atktype_godzilla == "Sopro Atomico":
        hp_kingkong -= DMG_ATOMICBLOW

    elif atktype_godzilla == "Ataque de Cauda":
        hp_kingkong -= DMG_TAIL

    else:
        for algarism in atktype_godzilla:
            if algarism.isdigit():
                hp_kingkong -= int(algarism) * DMG_RADPULSE

    if hp_kingkong <= 0 or hp_godzilla <= 0:
        break

print(f"Foram usados {rounds} golpes...")

if hp_kingkong <= 0 and hp_godzilla > 0:
    print("O rei dos monstros continua seu reinado!")

elif hp_godzilla <= 0 and hp_kingkong > 0:
    print("O Deus macaco venceu!")

elif hp_godzilla <= 0 and hp_kingkong <= 0:
    print("Os grandes titas se destruiram...")

else:
    print("Eh impossivel simular alem disso.")