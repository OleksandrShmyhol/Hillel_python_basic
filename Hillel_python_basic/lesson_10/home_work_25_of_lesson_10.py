def pow(x):
    return x ** 2

# Намек на генераторную функцию:
def some_gen(begin, end, func):
    """
    begin: первый член последовательности
    end: кол-во элементов в последовательности
    func: функция, которая формирует значения для последовательности
    """
    for i in range(0, end):
        yield begin
        begin = func(begin)



assert list(some_gen(2, 4, pow)) == [2, 4, 16, 256], 'Test1'
print('OK')
