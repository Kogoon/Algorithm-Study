# 2020.03.19
"""
문제: 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
    즉, 첫번째 문자를 R번 반복하고, 두번째 문자를 R번 반복하는 식으로 P를 만들면된다. 
입력: 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 반복 횟수 R, 문자열 S가 공백으로 구분되어 주어진다.
    S의 길이는 적어도 1이며, 20글자를 넘지 않는다.
출력: 각 테스트 케이스에 대해 P를 출력한다.
"""
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    R, S = input().split()
    S = list(S)
    for j in S:
        print(int(R) * j, end=(""))

    print()