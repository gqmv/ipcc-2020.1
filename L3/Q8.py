pokemon_count = int(input())
highest_level = 0
highest_level_pokemons = []
lowest_level = 9999999
lowest_level_pokemons = []
for _ in range(pokemon_count):
    name, level = input().split()
    level = int(level)
    if level == highest_level:
        highest_level_pokemons.append(name)
    elif level > highest_level:
        highest_level = level
        highest_level_pokemons = [name]

    if level == lowest_level:
        lowest_level_pokemons.append(name)
    elif level < lowest_level:
        lowest_level = level
        lowest_level_pokemons = [name]

"O maior level é LMax, do(s) pokemon(s) P1, P2 ... Pn. E o menor é Lmin, do(s) pokemon(s) P1, P2, ... Pn"
print(f"O maior level é {highest_level}, do(s) pokemon(s) ", end="")
for pokemon in highest_level_pokemons[:-1]:
    print(pokemon, end=", ")
print(highest_level_pokemons[-1], end=". ")
print(f"E o menor é {lowest_level}, do(s) pokemon(s) ", end="")
for pokemon in lowest_level_pokemons[:-1]:
    print(pokemon, end=", ")
print(lowest_level_pokemons[-1])
