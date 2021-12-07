def readInput(dayno, isSample):
    if isSample:
        folder = 'sample'
    else:
        folder = 'input'
    with open(f'../data/{folder}/day{dayno}.txt', 'r') as f:
        data = f.readlines()

    return data

class Day5():
    def __init__(self, isSample = False):
        data = readInput(5, isSample)
        self.lines = [[(int(x[0][0]), int(x[0][1])), (int(x[1][0]), int(x[1][1]))] for x in [[c[0].strip().split(","), c[1].strip().split(",")] for c in [line.split("->") for line in data]]]

        pass


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
            
            elif line[0][1] == line[1][1]:
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
                    if line[0][1] > line[1][1]:
                        s = 1
                    else:
                        s = -1
                    while x >= line[1][0]:
                        self.addpoint(x, y)
                        x -= 1
                        y -= s
                else:
                    if line[0][1] > line[1][1]:
                        s = -1
                    else:
                        s = 1
                    while x <= line[1][0]:
                        self.addpoint(x, y)
                        x += 1
                        y += s

        print(len(self.pass2p))
    def addpoint(self, x, y):
        if (x, y) in self.pass1:
            self.pass2p.add((x, y))
        else:
            self.pass1.add((x, y))

if __name__ == "__main__":
    day = Day5()

    day.part1()