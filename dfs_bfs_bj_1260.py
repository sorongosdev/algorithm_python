import sys
from collections import deque, defaultdict

def dfs(v):
  visited[v] = True
  dfs_result.append(v)

  for i in sorted(graph[v]): # 겹치는 것 제거하고 정렬
    if i not in visited:
      dfs(i)

def bfs():
  visited = {} # dfs에서 썼으니 비워줌
  queue = deque([v])
  visited[v] = True

  while queue:
    cur_v = queue.popleft()
    bfs_result.append(cur_v)

    for i in sorted(graph[cur_v]):
      if i not in visited:
        queue.append(i)
        visited[i] = True

n,m,v = map(int,sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(m):
  a, b = map(int,sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

# 정점 번호가 1부터 시작해서 n+1개 만들어줌.
visited = {}
dfs_result = []
bfs_result = []
dfs(v)
bfs()
print(' '.join(map(str,dfs_result)))
print(' '.join(map(str,bfs_result)))