if flag.onClick():
    costume = loadImage("コスチューム１")
    wait(1)
    costume = loadImage("コスチューム２")
    WaitKey()
    if buttom.pressed("1"):
        costume = loadImage("コスチューム３")
    else:
        if buttom.pressed("2"):
            costume = loadImage("コスチューム４")
        else:
            costume = loadImage("コスチューム２")