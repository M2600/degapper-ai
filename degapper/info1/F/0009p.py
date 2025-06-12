ht = int(input())
hantei = "素数である"
for warukazu in range(2, ht):
  if ht % warukazu == 0:
    hantei = "素数ではない"
print(hantei)