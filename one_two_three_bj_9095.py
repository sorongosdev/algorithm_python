import sys
input = sys.stdin.readline

t = int(input())
input_list = [0] * 11
input_list[1] = 1
input_list[2] = 2
input_list[3] = 4

for j in range(4,11):
  input_list[j] = input_list[j-1] + input_list[j-2] + input_list[j-3]

for _ in range(t):
  n = int(input())
  print(input_list[n])