def sosu_hantei(ht):
    hantei = True
    for warukazu in range (2, ht):
        if ht % warukazu == 0 :
            hantei = False
    return hantei

sosu = []
sosu.append (2)
for kazu in range (3, 10001, 2):
    if (sosu_hantei(kazu)):
        sosu.append(kazu)
print(sosu)