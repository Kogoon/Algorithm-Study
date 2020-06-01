"""
문제: 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다. 
    동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때, 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
입력: 첫째줄에 N과 K가 주어진다.
    둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다.
출력: 첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.
"""
import sys 
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
count = 0
for _ in range(N):
    coin = int(input())
    if coin > K:
        continue
    coins.append(coin)

a = len(coins) - 1
while True:
    if K == 0:
        break
    b = K // coins[a]
    if b > 0:
        K -= (coins[a] * b)
        count += b
    else:
        a -= 1

print(count)