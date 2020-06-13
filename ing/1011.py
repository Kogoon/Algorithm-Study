#
"""
"""
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    count = 2
    x, y = map(int, input().split())
    y2 = y - 1
    x2 = x + 1
    while True:
        if y2 - x2 == 0:
            break
        elif y2 - x2 >= 2:
            x2 += 2
            count += 1
        else:
            x2 += 1
            count += 1
    print(count)