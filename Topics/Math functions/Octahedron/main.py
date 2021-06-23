import math
a = int(input())

s = round(2 * a ** 2 * math.sqrt(3), 2)
v = round(a ** 3 * math.sqrt(2) * (1 / 3), 2)

print(f'{s} {v}')
