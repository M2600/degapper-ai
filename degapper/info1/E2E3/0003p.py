def NokoriJikan(start):
  countDown = start
  while countDown >= 1:
    print("カウントダウン")
    countDown -= 1

def Run():
  LimitRotation("LR")
  while True:
    move(10)
    setNextCostume()
    if touchWall():
      Bounce()

if flag.onClick():
  NokoriJikan(10)
  Run()