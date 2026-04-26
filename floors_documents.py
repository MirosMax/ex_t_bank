n, t = map(int, input().split())
floors = list(map(int, input().split()))
n_employ = int(input())

time_sum = 0
start = 0
is_middle = False
result = 0

# Определяем старт
if (floors[n_employ - 1] - floors[0]) > t and (floors[-1] - floors[n_employ - 1]) > t:
    start = n_employ - 1
    is_middle = True

# Если мы между 1 и последним, то + минимальное расстояние
if is_middle:
    result += min((floors[start] - floors[0]), (floors[-1] - floors[start]))

result += floors[-1] - floors[0]

print(result)
