from time import perf_counter_ns
import numpy as np
from numpy.core.fromnumeric import reshape

def readInput(dayno, isSample):
    if isSample:
        folder = 'sample'
    else:
        folder = 'input'
    with open(f'../data/{folder}/day{dayno}.txt', 'r') as f:
        data = f.readlines()

    return data


class Day8():
    digitDict = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6
    }
    digitLen = {
        2: 1,
        4: 4,
        3: 7,
        7: 8
    }
    def __init__(self, isSample = False):
        self.lines = readInput(8, isSample)
    

    def part2(self):
        result = []
        for line in self.lines:
            digits, display = line.split(" | ")
            mapping = {str("".join(sorted(digit))):self.digitLen.get(len(digit), None) for digit in digits.split(" ")}
            rev_mapping = {item: key for key, item in mapping.items()}
            segments = {}

            segments['a'] = "".join(set(rev_mapping[7]).symmetric_difference(rev_mapping[1]))
            sevenFour = set(rev_mapping.get(7) + rev_mapping.get(4))
            for digit in mapping.keys():
                if len(digit) == 6:
                    if all(d in digit for d in sevenFour):
                        mapping[digit] = 9
                        rev_mapping[9] = digit
                        segments['e'] = "".join(set(digit).symmetric_difference(set(rev_mapping[8])))
                        break
            for digit in mapping.keys():
                if len(digit) == 6:
                    if (len(set(digit).symmetric_difference(set(rev_mapping[8]))) == 1 and len(set(digit).symmetric_difference(set(rev_mapping[9]))) == 2):
                        if len(set(digit).symmetric_difference(set(rev_mapping[1]))) == 4:
                            mapping[digit] = 0
                            rev_mapping[0] = digit
                            segments['d'] = "".join(set(digit).symmetric_difference(rev_mapping[8]))
                        else:
                            mapping[digit] = 6
                            rev_mapping[6] = digit
                            segments['c'] = "".join(set(digit).symmetric_difference(rev_mapping[8]))

            for digit in mapping.keys():
                if len(digit) == 5:
                    if len(set(digit).symmetric_difference(set(rev_mapping[1]))) == 3:
                        mapping[digit] = 3
                        rev_mapping[3] = digit
                    elif len(set(digit).symmetric_difference(set(rev_mapping[6]))) == 1:
                        mapping[digit] = 5
                        rev_mapping[5] = digit
                    elif len(set(digit).symmetric_difference(set(rev_mapping[6]))) == 3:
                        mapping[digit] = 2
                        rev_mapping[2] = digit
            mapping_result = {key: item for item, key in rev_mapping.items()}
            rc = ''
            for disp in display.split(" "):
                dispres = mapping_result.get(str("".join(sorted(disp.strip()))))
                if dispres == None:
                    print('e')
                rc += (str(dispres))
            result.append(int(rc))

        return sum(result)

    def part1(self):
        counter =0
        for line in self.lines:
            digits, display = line.strip().split(" | ")
            for disp in display.split(" "):
                if len(disp) in (2, 4, 3, 7):
                    counter += 1
        return counter





if __name__ == "__main__":
    start = perf_counter_ns()
    day = Day8(False)

    print(day.part1()) 
    print(day.part2())
    stop = perf_counter_ns()
    print((stop-start) / 1000000)