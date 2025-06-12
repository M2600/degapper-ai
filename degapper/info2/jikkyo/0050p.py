import requests, json
url = '国土地理院が提供している標高APIのURL'
latitude = input('緯度の入力')
longitude = input('経度の入力')
param = {'lat': latitude, 'log': longitude, 'outtype': 'JSON'}
res = requests.get(url, params=param)
data = json.loads(res.text)
print('標高＝', data['elevation'])