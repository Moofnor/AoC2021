from time import perf_counter_ns
import numpy as np
from collections import Counter, defaultdict
from copy import copy


def readInput(dayno, isSample):
    if isSample:
        folder = 'sample'
    else:
        folder = 'input'
    with open(f'../data/{folder}/day{dayno}.txt', 'r') as f:
        data = f.readlines()

    return data

DAY = 12


class Day:
    def __init__(self, isSample):
        lines = readInput(DAY, isSample)
        # self.tunnels = [(p.strip().split("-")[0], p.strip().split("-")[1]) for p in lines]
        self.tunnels = defaultdict(list)
        for line in lines:
            start, end = line.strip().split("-")
            self.tunnels[start] += [end]
            self.tunnels[end] += [start]


    def part1(self):
        self.paths = []
        self.constructPath(["start"], "start", True)
        return len(self.paths)

    def part2(self):
        self.paths = []
        self.constructPath(["start"], "start", False)
        return len(self.paths)

    def constructPath(self, path, currentPoint, isPartOne):
        if currentPoint == "end":
            self.paths.append(path)
            return
        for nextpoint in self.tunnels[currentPoint]:
                # nextpoint = tunnel[tunnel.index(currentPoint) - 1]
                if isPartOne:
                    if nextpoint.islower() and nextpoint in path:
                        continue
                else:
                    if nextpoint.islower() and nextpoint in path:
                        if nextpoint == "start":
                            continue
                        if self.contains2small(path):
                            continue    
                newpath = copy(path)
                newpath.append(nextpoint)
                self.constructPath(newpath, nextpoint, isPartOne)

    def contains2small(self, path):
        c = [path.count(p) for p in path if (p.islower() and p is not "start")]
        if c == []:
            return False
        return max(c) >= 2


if __name__ == "__main__":
    start = perf_counter_ns()
    day = Day(False)

    print(day.part1()) 
    print(day.part2())
    stop = perf_counter_ns()
    print((stop-start) / 1000000)