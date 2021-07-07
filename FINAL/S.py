n = int(input())
a = list(map(int, input().split()))

for i in a:
    if i == max(a):
        print(1, end = ' ')
    else:
        print(0, end = ' ')