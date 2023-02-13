def second_index (string = str(), element = str()):
    if not string.rfind(element):
        return None
    return string.rfind(element)


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hellolo", "lo") == 10, 'Test4'
print('ОК')
