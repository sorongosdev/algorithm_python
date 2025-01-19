import sys
from collections import deque

def bfs():

  dx = [-1,1,0,0]
  dy = [0,0,-1,1]


  while(queue):
    # 모두 다 익은 토마토이면 리턴

    cur_x, cur_y, day = queue.popleft()

    for k in range(4):

      nx = cur_x + dx[k]
      ny = cur_y + dy[k]

      if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
        box[nx][ny] = 1
        queue.append((nx,ny,day+1))

  for i in range(n):
    for j in range(m):
      if box[i][j] == 0:
        return -1

  return day

m,n = map(int,sys.stdin.readline().split())
box = []
queue = deque()

all_ripen = True

# 리스트 입력
for i in range(n):
  row = list(map(int,sys.stdin.readline().split()))
  box.append(row)
  for j in range(m):
    if row[j] == 0:
      all_ripen = False
    elif row[j] == 1:
      queue.append((i,j,0))

if all_ripen:
  print(0)
else:
  print(bfs())