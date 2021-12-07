import numpy as np
from time import perf_counter_ns

def readInput(dayno, isSample):
    if isSample:
        folder = 'sample'
    else:
        folder = 'input'
    with open(f'../data/{folder}/day{dayno}.txt', 'r') as f:
        data = f.readlines()

    return data

class Day7():

    def __init__(self, isSample = False):
        self.crabs = np.array([int(x) for x in readInput(7, isSample)[0].split(',')])

    def part1(self):
        med = np.median(self.crabs)
        dist = np.sum([np.abs(crab - med) for crab in self.crabs])

        return dist

    def part2(self):
        crabmax = np.max(self.crabs)
        mindist = np.inf

        for i in range(crabmax):
            dist = [(np.abs(crab - i) * (np.abs(crab - i) + 1))/2 for crab in self.crabs]
            tot_dist = np.sum(dist)
            if tot_dist < mindist:
                mindist = tot_dist
        
        return mindist



if __name__ == "__main__":
    start = perf_counter_ns()
    day = Day7(True)

    print(day.part1()) 
    print(day.part2())
    stop = perf_counter_ns()
    print((stop-start) / 1000000)