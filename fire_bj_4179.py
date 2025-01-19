import sys
from collections import deque

def bfs():
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]

  while f_queue or j_queue:

    # 불먼저 번짐
    f_size = len(f_queue)
    for _ in range(f_size):
      cur_x, cur_y = f_queue.popleft()

      for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] == '.':
          f_queue.append((nx,ny))
          maze[nx][ny] = 'F'

    # 지훈 이동
    j_size = len(j_queue)
    for _ in range(j_size):
      cur_x,cur_y,time = j_queue.popleft()

      # 가장자리 도달 처리
      # cur_x, cur_y는 각각 행좌표 열좌표
      if cur_x == 0 or cur_x == r-1 or cur_y == 0 or cur_y == c-1:
        return time + 1
  
      for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        # 지훈이 이동
        if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and maze[nx][ny] == '.':
          j_queue.append((nx,ny,time+1))
          visited[nx][ny] = True

  return "IMPOSSIBLE"

r,c = map(int,sys.stdin.readline().split())

maze = []
j_queue = deque()
f_queue = deque()
visited = [[False] * c for _ in range(r)]

for i in range(r):
  row = list(sys.stdin.readline().strip())
  maze.append(row)

  for j in range(c):
    if maze[i][j] == 'J':
      j_queue.append((i,j,0))
      visited[i][j] = True
    
    elif maze[i][j] == 'F':
      f_queue.append((i,j))

print(bfs())