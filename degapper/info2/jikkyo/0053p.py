f = open('data.txt', mode='r', encoding='utf-8')
list = f.readlines()
for line in list:
    print(line, end='')
f.close()