bob_elogios = int(input())
bob_falhas = int(input())
bob_horasextras = float(input()) / 10
bob_prejuizo = input()

lula_elogios = int(input())
lula_falhas = int(input())
lula_horasextras = float(input()) / 10
lula_prejuizo = input()

if (bob_prejuizo == "nao causou prejuizo" and lula_prejuizo == "nao causou prejuizo") or (bob_prejuizo != "nao causou prejuizo" and lula_prejuizo != "nao causou prejuizo"):
    bob_pontuacao = bob_elogios - bob_falhas + bob_horasextras
    lula_pontuacao = lula_elogios - lula_falhas + lula_horasextras

    if bob_pontuacao == lula_pontuacao:
        if bob_horasextras > lula_horasextras:
            print("Bob Esponja venceu o concurso e se tornou o funcionário do mes")
        else:
            print("Lula Molusco venceu o concurso e se tornou o funcionário do mes")

    elif bob_pontuacao > lula_pontuacao:
        print("Bob Esponja venceu o concurso e se tornou o funcionário do mes")
    else:
        print("Lula Molusco venceu o concurso e se tornou o funcionário do mes")

else:
    if bob_prejuizo != "nao causou prejuizo":
        print("Lula Molusco venceu o concurso e se tornou o funcionário do mes")
    else:
        print("Bob Esponja venceu o concurso e se tornou o funcionário do mes")