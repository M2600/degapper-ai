setGroup(1)
while True:
    res = recieve()
    if res > 50:
        show("Heart")
        soundPlay("sound1", repeat=True)
    else:
        show("")
        soundStop("all")