def Kuji():
  for retu in range(1, 4):
    cells[1, retu] = int(random() * 10)

def Hantei():
  a = cells[1, 1]
  b = cells[1, 2]
  c = cells[1, 3]
  if a == b and b == c:
    print("あたり")
  else:
    print("")

Kuji()
Hantei()