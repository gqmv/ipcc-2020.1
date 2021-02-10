ingrediente1 = input()
ingrediente2 = input()
ingrediente3 = input()
ingrediente4 = input()

if ingrediente1 == "Plankton" or ingrediente2 == "Plankton" or ingrediente3 == "Plankton" or ingrediente4 == "Plankton":
    print("Nao acredito que o Seu Sirigueijo me enganou de novo!")

else:
    ingredientes_validos = 4

    if ingrediente1 == "<ERRO>":
        ingredientes_validos -= 1
        
    if ingrediente2 == "<ERRO>":
        ingredientes_validos -= 1

    if ingrediente3 == "<ERRO>":
        ingredientes_validos -= 1
    
    if ingrediente4 == "<ERRO>":
        ingredientes_validos -= 1

    if ingredientes_validos == 4:
        print("Enfim, a formula secreta do Hamburguer de Siri!")

    elif ingredientes_validos == 0:
        print("Karen, acho que temos que melhorar esse seu programa")

    else:
        print(f"Pelo menos descobrimos {ingredientes_validos} ingrediente(s)")