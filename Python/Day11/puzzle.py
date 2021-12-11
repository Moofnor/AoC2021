from time import perf_counter_ns
import numpy as np
from collections import deque


def readInput(dayno, isSample):
    if isSample:
        folder = 'sample'
    else:
        folder = 'input'
    with open(f'../data/{folder}/day{dayno}.txt', 'r') as f:
        data = f.readlines()

    return data

DAY = 11
EPOCHS = 100
FLASH = 9

class Day:
    def __init__(self, isSample):
        lines = readInput(DAY, isSample)
        self.grid = np.array([list(map(int, line.strip())) for line in lines])
     
    def run(self):
        self.num_flashed = 0
        epoch = 0
        while True:
            epoch += 1
            self.flashed = np.zeros(self.grid.shape)
            self.grid += 1
            for i, r in enumerate(self.grid):
                for j, c in enumerate(r):
                    if c > FLASH:
                        self.flash(i, j)
            
            if np.all(self.flashed == 1):
                self.part2(epoch)
                break

            for i, r in enumerate(self.grid):
                for j, c in enumerate(r):
                    if self.flashed[i, j] == 1:
                        self.grid[i, j] = 0
            
            if epoch == EPOCHS:
                self.part1()

    def part1(self):
        print(f"Part1: {self.num_flashed}")  

    def part2(self, epoch):
        print(f"Part2: {epoch}") 
    
    def flash(self, i, j):
        if self.flashed[i, j] == 1:
            return
        
        self.flashed[i, j] = 1
        self.num_flashed += 1

        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                if x==0 and y==0:
                    continue
                if ((i+x >=0 and i+x <self.grid.shape[0]) and (j+y >=0 and j+y <self.grid.shape[1])):
                    self.grid[i+x, j+y] += 1
                    if self.grid[i+x, j+y] > FLASH:
                        self.flash(i+x, j+y)


if __name__ == "__main__":
    start = perf_counter_ns()
    day = Day(False)
    day.run()
    # print(day.part1(1000)) 
    # print(day.part2())
    stop = perf_counter_ns()
    print((stop-start) / 1000000)