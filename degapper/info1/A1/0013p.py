import random
cut=0
for i in range(10000):
    r=random.randint(1,6)
    if r==1:
        cnt=cnt+1
p=cnt/10000
print(p)