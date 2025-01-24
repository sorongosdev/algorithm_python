import sys
from collections import defaultdict, deque

def dfs(v):
  global wormed_cnt
  visited[v] = True
  wormed_cnt += 1

  for i in sorted(graph[v]):
    if i not in visited:
      dfs(i)

computer_num = int(sys.stdin.readline())
connection_num = int(sys.stdin.readline())

graph = defaultdict(list)
visited = defaultdict(list)
wormed_cnt = -1

for _ in range(connection_num):
  a,b = map(int,sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

dfs(1)

print(wormed_cnt)