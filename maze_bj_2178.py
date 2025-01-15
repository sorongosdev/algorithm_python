import sys
from collections import deque

def bfs(n,m,maze):
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]

  distance = [[-1] * m for _ in range(n)]
  distance[0][0] = 1

  queue = deque([(0,0)])

  while(queue):
    cur_x, cur_y = queue.popleft()

    for i in range(4):

      nx = cur_x + dx[i]
      ny = cur_y + dy[i]

      if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1 and maze[nx][ny] == 1:
        queue.append((nx,ny))
        # 너 나보다 거리 하나 더 큼
        distance[nx][ny] = distance[cur_x][cur_y] + 1

  return distance[n-1][m-1]

# n행, m열
n, m = map(int,sys.stdin.readline().split())
maze = []
for _ in range(n):
  maze.append(list(map(int,sys.stdin.readline().strip())))

print(bfs(n,m,maze))