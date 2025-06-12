import random
member_num = 25
group_num = 3

group1_size = member_num // group_num
group2_size = group1_size + 1

group2_num = member_num % group_num
group1_num = group_num - group2_num

group_list_1 = []
group_list_2 = []
group_list_3 = []

set_num = []

for i in range(group_num) :
    if i < group1_num:
        set_num. append(group1_size)
    else:
        set_num. append(group2_size)

i = 0
while i < member_num:
    n = random. randint(1, group_num)
    if set_num[n-1] > 0:
        if n == 1:
            group_list_1.append(i+1)
        elif n == 2:
            group_list_2.append(i+1)
    else:
        group_list_3.append(i+1)
    set_num[n-1] = set_num[n-1] - 1
    i=i+1

print('グループ1', group_list_1)
print('グループ2', group_list_2)
print('グループ3', group_list_3)
