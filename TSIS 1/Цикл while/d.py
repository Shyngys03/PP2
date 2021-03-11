a = int(input())

while(a % 2 == 0):
    a //= 2
print("YES" if a == 1 else "NO")