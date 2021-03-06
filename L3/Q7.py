world_record_times = []
for _ in range(9):
    time = input().split(sep=":")
    seconds = int(time[2])
    minutes = int(time[1])
    hours = int(time[0])

    minutes += hours * 60
    seconds += minutes * 60

    world_record_times.append(seconds)

luigi_times = []
for _ in range(9):
    time = input().split(sep=":")
    seconds = int(time[2])
    minutes = int(time[1])
    hours = int(time[0])

    minutes += hours * 60
    seconds += minutes * 60

    luigi_times.append(seconds)

luigi_times.sort()

total_luigi_time = 0
total_world_record_time = 0
biggest_difference = [0,None]
smallest_difference = [0,None]
for i in range(9):
    current_luigi_time = luigi_times[i] - total_luigi_time
    current_world_record_time = world_record_times[i] - total_world_record_time

    difference = current_luigi_time - current_world_record_time
    if biggest_difference[0] < difference:
        biggest_difference = [difference, i + 1]
    if smallest_difference[0] > difference:
        smallest_difference = [difference, i + 1]

    total_luigi_time += current_luigi_time
    total_world_record_time += current_world_record_time

if smallest_difference[0] == 0 and biggest_difference[0] == 0:
    print("Voce ainda nao quebrou o recorde, mas seus tempos estao iguais ao do recorde")
elif total_luigi_time >= total_world_record_time:
    print(f"No mundo {biggest_difference[1]} voce  ficou {biggest_difference[0]}s atras do tempo do recorde e teve o pior desempenho")
elif total_world_record_time > total_luigi_time:
    print(f"Parabens voce quebrou o recorde mundial. No mundo {smallest_difference[1]} voce foi {abs(smallest_difference[0])}s mais rapido que o tempo do recorde e teve o melhor desempenho")
