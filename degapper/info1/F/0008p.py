def Kuji():
  for retu in range(1, 4):
    cells[1, retu] = int(random() * 10)

def Hantei():
  a = cells[1, 1]
  b = cells[1, 2]
  c = cells[1, 3]
  if a == b and b == c:
    cells[1, 4]
  else:
    cells[1, 4] = ""

def Start():
  Kuji()
  Hantei()

Start()
kaisu = 1
while cells[1, 4] == "あたり":
  Start()
  kaisu = kaisu + 1
print("回数は", kaisu)