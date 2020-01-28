# 2020.01.29
# 수학
"""
acmicpc.net/problem/1676
문제: N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
입력: 첫째 줄에 N이 주어진다. (0<=N<=500)
출력: 첫째 줄에 구한 0의 개수를 출력한다. 
"""
# 팩토리얼 0의 개수

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)
N = int(input())
num = list(str(fact(N)))
#print(num)
count = 0
num.reverse()
#print(num)
for x in range(len(num)):
    if num[x] != '0':
        break
    if num[x] == '0':
        count += 1
        

print(count)