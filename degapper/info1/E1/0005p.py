import random
set_num = [6, 7, 7]
group_list_1 = []
group_list_2 = []
group_list_3 = []
member = []
member_flag = []

for i in range (20):
    member_flag.append (0)

i = 0
while i < 20:
    n = random. randint (1, 20)
    if member_flag[n-1] == 0:
        member.append(n)
        member_flag[n-1] = 1
        i = i + 1

slice_start = 0
for i in range (3):
    slice_end = slice_start + set_num[i]
    group_work = member[slice_start : slice_end]
    if i == 0:
        group_list_1 = group_work
    elif i == 1:
        group_list_2 = group_work
    else:
        group_list_3 = group_work
    slice_start = slice_end

print('グループ1', group_list_1)
print('グループ2', group_list_2)
print('グループ3', group_list_3)