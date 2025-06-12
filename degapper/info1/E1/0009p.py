import random
set_num = [6, 7, 7]
group_list = []
member = []
member_flag = []

for i in range(20) :
    member_flag.append(0)

def koukan(data) :
    n = len(data)
    for i in range(n, 1, -1):
        for j in range(i-1):
            if data[j] > data[j+1]:
                k = data[j]
                data[j] = data[j+1]
                data[j+1] = k
    return data[3]

i = 0
while i < 20:
    n = random. randint (1, 20)
    if member_flag[n-1] == 0:
        member.append(n)
        member_flag[n-1] = 1
        i=i+1

slice_start = 0
for i in range (3):
    slice_end = slice_start + set_num[i]
    group_work = member [slice_start: slice_end]
    group_list. append (group_work)
    slice_start = slice_end

for i in range (3) :
    print('グループ', (i+1), koukan(group_list[i]))