import sys

n,k = map(int,sys.stdin.readline().split())

score_list = list(map(float,sys.stdin.readline().split()))
result_list = []

for i in range(k):
  start, end = map(int,sys.stdin.readline().split())
  score_sum = sum(score_list[start-1:end])
  score_average = round(score_sum / (end-start+1.00), 2)
  result_list.append(score_average)

for j in result_list:
  print(f"{j:.2f}")