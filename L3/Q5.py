levels, avg = input().split()
levels = int(levels)
avg = float(avg)

score_list = input().split()
score_list = [float(x) for x in score_list]  # Simulating list(map(int, score_list))

sum = 0
for score in score_list:
    sum += score

missing_score = (avg * levels) - sum
score_list.append(missing_score)
score_list.sort()

minimum_score = score_list[0]
maximum_score = score_list[-1]

if len(score_list) % 2 != 0:
    median_score = score_list[int((len(score_list) - 1) / 2)]

else:
    median_score = (score_list[int(len(score_list) / 2)] + score_list[int((len(score_list) / 2) - 1)]) / 2

print(f"A pontuacao faltando era: {missing_score:.2f}")
print(f"Minimo: {minimum_score:.2f}")
print(f"Maximo: {maximum_score:.2f}")
print(f"Mediana: {round(median_score, 2):.2f}")

