s = input()

t = str()
maxi = str()
cnt = 0
mx = 0

for i in s:
    if i != ' ':
        t = t.join(i)
        cnt += 1
    
    elif i == ' ':
        if mx < cnt:
            mx = cnt
            maxi = t
        cnt = 0
        t = 0

print(maxi, '\n', mx)