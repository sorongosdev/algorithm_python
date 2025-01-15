# B의 제일 큰 수를 A의 제일 작은 수랑 곱해야함.

import sys

n = int(sys.stdin.readline())

a = map(int,sys.stdin.readline().split())
b = map(int,sys.stdin.readline().split())

# a는 정렬, b는 비파괴 정렬
a_sorted = sorted(a, reverse=False)
b_sorted = sorted(b, reverse=True)

total_sum = 0

for i in range(0,n):
  total_sum += a_sorted[i] * b_sorted[i]

print(total_sum)