s = input()

print(s[2])
print(s[len(s) - 2])
print(s[0] + s[1] + s[2] + s[3] + s[4])
for i in range(len(s) - 2):
    print(s[i], end = '')
print()
for i in range(0, len(s), 2):
    print(s[i], end = '')
print()
for i in range(1, len(s), 2):
    print(s[i], end = '')
print()
for i in range(len(s) - 1, -1, -1):
    print(s[i], end = '')
print()
for i in range(len(s) - 1, -1, -2):
    print(s[i], end = '')
print()
print(len(s))