# 200616
"""
"""
import sys
input = sys.stdin.readline

words = list(input().rstrip())
cutting = ''

for _ in range(len(words)):

    if len(cutting) == 10:
        print(cutting)
        cutting = ''
    cutting += words.pop(0)

print(cutting)
