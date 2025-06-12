a = [10, 16, 45, 57, 99]; n = len(a)
print('番号', ' ', 'データ')
for i in range(0, n, 1):
    print(i,'　　　',a[i])
print('')
s = int(input("探索値の入力"))
i= 0; j = n-1
while i <= j:
    m = int((i + j)/2)
    if a[m] == s:
        print(s, 'は', m, '番目に存在')
        break
    if a[m] > s:
        j = m - 1
    else:
        i = m + 1