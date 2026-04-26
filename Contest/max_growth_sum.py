n, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)

size_max_digit = len(str(numbers[0]))
temp_list = []
data = {}
result = 0

while True:
    while True:
        if not numbers or len(str(numbers[0])) < size_max_digit or len(str(numbers[0])) == 1:
            break
        num = str(numbers.pop(0))
        for i in range(len(num)):
            key = len(num) - 1 - i
            value = int(num[i])
            if value != 9:
                data.setdefault(key, []).append(value)

    if size_max_digit == 1:
        for num in numbers:
            if num != 9:
                data.setdefault(0, []).append(num)
        numbers = []

    temp_list = sorted(data.get(size_max_digit - 1, []))
    for num in temp_list:
        result += (9 - num) * 10 ** (size_max_digit - 1)
        k -= 1
        if k <= 0:
            break

    if k == 0 or (not numbers and size_max_digit == 1):
        break

    if k > 0:
        size_max_digit -= 1

print(result)


# Алгоритм кратко:
#
# Берем самые большие числа и делим их по разрядам, сохраняя в словать data. Если число равно 9, то не добавляем
# Выбираем получившийся списо максимального разряда, соритруем, и по очереди получаем разницу увеличения.
# Если после этого k>0, то повторяем процесс со следующим разрядом
