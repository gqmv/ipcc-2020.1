posts_count = int(input())
godzilla_occur = 0
kingkong_occur = 0


for _ in range(posts_count):
    post = input().lower()
    for i in range(len(post)):
        if post[i] == "k" and (len(post) - i >= len("king kong")):
            if post[i + 1] == "i":
                if post[i + 2] == "n":
                    if post[i + 3] == "g":
                        if post[i + 4] == " ":
                            if post[i + 5] == "k":
                                if post[i + 6] == "o":
                                    if post[i + 7] == "n":
                                        if post[i + 8] == "g":
                                            kingkong_occur += 1
        
        elif post[i] == "g" and (len(post) - i >= len("godzilla")):
            if post[i + 1] == "o":
                if post[i + 2] == "d":
                    if post[i + 3] == "z":
                        if post[i + 4] == "i":
                            if post[i + 5] == "l":
                                if post[i + 6] == "l":
                                    if post[i + 7] == "a":
                                        godzilla_occur += 1

if godzilla_occur > kingkong_occur:
    print("Godzilla eh mais famoso")

elif kingkong_occur > godzilla_occur:
    print("King Kong eh mais famoso")

else:
    print("Os dois titas sao igualmente amados")