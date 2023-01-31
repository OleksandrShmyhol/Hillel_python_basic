# [12, 3, 4, 10] => [10, 12, 3, 4]
# [1] => [1]
# [] => []
# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]

lst = [12, 3, 4, 10, 8]

if len(lst) < 2:
    print(lst)
else:
    last_element = lst.pop()
    lst.insert(0, last_element)
    print(lst)
