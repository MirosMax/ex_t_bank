def func(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    if n % 2:
        return 1 + func(n // 2 + 1)
    else:
        return 1 + func(n // 2)


print(func(int(input())))
