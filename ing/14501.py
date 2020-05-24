def find_min_profit(N, day, profit):

    min_profit = 0
    day_num = 0

    for _ in range(N):
        if day_num+day[day_num] > N:
            return min_profit
        min_profit += profit[day_num]
        day_num += day[day_num]

    return min_profit

"""
def find_max_profit(N, day, profit):
    
    min_profit = find_min_profit(N, day, profit)
    day_num = 0
    max_profit = 0

    for _ in range(N):
        if day_num+day[day_num] > N:
            return min_profit
        if profit[day_num] < profit[day_num+1]:
            """

N = int(input())

day = []
profit = []

for _ in range(N):
    a, b = map(int, input().split())
    day.append(a)
    profit.append(b)

print(find_min_profit(N, day, profit))
