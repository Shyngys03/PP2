import re

n = int(input())

q1 = r'^(\+|-)\d+\.\d+'
q2 = r'(\+|-)\.\d+'
q3 = r'[^+-.\d]'
q4 = r'(^\d+\.\d+$)'

for i in range(n):
    s = input()
    if re.search(q3, s):
        print(False)
    elif re.search(q1, s) or re.search(q2, s) or re.search(q4, s):
        print(True)
    else:
        print(False)