import random
saikoro = [1000, 0, 0, 0, 0, 0, 0]
for i in range(saikoro[0]):
    kazu = random.randint(1, 6)
    saikoro[kazu] = saikoro[kazu] + 1
print(saikoro)
