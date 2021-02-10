a = input().split()
x = int(input())

for i in range(len(a)):
    if x >= 0:
        print(a[i - x], end = ' ')
    else:
        print(a[len(a) - abs(x) + i - 1], end = ' ')