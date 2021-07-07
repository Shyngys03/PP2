def unique(a):
    l = []
    for i in a:
        if not(i in a):
            l.append(i)
    return l

a = list(map(int, input().split()))

print(*unique(a))