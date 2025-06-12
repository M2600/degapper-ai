if flag.onClick():
  x = input("あなたの名前はなんですか？")
  if x == "":
    name = "名無し"
  else:
    name = x
print(x, "さん")