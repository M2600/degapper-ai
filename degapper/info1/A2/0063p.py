setGroup(1)
while True:
    res = receive()
    if res == 1:
        playSound("歓喜の歌", repeat=True)
    else:
        stopSound("all")