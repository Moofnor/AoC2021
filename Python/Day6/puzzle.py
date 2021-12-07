from tqdm import tqdm
from time import perf_counter_ns

def readInput(dayno, isSample):
    if isSample:
        folder = 'sample'
    else:
        folder = 'input'
    with open(f'../data/{folder}/day{dayno}.txt', 'r') as f:
        data = f.readlines()

    return data

class Day5():
    AGE_OF_NEW_FISH = 8
    AGE_OF_FISH = 6

    def __init__(self, isSample = False):
        self.fish = [int(x) for x in readInput(6, isSample)[0].split(',')]

    def part1(self, number_of_days):
        
        for day in range(number_of_days):
            for i, fish in enumerate(self.fish):
                fish -= 1
                if fish < 0:
                    fish = self.AGE_OF_FISH
                    self.fish.append(self.AGE_OF_NEW_FISH + 1)
                self.fish[i] = fish
        return len(self.fish)

    def part2(self, number_of_days):
        daysOfBirth = {day: [0, 0, 0] for day in range(7)}
        for fish in self.fish:
            daysOfBirth[(fish + 1) % 7][0] = daysOfBirth.get((fish + 1) % 7)[0] + 1
        
        for day in range(number_of_days + 1):
            weekday = day % 7
            new_fish_day = (weekday + 2) % 7
            daysOfBirth[new_fish_day][1] = daysOfBirth[weekday][0]
            daysOfBirth[weekday][0] += daysOfBirth[weekday][1]
            daysOfBirth[weekday][1] = 0
            total = 0

            for dayf in daysOfBirth.items():
                total += dayf[1][0] + dayf[1][1]

        return total


if __name__ == "__main__":
    start = perf_counter_ns()
    day = Day5(False)

    # print(day.part1(80)) 
    print(day.part2(256))
    stop = perf_counter_ns()
    print((stop-start) / 1000000)