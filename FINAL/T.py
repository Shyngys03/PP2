a, b, c, d = map(int, input().split())

if (b + d)/(a - c) == (b + d)//(a - c):
    print((b + d)//(a - c))
else:
    print((b + d)/(a - c))