# 2020.01.06
"""
acmicpc.net/problem/1463
문제집 : 백준에서 가장 많이 풀린 문제 TOP 100 (입문자 추천) - njw1204
문제: 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
    1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
    2. X가 2로 나누어 떨어지면, 2로 나눈다.
    3. 1을 뺀다.
    정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
    연산을 사용하는 횟수의 최솟값을 출력하시오.
"""
X = int(input())
count = 0
while True:
    if(X==1):
        break
    
    if(X%3!=0 and X%2!=0):
        X = X - 1
        count = count + 1
    elif(X%3==0):
        X = X / 3
        count = count + 1
    elif(X%2==0):
        X = X / 2
        count = count + 1
print(count)

