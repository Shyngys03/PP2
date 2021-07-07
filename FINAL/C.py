a = list(map(int, input().split()))

for i in a:
    if i != 0:
        print(i, end = ' ')

print('0 ' * a.count(0))