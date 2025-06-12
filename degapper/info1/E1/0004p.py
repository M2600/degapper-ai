import random
set_num = [6, 7, 7]
group_list_1 = []
group_list_2 = []
group_list_3 = []

i = 0
while i < 20:
    n = random.randint(1, 3)
    if set_num[n-1] > 0:
        if n == 1:
            group_list_1.append(i+1)
        elif n == 2:
            group_list_2.append(i+1)
    else:
        group_list_3.append(i+1)
    set_num[n-1] = set_num[n-1] - 1
    i = i + 1
print('グループ1', group_list_1)
print('グループ2', group_list_2)
print('グループ3', group_list_3)