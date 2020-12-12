import random

random.seed(2020) 

MIN = 100
MAX = 120
n = 0

num_list = []
mode_dict = {}


for i in range(20):
    ran_num = random.randint(MIN,MAX) 
    num_list.append(ran_num) 

n = len(num_list)
num_list_sorted = sorted(num_list)
print(num_list_sorted)

if n % 2 == 0:
    median1 = num_list_sorted[n//2] 
    median2 = num_list_sorted[n//2 - 1] 
    median = (median1 + median2)/2
else: 
    median = num_list_sorted[n//2] 

print("Median Value is: " + str(median))

#mode calculation
for j in num_list_sorted:
    if j in mode_dict:
        mode_dict[j] += 1
    else:
        mode_dict[j] = 1

mode = [k for (k,v) in mode_dict.items() if v == max(list(mode_dict.values()))]

print("Mode Value(s) is/are :" + str(mode))