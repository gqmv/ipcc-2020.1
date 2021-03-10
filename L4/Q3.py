def sum_main_diagonal(matrix):
    sum = 0
    for i, linha in enumerate(matrix):
        sum += linha[i]
    return sum

def sum_secondary_diagonal(matrix):
    sum = 0
    for i, linha in enumerate(matrix):
        sum += linha[len(matrix) - 1 - i]
    return sum

def sum_above_main_diagonal(matrix):
    sum = 0
    for i, linha in enumerate(matrix):
        for j in range(i + 1, len(linha)):
            sum += linha[j]
    return sum

def sum_below_main_diagonal(matrix):
    sum = 0
    for i, linha in enumerate(matrix):
        for j in range(i):
            sum += linha[j]
    return sum

lines = int(input())

is_valid = True
matrix = []
for _ in range(lines):
    line = list(map(int, input().split()))

    if len(line) != lines:
        is_valid = False

    matrix.append(line)

if is_valid:
    diagonals_sum = sum_secondary_diagonal(matrix) + sum_main_diagonal(matrix)
    above_below_diagonal_diff = abs(sum_above_main_diagonal(matrix) - sum_below_main_diagonal(matrix))

    if diagonals_sum != above_below_diagonal_diff:
       is_valid = False

if is_valid:
    print("Essa informacao e confiavel")
else:
    print("Essa informacao nao e muito confiavel")
