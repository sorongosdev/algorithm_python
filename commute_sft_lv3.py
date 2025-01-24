import sys
from collections import deque, defaultdict

def dfs(vertex, end, path_list):
  path_list.append(vertex)

  if vertex == end: return

  visited[vertex] = True

  for i in sorted(graph[vertex]):
    if i not in visited:
      dfs(i,end,path_list)

# n 정점 m 간선
n,m = map(int,sys.stdin.readline().split())
graph = defaultdict(list)
visited = defaultdict(list)

go_list = []
back_list = []

for _ in range(m):
  a, b = map(int,sys.stdin.readline().split())
  graph[a].append(b)

s, t = map(int,sys.stdin.readline().split())

dfs(s,t,go_list)
# print(go_list)
visited.clear()
dfs(t,s,back_list)
# print(back_list)

common_list = list(set(go_list) & set(back_list))

print(len(common_list)-2)