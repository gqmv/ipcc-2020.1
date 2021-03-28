MUL_RANK_S = 1.5
MUL_RANK_A = 1.2
MUL_RANK_B = 0.8
MUL_RANK_C = 0.5

monster_count = int(input())
global_avg = int(input())

defeated_count = 0
for _ in range(monster_count):
    name = input()
    hp = int(input())
    atk_count = int(input())

    if hp > MUL_RANK_S * global_avg:
        ranking = "S"
    elif hp >= MUL_RANK_A * global_avg:
        ranking = "A"
    elif hp > MUL_RANK_B * global_avg:
        ranking = "B"
    elif hp >= MUL_RANK_C * global_avg:
        ranking = "C"
    else:
        ranking = "D"

    total_dmg = 0
    for _ in range(atk_count):
        damage = int(input())
        total_dmg += damage

    if total_dmg >= hp:
        print(f"{name} ranking {ranking} foi destruido!")
        defeated_count += 1
    else:
        print(f"{name}, nivel de classe {ranking}, conseguiu escapar do Godzilla.")

if defeated_count < monster_count:
    print("Alguns oponentes ainda estao a espreita...")
else:
    print("O rei dos Kaijus aniquilou as ameaças.")
