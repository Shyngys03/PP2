import re

with open('3.txt', 'r', encoding = 'utf-8') as f:
    data = f.read()

name = re.search(r'Филиал\sТОО\s\w+\s\w+', data).group()
BIN = re.search(r'\d{12}', data).group()
items = re.findall(r'\d+\.\n(.*)', data)
cnt = re.findall(r'(\d),\d{3}', data)
price = re.findall(r'x\s([\d\s]+,\d+)', data)
total = re.findall(r'Стоимость\n([\d\s]+,\d+)', data)
date = re.search(r'\d{2}\.\d{2}\.\d{4}\s\d{2}\:\d{2}\:\d{2}', data)
address = re.search(r'г\.\s[\w\-]+\,\w+\,\s[\w+\s]+\,\d+\,\s\w+\-\d', data)
print()
print("1. Name of the company: " + name)
print("2. BIN number: " + BIN)
print()
for i in range(len(items)):
    print("1. Title: " + items[i])
    print("\t2. Count: " + cnt[i])
    print("\t3. Unit price: " + price[i])
    print("\t4. Total price: " + total[i])
    print()

print('Date - ' + date.group())
print('Address - ' + address.group())