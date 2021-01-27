import sys
input = sys.stdin.readline

data = list(map(int, input().rstrip()))
len_data = len(data) // 2

sum_l = 0
sum_r = 0

for i in range(len(data)):
  if i < len_data:
    #print("a", data[i])
    sum_l += data[i]
  elif len_data <= i:
    #print("b", data[i])
    sum_r += data[i]

if sum_l == sum_r:
  print("LUCKY")
else:
  print("READY")
