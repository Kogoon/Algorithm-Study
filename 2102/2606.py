# 21.02.22
# bfs 풀이. 
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for N in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

queue = deque([1])
visited[1] = True
while queue:
  x = queue.popleft()
  for i in graph[x]:
    if not visited[i]:
      queue.append(i)
      cnt += 1
      visited[i] = True

print(cnt)

