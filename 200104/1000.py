# 2020.01.03
"""
acmicpc.net/problem/1000
문제집 A+B
문제: 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
입력: 첫째 줄에 A와 B가 주어진다. (0<A, B<10)
(1 2)
출력: 첫째 줄에 A+B를 출력한다.
(3)
"""
"""
#1
A, B = input().split()
print(int(A)+int(B))
"""
#2
A, B = map(int, input().split())
print(A+B)