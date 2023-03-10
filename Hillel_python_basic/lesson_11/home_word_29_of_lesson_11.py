def generate_cube_numbers(end):
    el = 2
    while el ** 3 < end:
        yield el ** 3
        el += 1


assert list(generate_cube_numbers(10)) == [8], 'поскольку оно меньше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 в кубе это 125, а оно уже больше 100'
