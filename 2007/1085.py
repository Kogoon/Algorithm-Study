# 2020.07.10
"""
이거보다 더 좋은 방법이 있을 거 같은데... 
"""
"""
import sys
input = sys.stdin.readline 

x, y, w, h = map(int, input().split())
xresult = w-x 
if xresult > x:
    xresult = x
yresult = h-y
if yresult > y:
    yresult = y

if xresult > yresult:
    print(yresult)
else:
    print(xresult)
"""
#더 쉬운 방법...
x, y, w, h = map(int, input().split())
print(min([x, y, w-x, h-y]))
