import random
# [1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
# [1, 1, 1, 1] == [1, 1, 1]
# [6, 3, 7] == [6, 7, 3]

lst = []
lst_result = []

for i in range(random.randint(3, 10)):
    lst.append(random.randint(1, 100))

print(lst)

lst_result.append(lst[0])
lst_result.append(lst[2])
lst_result.append(lst[len(lst) - 2])

print(lst_result)
