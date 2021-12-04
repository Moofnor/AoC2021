with open('Day2/input.txt', 'r') as f:
    moves = f.readlines()

x, depth1, depth2, aim = 0, 0, 0, 0
for i, move in enumerate(moves):
    command, value = move.split(' ')
    value_f = float(value)
    if command == 'forward':
        x += value_f
        depth2 += aim*value_f
    elif command == 'up':
        aim -= value_f
        depth1 -= value_f
    elif command == 'down':
        aim += value_f
        depth1 += value_f
    else:
        raise Exception("Unknown command")

print(f"Result 1: {x*depth1}")
print(f"Result 2: {x*depth2}")