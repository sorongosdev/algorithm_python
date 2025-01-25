import sys
sys.setrecursionlimit(10**5) # 노드 제약 조건 
input = sys.stdin.readline

# n 정점
n,m = map(int,input().split())
adj = [[] for _ in range(n+1)] # 한 칸 낭비하더라도 인덱스 편의를 위해 n+1로 지정
adj_reverse = [[] for i in range(n+1)] # adj가 거꾸로 된 이차원 배열. 들어오는 거라고 생각하자.

for _ in range(m):
  x,y = map(int, input().split())
  adj[x].append(y)
  adj_reverse[y].append(x)
s,t = map(int,input().split())

def dfs(now, adj, visited):
  if visited[now]:
    return
  visited[now] = True
  for neighbor in adj[now]:
    dfs(neighbor, adj, visited)
  return

fromS = [0] * (n+1)
fromS[t] = 1 # 미리 방문 처리해서 도착하면 순회 끝내도록
dfs(s,adj,fromS) # 일반

fromT = [0] * (n+1)
fromT[s] = 1
dfs(t,adj,fromT) # T에서 시작

toS = [0] * (n+1) # 돌아올 수 있는가 체크
dfs(s,adj_reverse,toS)

toT = [0] * (n+1)
dfs(t,adj_reverse,toT)

count = 0
for i in range(1,n+1):
  if fromS[i] and fromT[i] and toS[i] and toT[i]:
    count += 1

print(count-2)