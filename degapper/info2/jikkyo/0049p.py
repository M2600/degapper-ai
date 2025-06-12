import requests, json
url = 'http://サーバのIPアドレスポート番号/cgi-bin/calc3.py'
n1 = input('被加数の入力')
n2 = input('加数の入力')
param = {'num1': n1, 'num2': n2}
res = requests.get(url, params=param)
data = json.loads(res.text)
print(data)