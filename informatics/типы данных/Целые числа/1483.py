a, b, c = map(int, input().split())
n, m, k = map(int, input().split())

print(((n - a) * 3600) + ((m - b) * 60) + k - c)