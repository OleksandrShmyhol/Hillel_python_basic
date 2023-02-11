# [0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88

# [1, 3, 5] => 30
# [6] => 36
# [] => 0

lst = [0]
result = 0
if len(lst):
    for el in range(len(lst)):
        if not el % 2:
            result += lst[el]
    print(result * lst[-1])
else:
    print(0)
