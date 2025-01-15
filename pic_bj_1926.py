import sys
from collections import deque

def bfs(x,y,visited,paper):
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]

  queue = deque([(x,y)]) # 탐색 예정인 큐
  visited[x][y] = True
  size = 1

  while(queue):
    cur_x, cur_y = queue.popleft() # 맨 처음 값 뽑아냄

    # 4방향 탐색
    for i in range(4):
      # 지금 탐색하려는 곳 nx, ny
      nx = cur_x + dx[i]
      ny = cur_y + dy[i]

      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and paper[nx][ny] == 1:
        queue.append((nx,ny))
        visited[nx][ny] = True
        size += 1

  return size

# n: 행, m: 열
n, m = map(int,sys.stdin.readline().split())
paper = [] # 그림 전체 2차원 배열
for _ in range(n):
  paper.append(list(map(int,sys.stdin.readline().split())))
visited = [[False] * m for _ in range(n)] # 방문여부 리스트

pic_count = 0 # 그림 개수
max_size = 0 # 최대 크기

for i in range(n): # 행
  for j in range(m): # 열
    # 처음 방문한 것만 그림으로 셈
    if not visited[i][j] and paper[i][j] == 1:
      pic_count += 1
      max_size = max(max_size,bfs(i,j,visited,paper))

print(pic_count)
print(max_size)