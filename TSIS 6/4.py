def f(a):
    cnt = 1
    for i in a:
        cnt *= i
    return cnt

print(f(list(map(int, input().split()))))