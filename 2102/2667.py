# 21.02.23
"""
"""
import sys 
input = sys.stdin.readline 

N      = int(input())
graph  = []

cnt    = 0 
results = []

for _ in range(N):
  graph.append(list(map(int, input().rstrip())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
  global cnt
  graph[x][y] = 0
  cnt += 1
  for a in range(4):
    xx = x + dx[a]
    yy = y + dy[a]

    if xx<0 or yy<0 or xx>=N or yy>=N:
      continue

    if graph[xx][yy]:
      dfs(xx, yy)

for i in range(N):
  for j in range(N):
    if graph[i][j]:
      dfs(i, j)
      results.append(cnt)
      cnt = 0

print(len(results))
results.sort()
for result in results:
  print(result)
