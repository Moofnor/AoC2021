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



def part1(self):
        self.pass1 = set()
        self.pass2p = set()

        for line in self.lines:
            if line[0][0] == line[1][0]:
                x, y = line[0]
                if line[0][1] > line[1][1]:
                    while y >= line[1][1]:
                        self.addpoint(x, y)
                        y -= 1
                else:
                    while y <= line[1][1]:
                        self.addpoint(x, y)
                        y += 1
            
            if line[0][1] == line[1][1]:
                x, y = line[0]
                if line[0][0] > line[1][0]:
                    while x >= line[1][0]:
                        self.addpoint(x, y)
                        x -= 1
                else:
                    while x <= line[1][0]:
                        self.addpoint(x, y)
                        x += 1
            else:
                x, y = line[0]
                if line[0][0] > line[1][0]:
                    while x >= line[1][0]:
                        self.addpoint(x, y)
                        x-=1
                        y-=1
                else:
                    while x <= line[1][0]:
                        self.addpoint(x, y)
                        x += 1
                        y-= 1