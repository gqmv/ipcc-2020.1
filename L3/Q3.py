enemy_hp = int(input())

atk_count = int(input())

atk_list = []

for _ in range(atk_count):
    atk_data = input().split()

    atk_list.append(atk_data)

possible_subarrays = []
for i in range(len(atk_list) + 1):
    for j in range(i + 1, len(atk_list) + 1):
        possible_subarrays.append(atk_list[i:j])

atks_subarray = []
for subarray in possible_subarrays:
    sum = 0
    atks_used = []
    for atk in subarray:
        sum += int(atk[1])
        atks_used.append(atk[0])

    if sum == enemy_hp:
        atks_subarray = atks_used
        break

if len(atks_subarray) != 0:
    print("Super efetivo! Os ataques usados foram:")
    for atk in atks_subarray:
        print(atk)
else:
    print("Nao ha um subarray de ataques para derrotar o pokemon")

