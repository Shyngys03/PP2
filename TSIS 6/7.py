s = input()

CNT = 0
cnt = 0
for i in s:
    if i.isupper():
        CNT += 1
    elif i.islower():
        cnt += 1
print('Number of upper case: ' + str(CNT))
print('Number of lower case: ' + str(cnt))