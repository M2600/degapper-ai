import matplotlib.pyplot as plt
x = []; y1 = []; y2 = []
num0 = 14; num1 = 11; dt =1; nen =0
rate0 = 0.01; rate1 = 0.06
for i in range (0,11,1):
    x.append(nen)
    y1.append(num0)
    y2.append(num1)
    nen = nen + dt
    numO = numO + rate0 * numO * dt
    num1 = num1 + rate1 * num1 * dt
plt.plot(x, y1, color='blue', label='city A', marker='o')
plt.plot(x, y2, color='red', label='city B', marker='o')
plt. legend()
plt.title('JINKOU YOSOKU')
plt.xlabel('Jikan [nen]')
plt.ylabel('Jinkou[mannin]')
plt.show ()