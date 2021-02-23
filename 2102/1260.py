# 21.02.22
"""
import sys
input = sys.stdin.readline

N, M, root = map(int, input().split())
check = [0] * (N+1)
maps = [[0] * (N+1) for i in range(N+1)]
for m in range(M):
  a, b = map(int, input().split())
  maps[a][b] = 1
  maps[b][a] = 1

def dfs():
  pass

def bfs():
  pass

print(dfs(*root))
"""
from collections import deque
import sys
input = sys.stdin.readline

N, M, start = map(int, input().split())
graph = [[] for n in range(N+1)]
graph_bfs = [[] for n in range(N+1)]
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)
#queue = deque(start)

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  #graph_bfs[a].append(b)

for y in range(1, N+1):
  graph[y].sort()
  #print(graph[a])

def dfs(v):
  visited_dfs[v] = True
  print(v, end=' ')
  for i in graph[v]:
    if not visited_dfs[i]:
      dfs(i) 

def bfs(v):
  queue = deque([v])
  visited_bfs[v] = True
  while queue:
    x = queue.popleft()
    print(x, end=' ')
    for j in graph[x]:
      if not visited_bfs[j]:
        queue.append(j)
        visited_bfs[j] = True

dfs(start)
print()
bfs(start)

