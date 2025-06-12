tate = 100
yoko = 200
ActiveSheet.Shapes.Range(Array("RB")).Top = tate
ActiveSheet.Shapes.Range(Array("RB")).Left = yoko
ActiveSheet.Shapes.Range(Array("RB")).Rotation = 0
for gyo in range(2, 22):
  cells[gyo][1].Interior.Color = RGB(255, 255, 0)
  cells[2][4] = cells[gyo][1]
  ActiveSheet.Shapes.Range(Array("RB")).Rotation = (cells[2][4] -1) * 90
  tate = tate - cells[2][5] * 20
  yoko = yoko + cells[2][6] * 20
  if tate < 0:
    tate = 0
  if yoko < 0:
    yoko = 0
  ActiveSheet.Shapes.Range(Array("RB")).Top = tate
  ActiveSheet.Shapes.Range(Array("RB")).Left = yoko
  Application.Wait(Now + TimeValue("0:00:01"))
  cells[gyo][1].Interior.Color = RGB(2558, 255, 255)