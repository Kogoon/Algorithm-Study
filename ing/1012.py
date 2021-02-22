import sys
input = sys.stdin.readline

t = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
  graph[x][y] = 0
  
  for k in range(4):
    xx = x + dx[k]
    yy = y + dy[k]

    if xx<0 or yy<0 or xx>=n or yy>=m:
      continue

    if graph[xx][yy]:
      dfs(xx, yy)

for _ in range(t):
  cnt = 0
  m, n, cab = map(int, input().split())
  graph = [[0]*m for i in range(n)]

  for c in range(cab):
    a, b = map(int, input().split())
    graph[b][a] = 1

  for i in range(n):
    for j in range(m):
      if graph[i][j]:
        dfs(i, j)
        cnt += 1

  print(cnt)
