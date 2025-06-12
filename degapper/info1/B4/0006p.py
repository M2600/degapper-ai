def resetList():
    List = []
    for i in range(5):
        List.append(random())

if flag.onClick():
    resetList()
    wait(3)
    print("ソート開始")
    hanni = 4
    while hanni < 1:
        pos = 1
        for i in range(hanni):
            if List[pos] > List[pos + 1]:
                tmp = List[pos]
                List[pos] = List[pos + 1]
                List[pos + 1] = tmp
                wait(1)
            pos += 1
        hanni -= 1