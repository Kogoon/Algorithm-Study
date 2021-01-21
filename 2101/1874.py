import sys 
input = sys.stdin.readline

n = int(input())
ans = [0]
stk = []
pm  = []
i = j = 1

for _ in range(n):
  a = int(input())
  ans.append(a)

while j<=n:
  if stk and stk[-1] == ans[i]:
    stk.pop()
    pm.append('-')
    i+=1
  else:
    stk.append(j)
    pm.append('+')
    j+=1

while stk:
  if stk[-1] == ans[i]:
    stk.pop()
    pm.append('-')
    i+=1
  else:
    break

if not stk:
  while pm:
    a = pm.pop(0)
    print(a, end=' ')
else:
  print('NO')
