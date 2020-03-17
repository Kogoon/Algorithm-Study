# 2020.03.18
"""
acmicpc.net/problem/14681
문제: 흔한 수학 문제 중 하나는 주어진 점이 어느 사분면에 속하는지 알아내는 것이다.
    예를 들어, 좌표가 (12, 5)인 점 A는 x좌표와 y좌표가 모두 양수이므로 제 1사분면에 속한다.
    ...(중냑)
    점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오.
    단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.
입력: 첫 줄에는 정수 x가 주어진다.
    다음 줄에는 정수 y가 주어진다.
출력: 점(x, y)의 사분면 번호(1, 2, 3, 4 중 하나)를 출력한다.
"""
import sys
input = sys.stdin.readline

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
elif x > 0 and y < 0:
    print("4")