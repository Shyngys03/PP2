from math import factorial

a = int(input())
cnt = 0
for i in range(1, a + 1):
    cnt += factorial(i)
print(cnt)