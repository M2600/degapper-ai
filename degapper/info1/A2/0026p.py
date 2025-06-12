import random
dic=[ 'Hello', 'Good Morning', 'Hi!']
for i in range(5):
    msg=input(random.choice(dic) + '>')
    if msg not in dic:
        dic.append(msg)
print(dic)