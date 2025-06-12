b = input('数値の複数入力')
a = b.split(',')
sum = 0
for i in range(0, len(a), 1):
    sum =sum + int(a[i])
print('合計= ', sum)