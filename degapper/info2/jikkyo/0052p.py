f = open('data.txt', mode='r', encoding='utf-8')
line = f.readline()
while line != '':
    print(line, end='')
    line = f.readline()
f.close()