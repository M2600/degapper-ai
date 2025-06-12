a = [ ]
a.append({'名前' : '佐藤健太', '電話' : '012-345-67891' , '部活動' : 'サッカー'})
a.append({'名前' : '鈴木美香', '電話' : '098-765-43217'})
a.append({'名前' : '渡辺梨花', '部活動' : '吹奏楽'})
for i in range (0, len(a), 1):
    for key in a[i]:
        print(key , ' : ', a[i][key])
    print('')