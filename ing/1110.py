# 2020.01.06
"""
acmicpc.net/problem/1110
문제집 : 백준에서 가장 많이 풀린 문제 TOP 100 (입문자 추천) - njw1204
문제: 0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때, 다음과 같은 연산을 할 수 있다. 먼저 주어진 수가 10보다
    작다면 앞에 0을 붙여 두자리 수로 만들고, 각 자리의 숫자를 더한다. 그 다음, 주어진 수의 가장 오른쪽 자리 수와
    앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.
    
    26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는
    42이다. 4+2 = 6이다. 새로운 수는 26이다.

    위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다. 

    N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.
입력: 첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수이다.
출력: 첫째 줄에 N의 사이클 길이를 출력한다. 

import sys
input = sys.stdin.readline

num = input().rstrip()
final = num
count = 0
#print(num, type(num))

while True:
    process = str(int(num[0]) + int(num[1]))
    num = num[-1] + process[-1]
    count += 1
    if(num == final):
        break
print(count)
#시간초과... 후;; 2초.. 

import sys
input = sys.stdin.readline

def findme(number):
    global count
    if number == N and count != 0:
        return count

    addn = str(int(number[0]) + int(number[-1]))
    number = number[-1] + addn[-1]
    count += 1
    return findme(number)


count = 0
N = str(input().rstrip())
print(findme(N))
"""
import sys
input = sys.stdin.readline

N = int(input())
count = 0 
number=N
while True:
    addn = str((N//10) + (N%10))
    number = addn[1] + str(addn[-1])

