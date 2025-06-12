a = [57,16,99,10,45]; n = len(a)
print('番号', ' ', 'データ')
for i in range(0, n, 1):
    print(i, '　　　', a[i])
print('')
s = int(input('探索値の入力'))
for i in range(0, n, 1):
    if a[i] == s:
        print(s, 'は', i , '番目に存在します')
        break