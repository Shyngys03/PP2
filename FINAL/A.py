def check_power_of_3(x):
    while x % 3 == 0:
        x //= 3
    if x == 1:
        return True
    else:
        return False

a, b = map(int, input().split())

for i in range(b, a, -1):
    if check_power_of_3(i) and (len(str(i)) == 4):
        print(i, end = ' ')