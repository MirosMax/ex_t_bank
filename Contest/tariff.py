cost_tariff, size_tariff, cost_mb_extra, traffic = map(int, input().split())

bill = 0

if traffic <= size_tariff:
    bill = cost_tariff
else:
    bill = cost_tariff + (traffic - size_tariff) * cost_mb_extra

print(bill)