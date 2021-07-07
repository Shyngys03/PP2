n, m = map(int, input().split())

for i in range(n):
    for j in range(m):
        if j < m / 2 and i < n / 2:
            print(1, end = ' ')
        elif j >= m / 2 and i < n / 2:
            print(0, end = ' ')
        elif j < m / 2 and i >= n / 2:
            print(2, end = ' ')
        elif j >= m / 2 and i >= n / 2:
            print(3, end = ' ')
    print()