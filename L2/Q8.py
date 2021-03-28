strongest_name = ""
strongest_force = 0
weakest_name = ""
weakest_force = 99999999999999999999999999999999999999
count = 0
force_sum = 0
while True:
    try:
        name = input()
        force = int(input())
    except EOFError:
        break

    count += 1
    force_sum += force

    if force > strongest_force:
        strongest_name = name
        strongest_force = force
    if force < weakest_force:
        weakest_name = name
        weakest_force = force

victory_chance = max(0, ((strongest_force - force_sum / count) / (strongest_force - weakest_force)))
defeat_chance = max(0, (force_sum / count - weakest_force) / (strongest_force - weakest_force))


