# 2020.03.19
"""
acmicpc.net/problem/5565
문제: 책 10권의 총 가격과 가격을 읽을 수 있는 9권 가격이 주어졌을 때, 가격을 읽을 수 없는 책의 가격을 구하는 프로그램을 작성하시오.
입력: 첫째 줄에 10권의 총 가격이 주어진다.
    둘째 줄부터 9개 줄에는 가격을 읽을 수 있는 책 9권의 가격이 주어진다.
    책의 가격은 10,000원 이하이다. 
출력: 첫째 줄에 가격을 읽을 수 없는 책의 가격을 출력한다. 
"""
import sys
input = sys.stdin.readline

Total_price = int(input())

for i in range(9):
    book = int(input())
    Total_price -= book

print(Total_price)