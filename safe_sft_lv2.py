# 금고 털이
import sys

w, n = map(int,sys.stdin.readline().split())
metal_list = []

for i in range(n):
  m, p = map(int,sys.stdin.readline().split())
  metal_list.append((m,p))

sorted_list = sorted(metal_list, key = lambda x: (-x[1]))
price = 0

for i in range(len(sorted_list)):
  if sorted_list[i][0] < w:
    price = price + sorted_list[i][0] * sorted_list[i][1] #140
    w -= sorted_list[i][0]
  elif sorted_list[i][0] >= w: #90
    price = price + w * sorted_list[i][1] # 1
    w -= w

print(price)