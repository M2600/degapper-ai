import random
member_num = 25
group_num = 3

group1_size = member_num // group_num
group2_size = group1_size + 1

group2_num = member_num % group_num
group1_num = group_num - group2_num

group_list = []
for i in range(group_num):
    group_list.append([])

set_num = []

for i in range(group_num) :
    if i < group1_num:
        set_num. append(group1_size)
    else:
        set_num. append(group2_size)

i = 0
while i < member_num:
    n = random. randint (1, group_num)
    if set_num[n-1] > 0:
        group_list[n-1].append(i+1)
    set_num[n-1] = set_num[n-1]- 1
    i=i+1

for i in range(group_num):
    print('グループ', (i+1), group_list[i])