# 2020.03.20
"""
카카오 코드 페스티벌 2018 예선
문제: 제이지는 자신이 코드 페스티벌에 출전하여 받을 수 있을 상금이 얼마인지 궁금해졌다. 그는 자신이 두 번의 코드 페스티벌 본선 대회에서 얻을 수 있을 총 상금이 얼마인지 알아보기 위해, 상상력을 발휘하여 아래와 같은 가정을 하였다.
    제1회 코드 페스티벌 본선에 진출하여 a등(1 ≤ a ≤ 100)등을 하였다. 단, 진출하지 못했다면 a = 0으로 둔다.
    제2회 코드 페스티벌 본선에 진출하여 b등(1 ≤ b ≤ 64)등을 할 것이다. 단, 진출하지 못했다면 b = 0으로 둔다.
    제이지는 이러한 가정에 따라, 자신이 받을 수 있는 총 상금이 얼마인지를 알고 싶어한다.
입력: 첫 번째 줄에 제이지가 상상력을 발휘하여 가정한 횟수 T가 주어진다.
    다음 T개 줄에는 한 줄에 하나씩 제이지가 해본 가정에 대한 정보가 주어진다. 각 줄에는 두 개의 음이 아닌 정수 a가 공백 하나를 사이에 두고 주어진다.
출력: 각 가정이 성립할 때 제이지가 받을 상금을 원 단위의 정수로 한 줄에 하나씩 출력한다. 입력이 들어오는 순서대로 출력해야 한다.
"""
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    money = 0
    if a == 1:
        money += 5000000
    elif 1 < a <= 3:
        money += 3000000
    elif 3 < a <= 6:
        money += 2000000
    elif 6 < a <= 10:
        money += 500000
    elif 10 < a <= 15:
        money += 300000
    elif 15 < a <= 21:
        money += 100000
    else: 
        money += 0

    if b == 1:
        money += 5120000
    elif 1 < b <= 3:
        money += 2560000
    elif 3 < b <= 7:
        money += 1280000
    elif 7 < b <= 15:
        money += 640000
    elif 15 < b <= 31:
        money += 320000
    else: 
        money += 0

    print(money)