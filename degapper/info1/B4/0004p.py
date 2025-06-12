if flag.onClick():
    uriage = []
    uriage.append(56)
    uriage.append(34)
    uriage.append(63)
    uriage.append(81)
    pen.reset()
    pen.setThickness(20)
    pen.setColor("red")
    pen.position = [0, -150]
    pen.rotation = 0
    nanban = 1
    for i in range(4):
        pen.down()
        pen.move(uriage[nanban] * 2)
        pen.up()
        nanban += 1
        pen.position.x += 30
        pen.position.y = -150
    hide()
    