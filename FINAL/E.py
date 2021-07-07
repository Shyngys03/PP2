def is_prime(x):
    if x == 1 or x == 0:
        return False
    if x == 2:
        return True
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in b:
    a.append(i)

d = {}

for i in a:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1
    
for i in set(a):
    if (not is_prime(i)) and (d[i] > 1):
        print(i, end = ' ')