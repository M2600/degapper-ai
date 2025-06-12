import requests
url = 'http://サーバのIPアドレスポート番号/cgi-bin/calc2.py'
n1 = input('被加数の入力')
n2 = input('加数の入力')
param = {'num1': n1, 'num2': n2}
res = requests.get(url, params=param)
print(res.text)