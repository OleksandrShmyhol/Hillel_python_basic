# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
# [1, 2, 3] => [[1, 2], [3]]
# [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
# [1] => [[1], []]
# [] => [[], []]

lst = [1, 2, 3, 4, 5]
first_list = []
second_list = []
if not len(lst):
    print([first_list, second_list])
elif not len(lst) % 2:
    first_list = lst[:int(len(lst) / 2)]
    second_list = lst[int(len(lst) / 2):]
    print([first_list, second_list])
elif len(lst) > 1:
    first_list = lst[:int(len(lst) / 2) + 1]
    second_list = lst[int(len(lst) / 2) + 1:]
    print([first_list, second_list])
else:
    first_list += lst
    print([first_list, second_list])
