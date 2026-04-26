n, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)

size_max_digit = len(str(numbers[0]))
temp_list = []
result = 0

while True:
    while True:
        if len(str(numbers[0])) < size_max_digit or len(str(numbers[0])) == 1:
            break
        num = numbers.pop(0)
        f_digit = num // 10 ** (size_max_digit - 1)
        tail_num = num % 10 ** (size_max_digit - 1)
        if f_digit != 9:
            temp_list.append(f_digit)
        numbers.append(tail_num)

    if size_max_digit == 1:
        for num in numbers:
            if num != 9:
                temp_list.append(n)
        numbers = []

    temp_list.sort()
    for num in temp_list:
        result += (9 - num) * 10 ** (size_max_digit - 1)
        k -= 1
        if k <= 0:
            break

    if k == 0 or not numbers:
        break

    if k > 0:
        numbers.sort(reverse=True)
        size_max_digit = len(str(numbers[0]))
        temp_list = []

print(result)
