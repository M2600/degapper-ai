import_requests
url='https://tosho.high.proguru.jp/api/weather'
params={
    'code':4410,
    'date':'today'
}

response=requests.get(url,params)
print(response)