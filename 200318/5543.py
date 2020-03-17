# 2020.03.18
"""
acmicpc.net/problem/5543
문제: 햄버거는 총 3종류 상덕버거, 중덕버거, 하덕버거가 있고, 음료는 콜라와 사이다 두 종류가 있다.
    햄버거와 음료의 가격이 주어졌을 때, 가장 싼 세트 메뉴의 가격을 출력하는 프로그램을 작성하시오.
입력: 입력은 총 다섯 줄이다. 첫째 줄에는 상덕버거, 둘째 줄에는 중덕버거, 셋째 줄에는 하덕버거의 가격이 주어진다.
    넷째 줄에는 콜라의 가격, 다섯째 줄에는 사이다 가격이 주어진다. 
    모든 가격은 100원 이상, 20000원 이하이다.
출력: 첫째 줄에 가장 싼 세트 메뉴의 가격을 출력한다.
"""
import sys
input = sys.stdin.readline

sang = int(input())
jung = int(input())
ha = int(input())
cola = int(input())
cider = int(input())

burger = [sang, jung, ha]
drink = [cola, cider]
prices = []

for i in burger:
    for j in drink:
        price = i + j - 50
        prices.append(price)

prices.sort()
print(prices[0])
