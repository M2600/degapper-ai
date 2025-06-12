def CheckPrime(n):
  hantei = "素数である"
  for warukazu in range(2, n):
    if n % warukazu == 0:
      hantei = "素数ではない"
  return hantei

n = int(input("対象を入力してください"))
CheckPrime(n)