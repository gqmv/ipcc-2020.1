initial_lines = int(input())
database = []
for _ in range(initial_lines):
    alien = input().split()
    alien[1] = int(alien[1])
    database.append(alien)

new_lines = int(input())
for _ in range(new_lines):
    alien = input().split()
    alien[1] = int(alien[1])
    exists = False
    for instance in database:
        if instance[0] == alien[0]:
            exists = True
            instance[1] = alien[1]
    if not exists:
        database.append(alien)

elements = len(database)-1
ordered = False
while not ordered:
    ordered = True
    for i in range(elements):
        if database[i][1] > database[i+1][1]:
            database[i], database[i+1] = database[i+1], database[i]
            ordered = False
        elif database[i][1] == database[i+1][1]:
            if database[i][0] > database[i+1][0]:
                database[i], database[i + 1] = database[i + 1], database[i]
                ordered = False

for instance in database:
    print(f"{instance[0]} {instance[1]}")
