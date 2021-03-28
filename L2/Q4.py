scr_godzilla = 0
scr_kingkong = 0

rounds = int(input())
if rounds > 0:
    chosen_letter = input()

    for _ in range(rounds):
        rime_godzilla = input()
        for letter in rime_godzilla:
            if letter == chosen_letter:
                scr_godzilla += 1

        rime_kingkong = input()
        for letter in rime_kingkong:
            if letter == chosen_letter:
                scr_kingkong += 1

    if scr_godzilla == scr_kingkong:
        print("Empate, tem que melhorar essas rimas.")

    elif scr_godzilla > scr_kingkong:
        print("GodZilla Wins.")

    elif scr_kingkong > scr_godzilla:
        print("KingKong Wins.")

else:
    print("Sem rima por hoje, ate outro dia.")