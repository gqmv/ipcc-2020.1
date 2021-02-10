vitorias_patrick = 0
vitorias_lula = 0

escolha_patrick = input()
escolha_lula = input()

if escolha_patrick == "Pedra" and escolha_lula == "Papel":
    vitorias_lula += 1
elif escolha_patrick == "Pedra" and escolha_lula == "Tesoura":
    vitorias_patrick += 1
elif escolha_patrick == "Papel" and escolha_lula == "Pedra":
    vitorias_patrick += 1
elif escolha_patrick == "Papel" and escolha_lula == "Tesoura":
    vitorias_lula += 1
elif escolha_patrick == "Tesoura" and escolha_lula == "Pedra":
    vitorias_lula += 1
elif escolha_patrick == "Tesoura" and escolha_lula == "Papel":
    vitorias_patrick += 1

escolha_patrick = input()
escolha_lula = input()

if escolha_patrick == "Pedra" and escolha_lula == "Papel":
    vitorias_lula += 1
elif escolha_patrick == "Pedra" and escolha_lula == "Tesoura":
    vitorias_patrick += 1
elif escolha_patrick == "Papel" and escolha_lula == "Pedra":
    vitorias_patrick += 1
elif escolha_patrick == "Papel" and escolha_lula == "Tesoura":
    vitorias_lula += 1
elif escolha_patrick == "Tesoura" and escolha_lula == "Pedra":
    vitorias_lula += 1
elif escolha_patrick == "Tesoura" and escolha_lula == "Papel":
    vitorias_patrick += 1

if vitorias_patrick == vitorias_lula:
    escolha_patrick = input()
    escolha_lula = input()

    if escolha_patrick == "Pedra" and escolha_lula == "Papel":
        vitorias_lula += 1
    elif escolha_patrick == "Pedra" and escolha_lula == "Tesoura":
        vitorias_patrick += 1
    elif escolha_patrick == "Papel" and escolha_lula == "Pedra":
        vitorias_patrick += 1
    elif escolha_patrick == "Papel" and escolha_lula == "Tesoura":
        vitorias_lula += 1
    elif escolha_patrick == "Tesoura" and escolha_lula == "Pedra":
        vitorias_lula += 1
    elif escolha_patrick == "Tesoura" and escolha_lula == "Papel":
        vitorias_patrick += 1

if vitorias_patrick != vitorias_lula:
    if vitorias_patrick > vitorias_lula:
        vencedor = "Patrick"
    else:
        vencedor = "Lula Molusco"

    print(f"{vencedor} venceu!")

else:
    print("Empate!")
