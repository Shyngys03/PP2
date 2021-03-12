import re

n = int(input())

p = r'^(7|8|9)+\d{9}'

for i in range(n):
    s = input()
    if len(s) != 10:
        print("NO")
        continue
    if re.search(p, s):
        print("YES")
    else:
        print("NO")