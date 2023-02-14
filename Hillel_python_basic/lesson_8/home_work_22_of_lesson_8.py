def find_unique_value(lst):
    for el in lst:
        count = lst.count(el)
        if count == 1:
            return el


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 0.5]) == 0.5, 'Test3'
print("ОК")
