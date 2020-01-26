# 2020.01.26
"""
acmicpc.net/problem/11720
문제집 : 백준에서 가장 많이 풀린 문제 TOP 100 (입문자 추천) - njw1204
문제: N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
입력: 첫째 줄에 숫자의 개수 N(1 <= N <= 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
출력: 입력으로 주어진 숫자 N개의 합을 출력한다. 
"""
N = int(input())
list_n = list(map(int, input()))
sum = 0 # 숫자를 더해 저장할 변수 
for i in range(N): 
    sum = sum + list_n[i]
print(sum)
