pomo = list(map(int, input().split()))
harry = list(map(int, input().split()))
drako = list(map(int, input().split()))

INPUTS = 5

def move(player, coordinates):
    for i in range(3):
        player[i] += coordinates[i]

def check_colision(obj1, obj2):
    for a, b in zip(obj1, obj2):
        if a != b:
            return False
    return True

def eval_action(player, action, coordinates):
    '''
    This function returns True if a catch action was called and was sucessful.
    '''
    if action == "Mover:":
        move(player, coordinates)
    elif action == "Agarrar":
        if check_colision(player, pomo):
            return True
        else:
            return False

coordinates = [0,0,0]
winner = None
colision = False
for _ in range(INPUTS):
    user_input =  input().split()
    if len(user_input) == 4:
        action, x, y, z = user_input
        coordinates = [int(x), int(y), int(z)]
    else:
        action = user_input[0]

    is_over = eval_action(harry, action, coordinates)

    if is_over:
        winner = "Harry"
        break

    if check_colision(harry, drako):
        colision = True
        break

    user_input = input().split()
    if len(user_input) == 4:
        action, x, y, z = user_input
        coordinates = [int(x), int(y), int(z)]
    else:
        action = user_input[0]

    is_over = eval_action(drako, action, coordinates)

    if is_over:
        winner = "Drako"
        break

    if check_colision(harry, drako):
        colision = True
        break

if colision:
    print("Os apanhadores colidem e vao ao chao! Parece que eles nao vao se levantar tao cedo ...")
elif winner == "Harry":
    print("Harry conseguiu apanhar o Pomo de Ouro e fez a Grifinoria sair vitoriosa!")
elif winner == "Drako":
    print("Drako conseguiu apanhar o Pomo de Ouro e fez a Sonserina sair vitoriosa!")
else:
    print("A partida continua sem resultado, seguimos com o jogo!")