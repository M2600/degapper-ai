a = [88,43,27,65]; n = len (a)
print('整列前')
print('番号', ' ', 'データ')
for i in range(0, n, 1):
    print(i,'　　　',a[i])
print('')
input('Enterを押すと整列を開始')
print('')
for i in range (0 , n-1 , 1):
    for j in range(i+1 , n, 1):
        if a[i] > a[i]:
            temp = a [i]
            a[i] = a[i]
            a [j] = temp
print('整列後')
print('番号', '', 'データ')
for i in range(0, n, 1):
    print(i,'　　　',a[i])
print('')
print("整列は終了しました")