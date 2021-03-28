SCR_MOONWALK = 80
SCR_DUCKWALK = 70
SCR_ROOSTERSTRUT = 60
SCR_CARTWHEEL = 90
SCR_SIDEGLIDE = 70
SCR_SUPERMAN = 75
SCR_RUNNINGMAN = 85
SCR_FLARE = 100

scr_kingkong = 0
scr_godzilla = 0
rounds = int(input())

for _ in range(rounds):
    move_kingkong = input()
    perf_kingkong = float(input())

    if move_kingkong == "Moonwalk":
        scr_kingkong += SCR_MOONWALK * perf_kingkong

    elif move_kingkong == "Duck Walk":
        scr_kingkong += SCR_DUCKWALK * perf_kingkong

    elif move_kingkong == "Rooster Strut":
        scr_kingkong += SCR_ROOSTERSTRUT * perf_kingkong

    elif move_kingkong == "Cartwheel":
        scr_kingkong += SCR_CARTWHEEL * perf_kingkong

    elif move_kingkong == "Side Glide":
        scr_kingkong += SCR_SIDEGLIDE * perf_kingkong

    elif move_kingkong == "Superman":
        scr_kingkong += SCR_SUPERMAN * perf_kingkong

    elif move_kingkong == "The Running man":
        scr_kingkong += SCR_RUNNINGMAN * perf_kingkong

    elif move_kingkong == "Flare":
        scr_kingkong += SCR_FLARE * perf_kingkong

    move_godzilla = input()
    perf_godzilla = float(input())

    if move_godzilla == "Moonwalk":
        scr_godzilla += SCR_MOONWALK * perf_godzilla

    elif move_godzilla == "Duck Walk":
        scr_godzilla += SCR_DUCKWALK * perf_godzilla

    elif move_godzilla == "Rooster Strut":
        scr_godzilla += SCR_ROOSTERSTRUT * perf_godzilla

    elif move_godzilla == "Cartwheel":
        scr_godzilla += SCR_CARTWHEEL * perf_godzilla

    elif move_godzilla == "Side Glide":
        scr_godzilla += SCR_SIDEGLIDE * perf_godzilla

    elif move_godzilla == "Superman":
        scr_godzilla += SCR_SUPERMAN * perf_godzilla

    elif move_godzilla == "The Running man":
        scr_godzilla += SCR_RUNNINGMAN * perf_godzilla

    elif move_godzilla == "Flare":
        scr_godzilla += SCR_FLARE * perf_godzilla

if scr_godzilla > scr_kingkong:
    print("Lagartixa, oops... Godzilla wins")

elif scr_kingkong > scr_godzilla:
    print("Oozaro, oops... King Kong wins")

else:
    print("Empate")