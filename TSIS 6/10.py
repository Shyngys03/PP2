def evenl(a):
    l = []
    for i in a:
        if i % 2 == 0:
            l.append(i)
    return l

a = list(map(int, input().split()))