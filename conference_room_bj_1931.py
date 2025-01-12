import sys

n = int(sys.stdin.readline())
time_pair = []

for i in range(n):
  start, end = sys.stdin.readline().split()
  time_pair.append([int(start),int(end)])
  
sorted_time = sorted(time_pair, key = lambda x: (x[1],x[0]))

count = 1
last_end_time = sorted_time[0][1]

for i in range(1,n):
  if(sorted_time[i][0] >= last_end_time):
    count += 1
    last_end_time = sorted_time[i][1]
    
print(count)