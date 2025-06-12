stations =['天王寺', '寺田町', '桃谷', '鶴橋', 
            '玉造', '森ノ宮', '大阪城公園', '京橋', 
            '桜ノ宮', '天满', '大阪', '福島', 
            '野田', '西九条', '弁天町', '大正', 
            '芦原橋', '今宮', '新今宮']
print('駅番号を入力してください')
station_number = input ()
number = int (station_number)
if number > 0 and number < 20:
    print(stations[number - 1], '駅です')
else:
    print('該当する駅はありません')