# 2020.03.20
"""
문제: 그릇을 바닥에 놓았을 때, 그 높이는 10cm 이다. 그렇데 두 개의 그릇을 같은 방향으로 포개면 그 높이는 5cm만 증가한다. ...(중략)
입력: 첫 줄에는 괄호문자로만 이루어진 문자열이 주어진다. 입력 문자열에서 열린 괄호 '('는 바로 놓인 그릇, 닫힌 그릇')'은 거꾸로 놓인 그릇을 나타낸다.
    문자열의 길이는 3이상 50이하이다.
출력: 여러분은 그릇 방향이 괄호 문자로 표시된 문자열을 읽어서 그 최종의 높이를 정수로 출력해야한다. 
"""
import sys
input = sys.stdin.readline

s = list(input().rstrip())
height = 0
if s[0] == '(' or s[0] == ')':
    height += 10
for i in range(1, len(s)):
    if s[i-1] == '(':
        if s[i] == '(':
            height += 5
        else:
            height += 10

    else:
        if s[i] == ')':
            height += 5
        else:
            height += 10
print(height)
