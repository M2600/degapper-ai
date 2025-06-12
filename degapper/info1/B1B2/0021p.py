tl = input('気温[℃]の入力　')
fp = open('data.csv', 'rt')
for b in fp:
    a = b.split(',')
    date = a [0]
    t2 = a[1]
    if float(t2) >= float(t1):
        print(date + ' : ' + t2)
fp.close ()