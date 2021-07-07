def is_prime(x):
    if x == 1 or x == 0:
        return False
    if x == 2:
        return True
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

a, b = map(int, input().split())

for i in range(b, a - 1, -1):
    if is_prime(i):
        print(i, end = ' ')