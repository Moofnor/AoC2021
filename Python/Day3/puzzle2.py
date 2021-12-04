import numpy as np
import copy

def runbit(data, i):
    counter = [0, 0]
    split_data = [[],[]]

    for number in data:
        if number[i]=="1":
            counter[1] += 1
            split_data[1].append(number)
        else:
            counter[0] += 1
            split_data[0].append(number)

    return counter, split_data
    
with open('Day3/input.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

ox_data = copy.deepcopy(data)
n_bit = 0
while len(ox_data) > 1:
    counter, split_data = runbit(ox_data, n_bit)
    if counter[0] == counter[1]:
        counter[1] += 1
    ox_data = split_data[np.argmax(counter)]
    n_bit += 1

co_data = copy.deepcopy(data)
n_bit = 0
while len(co_data) > 1:
    counter, split_data = runbit(co_data, n_bit)
    if counter[0] == counter[1]:
        counter[1] += 1
    co_data = split_data[np.argmin(counter)]
    n_bit += 1

x=int(ox_data[0],2)
y=int(co_data[0],2)

print(x * y)

