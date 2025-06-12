import matplotlib.pyplot as graph

uriage = []

saidai_x = 0
saidai_uriage = 0

for x in range(223):
    kosuu1 = int((2000 - 9 * x) / 6)
    kosuu2 = int((2500 - 10 * x) / 9)
    if kosuu1 >= kosuu2:
        y = kosuu2
    else:
        y = kosuu1
    tmp_uriage = 20 * x + 16 * y
    uriage.append(tmp_uriage)
    
    if saidai_uriage < tmp_uriage:
        saidai_uriage = tmp_uriage
        saidai_x = x

print(saidai_x, saidai_uriage)
graph.plot(uriage)
graph.show()