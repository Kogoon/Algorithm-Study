# 2020.03.18
"""
acmicpc.net/problem/2588
문제: ... 중냑
    3, 4, 5, 6위치에 들어갈 값을 구하는 프로그램을 작성하시오.
입력: 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.
출력: 첫째 줄부터 넷째 줄까지 차례대로 3, 4, 5, 6에 들어갈 값을 출력한다.
"""
import sys
input = sys.stdin.readline

number1 = int(input())
number2 = list(input().rstrip())

for i in range(2, -1, -1):
    print(number1 * int(number2[i]))

print(number1 * int(number2[0]+number2[1]+number2[2]))