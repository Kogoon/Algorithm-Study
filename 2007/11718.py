#
"""
그대로 출력. 
입력 -> 공백으로 받지 않고 공백으로 끝나지 않는다. 
"""
import sys
input = sys.stdin.readline

for i in range(100): #100줄을 넘기지 않는다. 
    s = input().strip()
    print(s)