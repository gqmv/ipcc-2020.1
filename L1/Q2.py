adversaria_media = float(input())

bob_nota = int(input())
patrick_nota = int(input())
sandy_nota = int(input())
lula_nota = int(input())

lula_media = (bob_nota + patrick_nota + sandy_nota + lula_nota) / 4

if adversaria_media > lula_media:
    print("A banda adversária ganhou")
else:
    maior_nota = 0
    astro = ""

    if bob_nota > maior_nota:
        astro = "Bob Esponja"
        maior_nota = bob_nota

    if patrick_nota > maior_nota:
        astro = "Patrick"
        maior_nota = patrick_nota

    if sandy_nota > maior_nota:
        astro = "Sandy"
        maior_nota = sandy_nota

    if lula_nota > maior_nota:
        astro = "Lula Molusco"
        maior_nota = lula_nota

    print(f"A banda do Lula Molusco venceu! O astro do show foi {astro}")