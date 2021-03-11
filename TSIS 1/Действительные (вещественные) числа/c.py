a = float(input())

if (a - int(a) == 0.5):
    print(int(a + 0.5))
else:
    print(int(round(a)))