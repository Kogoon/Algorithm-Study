# 2020.03.17
"""
문제: ...(중략)
                        내린 사람 수     탄 사람 수
    1번역(출발역)        0               32
    2번역                3               13
    3번역                28              25
    4번역(종착역)        39              0

    예를들어 위와 같은 경우를 살펴보자. 이 경우, 기차 안에 사람이 가장 많은 때는 2번역에서 
    3명의 사람이 기차에서 내리고, 13명의 사람이 기차에 탔을 때로, 총 42명의 사람이 기차안에 있따.
    이 기차는 다음 조건을 만족하면서 운행된다고 가정한다.

    1. 기차는 역 번호 순서대로 운행한다.
    2. 출발역에서 내린 사람 수와 종착역에서 찬 사람 수는 0이다.
    3. 각 역에서 현재 기차에 있는 사람보다 더 많은 사람이 내리는 경우는 없다.
    4. 기차의 정원은 최대 10,000명이고, 정원을 초과하여 타는 경우는 없다. 

    4개의 역에 대해 기차에서 내린 사람 수와 탄 사람 수가 주어졌을 때, 기차에 사람이 가장 많을 때의
    사람 수를 계산하는 프로그램을 작성하시오. 
입력: 각 역에서 내린 사람 수와 탄 사람 수가 빈칸을 사이에 두고 첫째 줄부터 넷째 줄까지 역 순서대로 한 줄에 하나씩 주어진다.
출력: 첫째 줄에 최대 사람 수를 출력한다. 
"""
Fst_Station = list(map(int, input().split()))
Snd_Station = list(map(int, input().split()))
Trd_Station = list(map(int, input().split()))
Fth_Station = list(map(int, input().split()))

a = Fst_Station[1] + Snd_Station[1] - Fst_Station[0] - Snd_Station[0]
b = a + Trd_Station[1] - Trd_Station[0]
c = b + Fth_Station[1] - Fth_Station[0]

result = [a, b, c]
result.sort()
print(result[2])