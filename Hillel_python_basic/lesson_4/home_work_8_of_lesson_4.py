# [0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88

# [1, 3, 5] => 30
# [6] => 36
# [] => 0

lst = [0, 1, 7, 2, 4, 8]

result = 0
i = 0
while i < len(lst):
    if not i % 2:
        result += lst[i] * lst[len(lst) - 1]
    i += 1

print(result)
