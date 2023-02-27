def prime_generator(end):
    result = [2]
    if end == 2:
        return result
    if end != 2:
        for el in range(2, end):
            for i in range(2, el):
                if el % i == 0:
                    break
                elif i == el - 1:
                    result.append(el)
        return result


assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
