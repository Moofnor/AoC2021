with open("Day1/input.txt", 'r') as f:
    depth = f.readlines()

inc = 0
for i in range(3, len(depth)):
    if int(depth[i]) > int(depth[i-3]):
        inc += 1

print(inc)