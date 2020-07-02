#
"""
입력: 세점
출력: 마지막 한점
"""
import sys
input = sys.stdin.readline
"""
def swap(list):
    if list[0] > list[1]:
        temp = list[0]
        list[0] = list[1]
        list[1] = temp
    return list

for i in range(3):
    a, b = map(int, input().split())
    if a not in x:
        x.append(a)
    if b not in y:
        y.append(b)
#print(x, y)

swap(x)
swap(y)

#print(x, y)
"""
x = []
y = []

for i in range(3):
    a, b = map(int, input().split())
    if a > 1000 or b > 1000:
        sys.exit()
    x.append(a)
    y.append(b)
temp = [0] * (2)
temp[0] = x[0]
if temp[0] == x[1]:
    temp[0] = x[2]
if temp[0] == x[2]:
    temp[0] = x[1]
temp[1] = y[0]
if temp[1] == y[1]:
    temp[1] = y[2]
if temp[1] == y[2]:
    temp[1] = y[1]

print("{} {}".format(temp[0], temp[1]))