# 2020.01.05
"""
acmicpc.net/problem/8393
문제집 : 백준에서 가장 많이 풀린 문제 TOP 100 (입문자 추천) - njw1204
문제: n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오
입력: 첫째 줄에 n(1 <= n <= 10,000)이 주어진다.
출력: 1부터 n까지의 합을 출력한다.
"""
num = int(input())
sum = 0
for i in range(1, num+1):
    sum = sum + i
print(sum)