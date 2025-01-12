import sys

num_count = int(sys.stdin.readline())
num_list = []

for i in range(0,num_count):
  num = int(sys.stdin.readline())
  num_list.append(num)

num_list.sort()

for i in num_list:
  print(i)