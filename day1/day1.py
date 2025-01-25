import heapq
import re
from collections import Counter
list1,list2 = [],[]
total_lines = 0
with open('input.txt','r') as file:
    lines = file.readlines()
    for line in lines:
        first_number, second_number  = re.sub(r"( )+",",",line).split(',')
        list1.append(int(first_number))
        list2.append(int(second_number))
        total_lines += 1
heapq.heapify(list1)
heapq.heapify(list2)

sum = 0
for i in range(len(list1)):
    smallest_list_1 = heapq.heappop(list1)
    smallest_list_2 = heapq.heappop(list2)
    sum += abs(smallest_list_1 - smallest_list_2)
print("Sum:",sum)
# read the lines again
with open('input.txt','r') as file:
    lines = file.readlines()
    for line in lines:
        first_number, second_number = re.sub(r'( )+',",",line).split(',')
        list1.append(int(first_number))
        list2.append(int(second_number))


freq_map_2 = Counter(list2)
total_sim_score = 0
for number in list1:
    sim_score = 0
    if number in freq_map_2:
        sim_score = number * freq_map_2[number]
    total_sim_score += sim_score
    
print("Total Sim Score",total_sim_score)

       