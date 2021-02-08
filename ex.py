from math import pow

sum = 0

for i in range(1, 10):
    n = ((-1) ** i) * (4 / 2 * i + 1)
    sum += n

print(sum)