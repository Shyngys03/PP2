a = int(input())

hour = a // 3600
minute = (a // 60) % 60

print('It is ' + str(hour) + ' hours ' + str(minute) + ' minutes.')