def isPrime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return True
    return False

print(isPrime((int(input()))))