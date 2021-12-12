from time import perf_counter_ns
import numpy as np


def readInput(dayno, isSample):
    if isSample:
        folder = 'sample'
    else:
        folder = 'input'
    with open(f'../data/{folder}/day{dayno}.txt', 'r') as f:
        data = f.readlines()

    return data

class Day9:
    def __init__(self, isSample):
        lines = readInput(9, isSample)
        self.grid = [list(map(int, line.strip())) for line in lines]
        self.shape = (len(self.grid), len(self.grid[0]))
        
    def part1(self):
        risk = 0
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                values = np.array([
                   self.getNeighbour(i+1, j),
                   self.getNeighbour(i-1, j),
                   self.getNeighbour(i, j+1),
                   self.getNeighbour(i, j-1)
                ])
                if self.grid[i][j] < np.min(values):
                    risk += (self.grid[i][j] + 1)
        return risk

    def part2(self):
        self.checked = []
        self.basins = [[]]
        self.basinGrid = np.zeros(self.shape)
        nBasin = 1
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if (i, j) in self.checked:
                    continue
                self.growBasin(i, j, nBasin)
                nBasin += 1
                self.basins.append([])
        return np.prod(sorted([len(x) for x in self.basins])[-3:])

    def growBasin(self, i, j, nBasin):
        if (i, j) in self.checked or self.getNeighbour(i, j) >= 9:
            return
        self.checked.append((i, j))
        self.basins[nBasin-1].append((i, j))
        self.basinGrid[i, j] = nBasin
        self.growBasin(i+1, j, nBasin)
        self.growBasin(i-1, j, nBasin)
        self.growBasin(i, j+1, nBasin)
        self.growBasin(i, j-1, nBasin)


    def getNeighbour(self, i, j):
        if ((i < 0 or i > self.shape[0]-1) or(j < 0 or j > self.shape[1]-1)):
            return 11
        else:
            return self.grid[i][j]


if __name__ == "__main__":
    start = perf_counter_ns()
    day = Day9(False)

    print(day.part1()) 
    print(day.part2())
    stop = perf_counter_ns()
    print((stop-start) / 1000000)