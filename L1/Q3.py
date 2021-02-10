nome_vilao1 = input()
poder_vilao1 = int(input())
local_vilao1 = input()

nome_vilao2 = input()
poder_vilao2 = int(input())
local_vilao2 = input()


if local_vilao1 == "Siri Cascudo":
    potencial_vilao1 = 2

elif local_vilao1 == "Centro da Cidade":
    potencial_vilao1 = 5

elif local_vilao1 == "Lagoa Goo":
    potencial_vilao1 = 3

else:
    potencial_vilao1 = 1


if local_vilao2 == "Siri Cascudo":
    potencial_vilao2 = 2

elif local_vilao2 == "Centro da Cidade":
    potencial_vilao2 = 5

elif local_vilao2 == "Lagoa Goo":
    potencial_vilao2 = 3

else:
    potencial_vilao2 = 1


destruicao_vilao1 = poder_vilao1 * potencial_vilao1
destruicao_vilao2 = poder_vilao2 * potencial_vilao2

if destruicao_vilao1 > destruicao_vilao2:
    print(f"Precisamos nos apressar para salvar o(a) {local_vilao1} das garras do(a) {nome_vilao1}")
elif destruicao_vilao2 > destruicao_vilao1:
    print(f"Precisamos nos apressar para salvar o(a) {local_vilao2} das garras do(a) {nome_vilao2}")
else:
    print("Precisamos de reforcos")

