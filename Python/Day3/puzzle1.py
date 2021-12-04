import numpy as np

with open('Day3/sample.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

bit_len = len(data[0])

counter = [[0, 0] for bit in range(bit_len)]

for number in data:
    for i, bit in enumerate(number):
        if bit == '1':
            counter[i][1] += 1
        else:
            counter[i][0] += 1

gamma = "".join([str(np.argmax(x)) for x in counter])
epsilon = "".join([str(np.argmin(x)) for x in counter])


x=int(gamma,2)
y=int(epsilon,2)

print(x*y)