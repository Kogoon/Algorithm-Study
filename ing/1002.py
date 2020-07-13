# 2020.07.13
"""
acmicpc.net/problem/1002
문제: 이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다.
조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.
죠규현의 좌표(x1, y1)와 백승환의 좌표(x2, y2)가 주어지고, 조규현이 계산한 류재명과의 거리 r1과
백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 류재명이 있을 수 있는 좌표의 수를 출력하는 
프로그램을 작성하시오
입력: 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 이루어져 있다. 
한줄에 x1, y1, r1, x2, y2, r2가 주어진다. x1, y1, x2, y2는 -10,000보다 크거나 같고,
10,000보다 작거나 같은 정수이고, r1, r2는 10,000보다 작거나 같은 자연수 이다. 
(
    3
    0 0 13 40 0 37
    0 0 3 0 7 4
    1 1 1 1 1 5
)
출력: 각 테스트 케이스 마다 류재명이 있을 수 있는 위치의 수를 출력한다. 만약 류재명이 있을 수 있는
위치의 개수가 무한대일 경우에는 -1을 출력한다. 
"""
# 두 원 사이의 관계
# 두 점 r2 - r1 < d < r1 + r2
# 한 점 r2 + r1 = d, r2 - r1 = d
# 0 만나지 않을때
# 동심원일때 -1
"""
import math
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x2-x1 == 0 and y2-y1 == 0:
        if r2-r1 == 0:
            print("-1")
            continue
        else:
            print("0")
            continue
    else:
        y = (y2-y1)*(y2-y1)
        x = (x2-x1)*(x2-x1)
        d = math.sqrt(x+y)
        r = math.sqrt((r2-r1)*(r2-r1))
        
        if r1+r2 == d or r ==d:
            print("1")
        elif r2-r1 < d < r2+r1:
            print("2")
        else:
            print("0")
"""
#sqrt 사용안하고 
import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x2-x1 == 0 and y2-y1 == 0:
        if r2-r1 == 0:
            print("-1")
        else:
            print("0")
    else:
        d = ((x2 - x1)**2) + ((y2-y1)**2) 
        r_s = (r2 + r1)**2
        r_d = (r2 - r1)**2
      
        if r_s == d or r_d == d:
            print("1")
        elif r_d < d < r_s:
            print("2")
        else:
            print("0")
