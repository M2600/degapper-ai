import matplotlib.pyplot as graph
import random

kakaku = 120
seisan_time = 30
wait_time = []
arrived_time = 0
start_time = 0
end_time = 0

for i in range(50):
    tmp_kankaku = int(kakaku * random.random())
    arrived_time = arrived_time + tmp_kankaku
    if arrived_time >= end_time:
        start_time = arrived_time
    else:
        start_time = end_time
    
    wait_time.append(start_time - arrived_time)
    end_time = start_time + seisan_time
print(wait_time)
graph.hist(wait_time, range(0, 60), bins=12)
graph.show()
