def perfect(x):
    cnt = 0
    for i in range(1, x):
        if x % i == 0:
            cnt += i
    if x == cnt:
        return True
    else:
        return False

print(perfect(int(input())))