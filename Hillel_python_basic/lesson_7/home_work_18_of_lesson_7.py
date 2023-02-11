def second_index(word, symbol):
    if word.rfind(symbol):
        result = word.index(symbol) + word[word.index(symbol) + 1: len(word)].index(symbol) + 1
    else:
        result = None
    return result


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
