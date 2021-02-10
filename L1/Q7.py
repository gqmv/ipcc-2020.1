from math import ceil

tempo = int(input())

if tempo < 120:
    print("Tempo de competicao invalido")
else:
    nome_1 = input()
    velocidade_1 = int(input())
    nome_2 = input()
    velocidade_2 = int(input())
    nome_3 = input()
    velocidade_3 = int(input())

    total_1 = tempo / velocidade_1
    total_2 = tempo / velocidade_2
    total_3 = tempo / velocidade_3


    if total_1 == total_2 and total_2 == total_3:
        print(f"Nao houve vencedor, foram devorados {ceil(total_1)} sorvetes por cada um.")

    elif total_1 >= total_2 and total_1 >= total_3:
        if total_1 == total_2:
            print(f"Os competidores {nome_1} e {nome_2} empataram devorando {ceil(total_1)} sorvetes!")

        elif total_1 == total_3:
            print(f"Os competidores {nome_1} e {nome_3} empataram devorando {ceil(total_1)} sorvetes!")

        else:
            print(f"O vencedor foi: {nome_1}, devorando {ceil(total_1)} sorvetes!")

    elif total_2 >= total_1 and total_2 >= total_3:
        if total_2 == total_3:
            print(f"Os competidores {nome_2} e {nome_3} empataram devorando {ceil(total_2)} sorvetes!")

        else:
            print(f"O vencedor foi: {nome_2}, devorando {ceil(total_2)} sorvetes!")

    else:
        print(f"O vencedor foi: {nome_3}, devorando {ceil(total_3)} sorvetes!")