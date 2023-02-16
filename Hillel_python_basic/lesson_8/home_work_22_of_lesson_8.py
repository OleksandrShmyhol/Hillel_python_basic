def find_unique_value(lst):
    print(el * lst.count(el) == 1 for el in lst)
    return list(el * lst.count(el) == 1 for el in lst)[0]


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 0.5]) == 0.5, 'Test3'
print("ОК")
