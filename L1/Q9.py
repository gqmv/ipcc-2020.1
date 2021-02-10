bob_objeto = None
bob_total = 0

patrick_objeto = None
patrick_total = 0

bob_r1 = input()
if bob_r1.isdigit():
    bob_total += int(bob_r1)
else:
    bob_objeto = bob_r1
    bob_total = 0

bob_r2 = input()
if bob_objeto == None:
    if bob_r2.isdigit():
        bob_total += int(bob_r2)
    else:
        bob_objeto = bob_r2
        bob_total = 0

bob_r3 = input()
if bob_objeto == None:
    if bob_r3.isdigit():
        bob_total += int(bob_r3)
    else:
        bob_objeto = bob_r3
        bob_total = 0

patrick_r1 = input()
if patrick_r1.isdigit():
    patrick_total += int(patrick_r1)
else:
    patrick_objeto = patrick_r1
    patrick_total = 0

patrick_r2 = input()
if patrick_objeto == None:
    if patrick_r2.isdigit():
        patrick_total += int(patrick_r2)
    else:
        patrick_objeto = patrick_r2
        patrick_total = 0

patrick_r3 = input()
if patrick_objeto == None:
    if patrick_r3.isdigit():
        patrick_total += int(patrick_r3)
    else:
        patrick_objeto = patrick_r3
        patrick_total = 0

if patrick_objeto == None or bob_objeto == None:
    if patrick_total > bob_total:
        print(f"Patrick foi o vencedor do torneio com uma pontuacao de {patrick_total} pontos!")

        if bob_objeto == None:
            print(f"Bob Esponja foi derrotado, so pontuou {bob_total} pontos")
        else:
            print(f"Bob Esponja foi desclassificado porque capturou um/uma {bob_objeto}")
    
    elif bob_total > patrick_total:
        print(f"Bob Esponja foi o vencedor do torneio com uma pontuacao de {bob_total} pontos!")

        if patrick_objeto == None:
            print(f"Patrick foi derrotado, so pontuou {patrick_total} pontos")
        else:
            print(f"Patrick foi desclassificado porque capturou um/uma {patrick_objeto}")

    else:
        print("Bob Esponja e Patrick empataram!")

else:
    print("Que vergonha para a Fenda do Biquini! Ambos foram desclassificados!")