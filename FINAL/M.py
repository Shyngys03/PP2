s = input()


d = {}

for i in sorted(s):
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1

print(len(d))
for i in d:
    print(i, d[i])