def CheckPrime(n):
  hantei = "素数である"
  for warukazu in range(2, n):
    if n % warukazu == 0:
      hantei = "素数ではない"
  return hantei

def WritePrime():
  if cells[1][2] == "素数である":
    gyo = cells[rows.count]["A"].end("xlUp").Row + 1
    cells[gyo][1] = cells[1][1]

cells[2][1] = 2
for kazu in range(3, 10000, 2):
  cells[1][1] = kazu
  CheckPrime()
  WritePrime()