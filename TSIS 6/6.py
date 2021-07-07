def find(a, b, x):
    if x in range(a, b):
        return True
    else:
        return False

a, b = map(int, input().split())
x = int(input())
print(find(a, b, x))