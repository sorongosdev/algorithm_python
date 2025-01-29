import sys
from collections import deque
sys.setrecursionlimit(10**6) # 노드 제약 조건 

x = int(sys.stdin.readline())
queue = deque([(x,0)])

def bfs():
  visited = []

  while queue:

    cur_x, count = queue.popleft()

    if cur_x == 1:
      return count

    if cur_x % 3 == 0 and cur_x // 3 not in visited:
      visited.append(cur_x//3)
      queue.append((cur_x//3, count+1))
    if cur_x % 2 == 0 and cur_x // 2 not in visited:
      visited.append(cur_x//2)
      queue.append((cur_x//2, count+1))
    if cur_x - 1 not in visited:
      visited.append(cur_x-1)
      queue.append((cur_x-1,count+1))

  return count

print(bfs())