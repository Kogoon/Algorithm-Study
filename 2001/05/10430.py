# 2020.01.05
"""
acmicpc.net/problem/10430
문제집 : 백준에서 가장 많이 풀린 문제 TOP 100 (입문자 추천) - njw1204
문제: (A+B)%C는 (A%C) + (B%C)%C와 같을까?
      (AxB)%C는 (A%C) x (B%C)%C와 같을까?
      세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오
입력: 첫째 줄에 A, B, C가 순서대로 주어진다.(2<=A, B, C<=10000)
출력: 첫째 줄에 (A+B)%C, 둘째 줄에 (A%C + B%C)%C,
      셋째 줄에 (AxB)%C, 넷째 줄에 (A%C x B%C)%C 를 출력한다.
"""
A, B, C = map(int, input().split())
print((A+B)%C)
print((A%C+B%C)%C)
print((A*B)%C)
print((A%C*B%C)%C)
