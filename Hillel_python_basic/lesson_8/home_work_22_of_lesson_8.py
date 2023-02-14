def find_unique_value(lst):
    num = 0
    for el in lst:
        count = 0
        for i in lst:
            if i == el:
                count += 1
            if count > 1:
                count = 0
                break
        if count == 1:
            num = el
            break
    return num


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 0.5]) == 0.5, 'Test3'
print("ОК")
