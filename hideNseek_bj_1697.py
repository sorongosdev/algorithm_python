import sys
from collections import deque 

def bfs(n,k):
  dx = [0,-1,1]
  da = [2,1,1]

  # 방문 위치, 방문 시간을 함께 큐에 넣음.
  queue = deque([(n,0)])
  visited = {n: False}

  while(queue):
    cur_x,cur_time = queue.popleft()

    # 현재 위치가 동생 위치면 반환
    if(cur_x == k): return cur_time

    for i in range(3):
      nx = da[i] * cur_x + dx[i]

      if 0 <= nx < 100001 and not nx in visited:
        queue.append((nx, cur_time + 1))
        visited[nx] = True

  return -1

n,k = map(int,sys.stdin.readline().split())
print(bfs(n,k))