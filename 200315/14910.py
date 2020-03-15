# 2020.03.15
"""
문제: 주어진 N개의 정수가 비내림차순으로 나열되어 있는지 판정하는 프로그램을 작성하시오.
    N개의 수 A1, A2, ..., AN이 A1 <= A2 <= ... <= AN을 만족하는 것을 비내림차순이라고 한다.
입력: 첫째 줄에 공백으로 구분된 N(1 <= N <= 1,000,000)개의 정수가 주어진다.
    입력으로 주어지는 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
출력: 비내림차순으로 나열되어 있으면 Good을 출력하고, 그렇지 않으면 Bad를 출력한다.
"""
"""
Try.1 
import sys

numbers = list(map(int, input().split()))

for i in range(len(numbers)):
    if numbers[i] == numbers[-1]:
        print("Good")
        sys.exit()
        
    if numbers[i] <= numbers[i+1]:
        continue
    else:
        print("Bad")
        sys.exit()

# 마지막 예제 입력 1, 2, 3, 2, 1 쪽에서 첫 번째 1과 마지막 1이 같아서 Good 으로 오류남. 
"""
import sys

numbers = list(map(int, input().split()))

for i in range(len(numbers)):
    if i == len(numbers) - 1:
        if numbers[i] == numbers[i-1]:
            print("Good")
            sys.exit()
    else:
        if numbers[i] <= numbers[i+1]:
            continue
        else: 
            print("Bad")
            sys.exit()
    