s = input()

t = ""
maxi = ""
cnt = 0
mx = 0

for i in s:
    if i != ' ':
        t += i
        maxi += i
        cnt += 1
    
    elif i == ' ':
        if mx < cnt:
            mx = cnt
            