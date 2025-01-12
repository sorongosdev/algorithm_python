import sys

lope_num = int(sys.stdin.readline())
lope_list = []
max_weight = 0

for i in range(0,lope_num):
  lope_list.append(int(sys.stdin.readline()))

lope_list.sort()

for index, value in enumerate(lope_list):
  weight = value * (lope_num - index)
  if max_weight < weight:
    max_weight = weight

print(max_weight)