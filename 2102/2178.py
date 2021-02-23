# 21.02.23
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m  = map(int, input().split())
graph = [[0]*m for _ in range(n)]
cnt   = 0

for a in range(n):
  graph[a] = list(map(int, input().rstrip()))

visited = [[False]*m for _ in range(n)]

def bfs(x, y):
  global cnt 
  queue = deque([(x, y)])

  while queue:
    p, q = queue.popleft()
    visited[p][q] == True
    cnt = graph[p][q]

    for b in range(4):

      xx = p + dx[b]
      yy = q + dy[b]

      if xx<0 or yy<0 or xx>=n or yy>=m:
        continue 

      if visited[xx][yy]:
        continue

      if graph[xx][yy] and not visited[xx][yy]:
        queue.append((xx, yy))
        visited[xx][yy] = True
        graph[xx][yy] += cnt

bfs(0, 0)
print(graph[n-1][m-1])
