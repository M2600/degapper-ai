import_random
dice=[0,0,0,0,0,0]
i=1000
while (i>0):
    r=random.randrange (6)
    dice[r]=dice[r]+1
    i=i-1
print (dice)