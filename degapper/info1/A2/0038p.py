import_requests
url='https://tosho.high.proguru.jp/api/weather'
params={
    'code':4410,
    'date':'today'
}

response=requests.get(url,params)
prob=response['rain'][5]['prob']
print(prob)

if prob>=50:
    print('傘を持って出かけましょう')
else:
    print('今日、雨は降らないでしょう')