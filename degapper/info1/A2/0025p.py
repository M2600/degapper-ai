import random
dic=[ 'Hello', 'Good Morning', 'Hi!']
for i in range(5):
    msg=input(random.choice(dic) + '>')
    dic.append(msg)