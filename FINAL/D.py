def is_palindrome(s):
    return s == s[::-1]

a = list(input().split())

d = {}
m = set()

for i in a:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1

for i in set(a):
    if is_palindrome(i) and d[i] == 1:
        m.add(i)

ans = list(set(a).difference(m))
ans.sort()
for i in ans:
    print(i)