data = [5, 4, 3, 2, 1]
n = len (data)

for i in range (n, 1, -1):
    for j in range (i-1): 
        if data[j] > data[j+1]:
            k = data[j]
            data[j] = data[j+1]
            data[j+1] = k
        print(data)