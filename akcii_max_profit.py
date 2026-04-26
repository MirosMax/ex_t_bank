n = int(input())
prices = list(map(int, input().split()))

if n < 2:
    print(0)
    exit()

# макс прибыль от одной сделки на отрезке 0, i
left = [0] * n
min_price = prices[0]

for i in range(1, n):
    left[i] = max(left[i-1], prices[i] - min_price)
    min_price = min(min_price, prices[i])

# макс прибыль от одной сделки на отрезке i, n-1
right = [0] * n
max_price = prices[-1]

for i in range(n-2, -1, -1):
    right[i] = max(right[i+1], max_price - prices[i])
    max_price = max(max_price, prices[i])

# макс сумма двух непересекающихся сделок
max_profit = 0
for i in range(n):
    max_profit = max(max_profit, left[i] + right[i])

print(max_profit)
