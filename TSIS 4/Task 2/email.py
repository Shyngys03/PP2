import re

n = int(input())
q = r'\w+\s(<[a-zA-Z]{1}[\w._-]+?@[a-z]+.[a-z]{1,3}>)'

for i in range(n):
    s = input()
    if re.search(q, s):
        print(s)