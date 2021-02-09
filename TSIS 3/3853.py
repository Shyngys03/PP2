a = input().split()
x = int(input())

for i in range(len(a)):
    if i - x > 0:
        print(a[i - x], end = ' ')