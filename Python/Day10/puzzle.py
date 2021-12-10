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

OPENING = ("([{<")
CLOSING = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"}
SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}


class Day10:
    def __init__(self, isSample):
        self.lines = readInput(10, isSample)
      
        
    def part1(self):
        score1 = 0
        self.score2 = []
        for line in self.lines:
            line = line.strip()
            pairs = deque()
            corrupt = False
            for b in line:
                if b in OPENING:
                    pairs.append(b)
                else:
                    o = pairs.pop()
                    if o != CLOSING.get(b):
                        score1 += SCORES.get(b, None)
                        corrupt = True
                        break
            
            # Part 2
            if not corrupt:
                score2 = 0
                while len(pairs) > 0:
                    i = pairs.pop()
                    score2 *= 5
                    score2 += SCORES.get(i, None)
                self.score2.append(score2)
            
        return score1

    def part2(self):
        score = sorted(self.score2)
        return score[len(score) // 2]

   

if __name__ == "__main__":
    start = perf_counter_ns()
    day = Day10(False)

    print(day.part1()) 
    print(day.part2())
    stop = perf_counter_ns()
    print((stop-start) / 1000000)